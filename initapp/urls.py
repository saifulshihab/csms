from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Index"),   
    path('home', views.home, name="home"),
    path('about', views.about, name="about")
]
