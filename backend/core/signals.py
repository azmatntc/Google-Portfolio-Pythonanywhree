from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Lead
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Lead)
def handle_new_lead(sender, instance, created, **kwargs):
    if created:
        # 1. Send internal notification
        send_mail(
            f"New High-Score Lead: {instance.name}",
            f"Score: {instance.score}\nMessage: {instance.message}",
            settings.DEFAULT_FROM_EMAIL,
            [settings.ADMIN_EMAIL],
            fail_silently=False,
        )
        
        # 2. Send automated follow-up if score is high
        if instance.score >= 30:
            send_mail(
                "Thanks for reaching out!",
                "I've received your message and will get back to you shortly. Let's build something great.",
                settings.DEFAULT_FROM_EMAIL,
                [instance.email],
                fail_silently=False,
            )
