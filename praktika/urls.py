from django.urls import path
from app import views

urlpatterns = [
    path('', views.main),
    path('process_text/', views.process_text),
]