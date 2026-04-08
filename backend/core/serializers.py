from rest_framework import serializers
from .models import Lead, Project

class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
        read_only_fields = ['score', 'created_at', 'last_interaction']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
