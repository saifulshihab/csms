from django.shortcuts import render

# Create your views here.


def loginsuccess(request):
    return render(request, 'student_dashboard.html')
