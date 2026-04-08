from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Lead, Project, AnalyticsEvent
from .serializers import LeadSerializer, ProjectSerializer
import google.generativeai as genai
from django.conf import settings

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.filter(is_featured=True)
    serializer_class = ProjectSerializer

class LeadViewSet(viewsets.ModelViewSet):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    def create(self, request, *args, **kwargs):
        # Lead scoring logic
        data = request.data
        score = 10 # Base score for submission
        if len(data.get('message', '')) > 100:
            score += 20
        
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        lead = serializer.save(score=score)
        
        # Trigger automation signal (handled in signals.py)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class AIChatView(viewsets.ViewSet):
    def create(self, request):
        message = request.data.get('message')
        if not message:
            return Response({"error": "Message is required"}, status=400)
            
        try:
            genai.configure(api_key=settings.GEMINI_API_KEY)
            model = genai.GenerativeModel('gemini-1.5-flash')
            response = model.generate_content(message)
            return Response({"reply": response.text})
        except Exception as e:
            return Response({"error": str(e)}, status=500)
