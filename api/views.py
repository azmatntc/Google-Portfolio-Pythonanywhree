from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Project, Lead
import json
import os
import requests

def get_projects(request):
    featured_param = request.GET.get('featured')
    data = []
    
    try:
        projects = Project.objects.all().order_by('order')
        
        if featured_param == 'true':
            projects = projects.filter(is_featured=True)
        elif featured_param == 'false':
            projects = projects.filter(is_featured=False)
            
        for p in projects:
            data.append({
                "id": p.id,
                "title": p.title,
                "description": p.description,
                "tech_stack": p.tech_stack,
                "tags": p.tags,
                "features": p.features,
                "github_link": p.github_link,
                "live_demo": p.live_demo,
                "is_featured": p.is_featured
            })
    except Exception as e:
        print(f"Database error in get_projects: {e}")
        # Fallback data will be used below if data is empty
    
    # Fallback to hardcoded if DB is empty for initial setup
    if not data:
        data = [
            {
                "id": 1,
                "title": "AI Portfolio Architect",
                "description": "A full-stack portfolio generator with Django and Svelte. This system automates the creation of professional developer portfolios by analyzing GitHub repositories and generating optimized content using Gemini AI.",
                "tech_stack": ["Django", "Svelte", "MySQL", "Gemini"],
                "tags": ["Full-Stack", "AI", "Automation"],
                "features": ["GitHub Repo Analysis", "AI Content Generation", "Real-time Previews", "One-click Deployment"],
                "github_link": "https://github.com/example/portfolio",
                "live_demo": "#",
                "is_featured": True
            }
        ]
    return JsonResponse(data, safe=False)

@csrf_exempt
def capture_lead(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            email = data.get('email')
            message = data.get('message')
            
            if not name or not email or not message:
                return JsonResponse({"message": "All fields are required"}, status=400)
            
            Lead.objects.create(name=name, email=email, message=message)
            return JsonResponse({"status": "success", "message": "Lead captured successfully"}, status=201)
        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON"}, status=400)
    return JsonResponse({"message": "Method not allowed"}, status=405)

@csrf_exempt
def chat_proxy(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            api_key = os.environ.get('GEMINI_API_KEY')
            
            if not api_key:
                return JsonResponse({"error": "Gemini API key not configured"}, status=500)

            url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={api_key}"
            payload = {
                "contents": [{"parts": [{"text": data.get('message', '')}]}]
            }
            
            response = requests.post(url, json=payload)
            response_data = response.json()
            reply = response_data['candidates'][0]['content']['parts'][0]['text']
            return JsonResponse({"reply": reply})
        except Exception as e:
            print(f"AI Chat Error: {e}")
            return JsonResponse({"error": "Failed to process AI request"}, status=500)
    return JsonResponse({"message": "Method not allowed"}, status=405)
