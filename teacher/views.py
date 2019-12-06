from django.shortcuts import render, redirect
from .models import teacher
# Create your views here.


def dashboard(request):
    if request.session.has_key('teacher_eid'):
        return render(request, 'teacher/dashboard.html')
    else:
        return redirect('userlogin')

def teach_logout(request):
    try:
        del request.session['teacher_eid']
    except KeyError:
        pass
    return redirect('home')