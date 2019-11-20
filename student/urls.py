from django.urls import path
from . import views

urlpatterns = [
    path('loginsuccess/', views.loginsuccess, name="loginsuccess")
]
