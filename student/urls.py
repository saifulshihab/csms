from django.urls import path
from . import views

urlpatterns = [
    path('loginsuccess/', views.loginsuccess, name="loginsuccess"),
    path('', views.send_feedback, name="send_feedback")
]
