from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('teacher_logout', views.teach_logout, name='teach_logout'),    
    path('allstudent', views.allstudent, name="allstudent"),
    path('classes', views.classes, name="classes"),
    path('enterClass/<str:classno>', views.enterClass, name="enterClass")
]
