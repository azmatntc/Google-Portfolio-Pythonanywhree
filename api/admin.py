from django.contrib import admin
from .models import Lead, Project, AnalyticsEvent


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "score", "created_at", "last_interaction")
    search_fields = ("name", "email", "message")
    list_filter = ("created_at", "last_interaction", "score")
    ordering = ("-created_at",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "order", "is_featured", "github_link", "live_demo")
    search_fields = ("title", "description")
    list_filter = ("is_featured",)
    ordering = ("order",)


@admin.register(AnalyticsEvent)
class AnalyticsEventAdmin(admin.ModelAdmin):
    list_display = ("event_type", "path", "session_id", "timestamp")
    search_fields = ("event_type", "path", "session_id")
    list_filter = ("event_type", "timestamp")
    ordering = ("-timestamp",)
