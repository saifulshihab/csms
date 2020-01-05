from django.urls import path
from . import views

urlpatterns = [
    path('loginsuccess/', views.send_feedback, name="loginsuccess"),    
    path('slogout', views.slogout, name="slogout"),
    path('stuChangePass', views.stuChangePass, name="stuChangePass")
]
