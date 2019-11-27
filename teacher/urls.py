from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('teacher_logout', views.teacher_logout, name='teacher_logout')
]
