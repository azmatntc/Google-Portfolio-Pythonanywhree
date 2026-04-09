from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.get_projects, name='get_projects'),
    path('leads/', views.capture_lead, name='capture_lead'),
    path('chat/', views.chat_proxy, name='chat_proxy'),
    # Also support without trailing slash
    path('projects', views.get_projects),
    path('leads', views.capture_lead),
    path('chat', views.chat_proxy),
]
