# 🚀 Production Deployment Guide (PythonAnywhere)

## 1. Prerequisites
- PythonAnywhere account (Paid for MySQL and external API access)
- GitHub repository
- AWS Account (SES for emails)
- Google Gemini API Key

## 2. Backend Setup (Django)
1. Create a virtualenv: `mkvirtualenv --python=/usr/bin/python3.11 my-app`
2. Install requirements: `pip install django djangorestframework django-cors-headers mysqlclient google-generativeai boto3`
3. Configure MySQL in PythonAnywhere dashboard.
4. Update `backend/settings/prod.py` with DB credentials and secrets.
5. Run migrations: `python manage.py migrate`

## 3. Frontend Integration
1. Build locally: `npm run build`
2. Copy `dist/` contents to `backend/static/frontend/`
3. Run `python manage.py collectstatic` on PythonAnywhere.

## 4. Web App Configuration
1. Set up WSGI file pointing to `backend/wsgi.py`.
2. Add static file mappings:
   - `/static/` -> `~/my-app/backend/static/`
   - `/media/` -> `~/my-app/backend/media/`

## 5. Security Checklist
- [ ] `DEBUG = False` in production
- [ ] `ALLOWED_HOSTS` configured
- [ ] CSRF/CORS restricted to your domain
- [ ] Environment variables used for all keys
- [ ] Rate limiting enabled on API endpoints
