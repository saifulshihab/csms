from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="Index"),
    path('home', views.home, name="home"),
    path('about', views.about, name="about"),
    path('userlogin', views.userlogin, name="userlogin"),
    path('usersignup', views.usersignup, name="usersignup"),
    path('userbacklogin', views.userbacklogin, name="userbacklogin"),
    path('userregistration', views.userregistration, name="userregistration")
]
