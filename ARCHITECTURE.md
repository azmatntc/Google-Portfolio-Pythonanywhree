# 🚀 SYSTEM ARCHITECTURE (PythonAnywhere Optimized)

```text
[ CLIENT BROWSER ]
       |
       | (HTTPS)
       v
[ PYTHONANYWHERE WEB SERVER ]
       |
       +--- [ DJANGO 5.0 ] (WSGI)
       |       |
       |       +--- [ DRF API ] <--- [ SVELTE FRONTEND ] (Static Files)
       |       |
       |       +--- [ SERVICES ]
       |               |
       |               +--- [ GEMINI AI ] (Google API)
       |               +--- [ AWS SES ] (Email Notifications)
       |
       +--- [ MYSQL DB ] (Lead Tracking, Projects, Analytics)
```

# 📁 PROJECT STRUCTURE

## Backend (Django)
```text
backend/
├── core/
│   ├── models.py (Leads, Projects, Analytics)
│   ├── views.py (API Endpoints, AI Proxy)
│   ├── serializers.py
│   ├── signals.py (Automation Triggers)
│   └── urls.py
├── settings/
│   ├── base.py
│   ├── dev.py
│   └── prod.py
├── static/
│   └── frontend/ (Svelte dist/ copy)
└── manage.py
```

## Frontend (Svelte)
```text
src/
├── components/
│   ├── Hero.svelte
│   ├── ProjectCard.svelte
│   ├── ContactForm.svelte
│   └── AIChatWidget.svelte
├── lib/
│   └── api.ts
├── App.svelte
└── main.ts
```
