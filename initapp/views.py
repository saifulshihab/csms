from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def home(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')
