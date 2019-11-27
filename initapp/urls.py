from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),   
    path('about', views.about, name="about"),
    path('userlogin', views.userlogin, name="userlogin"),
    path('usersignup', views.usersignup, name="usersignup"),
    path('userbacklogin', views.userbacklogin, name="userbacklogin"),
    path('userregistration', views.userregistration, name="userregistration")
]
