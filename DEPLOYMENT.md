# 🚀 PythonAnywhere Deployment Guide (Veteran Recommended)

This application is a full-stack project with a **Django backend** and a **Svelte frontend**. This guide follows industry best practices for a stable, production-ready deployment on PythonAnywhere.

## 1. Project Structure Overview
- `/portfolio_project`: Django project settings.
- `/api`: Django app for backend logic.
- `/src`: Svelte frontend source.
- `/dist`: Built frontend assets (served by Django).
- `/staticfiles`: Collected static files for production.

## 2. Prerequisites
1. A PythonAnywhere account (Paid account recommended for SSH/GitHub Actions).
2. A GitHub repository for your code.
3. Your `GEMINI_API_KEY` from AI Studio.

## 3. Initial Setup on PythonAnywhere

### A. Clone the Repository
Open a **Bash Console** on PythonAnywhere and run:
```bash
git clone https://github.com/yourusername/your-repo.git portfolio
cd portfolio
```

### B. Create a Virtual Environment
```bash
mkvirtualenv portfolio-env --python=python3.10
pip install -r requirements.txt
```

### C. Configure Environment Variables
Create a `.env` file in the root directory:
```bash
nano .env
```
Add the following (replace with your actual values):
```env
DJANGO_SECRET_KEY="your-random-secret-key"
DJANGO_DEBUG="False"
DJANGO_ALLOWED_HOSTS="yourusername.pythonanywhere.com"
GEMINI_API_KEY="your-gemini-api-key"
```

### D. Initial Build and Migration
```bash
# Build the frontend (if npm is available, otherwise build locally and push)
npm install
npm run build

# Run migrations
python manage.py migrate

# Create a superuser to access the Admin Panel
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

## 4. Activate Admin Panel
Once the server is running:
1. Visit `https://yourusername.pythonanywhere.com/admin`.
2. Log in with the superuser credentials you just created.
3. You can now manage Projects, Leads, and Analytics directly.
4. Custom actions like "Mark as Contacted" have been pre-configured for you.

## 5. Web Tab Configuration

1. **Source Code**: `/home/yourusername/portfolio`
2. **Working Directory**: `/home/yourusername/portfolio`
3. **Virtualenv**: `/home/yourusername/.virtualenvs/portfolio-env`
4. **Static Files**:
   - URL: `/static/` -> Directory: `/home/yourusername/portfolio/staticfiles/`
5. **WSGI Configuration**:
   Edit the WSGI file (link in the Web tab) and replace its content with:
   ```python
   import os
   import sys
   from dotenv import load_dotenv

   path = '/home/yourusername/portfolio'
   if path not in sys.path:
       sys.path.append(path)

   load_dotenv(os.path.join(path, '.env'))

   os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio_project.settings'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

## 5. Automated Deployment (GitHub Actions)

We have pre-configured `.github/workflows/deploy.yml`. To use it, add these **Secrets** to your GitHub repository:
- `PA_USERNAME`: Your PythonAnywhere username.
- `PA_API_TOKEN`: Your PythonAnywhere API token (from Account -> API Token).
- `PA_DOMAIN`: Your domain (e.g., `yourusername.pythonanywhere.com`).
- `SSH_PRIVATE_KEY`: Your SSH private key (ensure the public key is in `~/.ssh/authorized_keys` on PythonAnywhere).

## 6. Stability Best Practices
- **WhiteNoise**: Used for serving static files efficiently from Django.
- **CSRF Protection**: Ensure `CORS_ALLOWED_ORIGINS` is restricted in production.
- **Error Logging**: Check `/var/log/yourusername.pythonanywhere.com.error.log` for troubleshooting.
- **Database**: For high traffic, migrate from SQLite to MySQL (available on PythonAnywhere).
