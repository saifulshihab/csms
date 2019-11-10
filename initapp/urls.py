from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name="Index"),
    path('home', views.home, name="home"),
    path('admin/', admin.site.urls),
]
