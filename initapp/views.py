from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def home(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def userlogin(request):
    return render(request, 'userlogin.html')


def usersignup(request):
    return render(request, 'usersignup.html')


def userbacklogin(request):
    return render(request, 'userlogin.html')
