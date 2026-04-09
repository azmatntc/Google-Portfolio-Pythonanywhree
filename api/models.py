from django.db import models
from django.utils import timezone

class Lead(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    score = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    last_interaction = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.name} ({self.email})"

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    tech_stack = models.JSONField(default=list)  # List of strings
    tags = models.JSONField(default=list)        # List of strings
    features = models.JSONField(default=list)    # List of strings
    github_link = models.URLField(blank=True)
    live_demo = models.URLField(blank=True)
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class AnalyticsEvent(models.Model):
    event_type = models.CharField(max_length=50) # page_visit, button_click, etc.
    path = models.CharField(max_length=255)
    session_id = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    metadata = models.JSONField(default=dict)

    def __str__(self):
        return f"{self.event_type} at {self.path}"
