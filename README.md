# Elite AI Portfolio Architect

A high-performance, production-ready portfolio system built with **Django 5.0**, **Svelte 5**, and **Gemini AI**. This project is optimized for deployment on PythonAnywhere and features a sleek, animated interface with real-time lead tracking and AI-powered interaction.

## 🚀 Features

- **Elite UI/UX**: Crafted with Tailwind CSS and Svelte 5, featuring smooth animations and a distinctive "Elite" aesthetic.
- **AI-Powered**: Integrated Gemini AI for real-time chat and content generation.
- **Full-Stack Architecture**: Robust Django backend with a reactive Svelte frontend.
- **Lead Management**: Automated lead capture with a professional Django Admin dashboard.
- **Analytics**: Built-in event tracking to monitor user engagement.
- **Dark Mode**: Native dark/light mode support with system preference detection.

## 🛠️ Tech Stack

- **Frontend**: Svelte 5, Tailwind CSS, Lucide Icons, Motion (for animations).
- **Backend**: Django 5.0, Django REST Framework.
- **AI**: Google Gemini API.
- **Database**: SQLite (Dev) / MySQL (Prod).
- **Deployment**: Optimized for PythonAnywhere.

## 📦 Installation & Setup

### Prerequisites
- Python 3.10+
- Node.js 18+
- Gemini API Key (from [Google AI Studio](https://aistudio.google.com/))

### Quick Setup (PythonAnywhere)
1. Upload the files or clone the repo.
2. Run the setup script:
   ```bash
   bash setup_django.sh
   ```

### Manual Backend Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run migrations:
   ```bash
   python manage.py migrate
   ```
3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```
4. Start the server:
   ```bash
   python manage.py runserver
   ```

### Frontend Setup
1. Install dependencies:
   ```bash
   npm install
   ```
2. Build the project:
   ```bash
   npm run build
   ```

## 🌐 Deployment

For detailed deployment instructions on PythonAnywhere, see [DEPLOYMENT.md](./DEPLOYMENT.md).

## 📄 License

This project is licensed under the MIT License.
