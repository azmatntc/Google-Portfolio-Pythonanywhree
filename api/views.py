from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
import os
import requests

PROJECTS = [
    {
        "id": 1,
        "title": "AI Portfolio Architect",
        "description": "A full-stack portfolio generator with Django and Svelte.",
        "tech_stack": ["Django", "Svelte", "MySQL", "Gemini"],
        "github_link": "https://github.com/example/portfolio",
        "live_demo": "#",
        "tags": ["Full-Stack", "AI", "Automation"]
    },
    {
        "id": 2,
        "title": "Cloud Automation Tool",
        "description": "Infrastructure as code automation for AWS.",
        "tech_stack": ["Python", "Terraform", "AWS"],
        "github_link": "https://github.com/example/cloud-auto",
        "live_demo": "#",
        "tags": ["DevOps", "Cloud"]
    }
]

def get_projects(request):
    return JsonResponse(PROJECTS, safe=False)

@csrf_exempt
def capture_lead(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if not data.get('name') or not data.get('email') or not data.get('message'):
                return JsonResponse({"message": "All fields are required"}, status=400)
            
            print(f"Lead captured: {data}")
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
