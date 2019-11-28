from django.urls import path
from . import views

urlpatterns = [
    path('loginsuccess/', views.send_feedback, name="loginsuccess"),    
]
