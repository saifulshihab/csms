from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('head_logout', views.head_logout, name="head_logout"),    
    path('', views.dashboard, name='dashboard'),
    path('about', views.about, name='about')

]
