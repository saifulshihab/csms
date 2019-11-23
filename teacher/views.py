from django.shortcuts import render
from .models import teacher
from django.contrib import messages
# Create your views here.
def dashboard(request):
    return render(request, 'teacher/dashboard.html')
