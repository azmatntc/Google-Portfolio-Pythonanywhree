from django.contrib import admin
from .models import Lead, Project, AnalyticsEvent

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'score', 'created_at', 'is_contacted')
    search_fields = ('name', 'email')
    list_filter = ('created_at', 'score')
    actions = ['mark_as_contacted']

    def is_contacted(self, obj):
        return obj.score > 0 # Simple logic for demo
    is_contacted.boolean = True

    @admin.action(description='Mark selected leads as contacted')
    def mark_as_contacted(self, request, queryset):
        queryset.update(score=10) # Update score to indicate contact
        self.message_user(request, "Selected leads have been marked as contacted.")

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_featured', 'tech_stack_count')
    list_editable = ('order', 'is_featured')
    search_fields = ('title', 'description')
    list_filter = ('is_featured',)
    
    def tech_stack_count(self, obj):
        return len(obj.tech_stack) if obj.tech_stack else 0
    tech_stack_count.short_description = 'Tech Count'

@admin.register(AnalyticsEvent)
class AnalyticsEventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'path', 'timestamp')
    list_filter = ('event_type', 'timestamp')
