from flask import Flask, send_from_directory, request, jsonify
import os
import requests
from flask_cors import CORS

app = Flask(__name__, static_folder='dist', static_url_path='')
CORS(app)

# Mock Project Data
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

@app.route('/api/projects', methods=['GET'])
def get_projects():
    return jsonify(PROJECTS)

@app.route('/api/leads', methods=['POST'])
def capture_lead():
    data = request.json
    if not data.get('name') or not data.get('email') or not data.get('message'):
        return jsonify({"message": "All fields are required"}), 400
    
    print(f"Lead captured: {data}")
    return jsonify({"status": "success", "message": "Lead captured successfully"}), 201

@app.route('/api/chat', methods=['POST'])
def chat_proxy():
    data = request.json
    api_key = os.environ.get('GEMINI_API_KEY')
    
    if not api_key:
        return jsonify({"error": "Gemini API key not configured"}), 500

    # Simple proxy to Gemini API (using requests for PythonAnywhere compatibility)
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={api_key}"
    payload = {
        "contents": [{"parts": [{"text": data.get('message', '')}]}]
    }
    
    try:
        response = requests.post(url, json=payload)
        response_data = response.json()
        reply = response_data['candidates'][0]['content']['parts'][0]['text']
        return jsonify({"reply": reply})
    except Exception as e:
        print(f"AI Chat Error: {e}")
        return jsonify({"error": "Failed to process AI request"}), 500

# Serve Svelte App
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if path != "" and os.path.exists(app.static_folder + '/' + path):
        return send_from_directory(app.static_folder, path)
    else:
        return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(port=3000)
