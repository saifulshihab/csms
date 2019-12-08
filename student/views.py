from django.shortcuts import render, redirect
from .forms import feedbackForm
from .models import student_feedback


def loginsuccess(request):
    return render(request, 'student_dashboard.html')

def send_feedback(request):
    feedback_form = feedbackForm()
    if request.method == 'POST':
        feedback_form = feedbackForm(request.POST)
        if feedback_form.is_valid():
            student_feedback.objects.create(**feedback_form.cleaned_data)
            feedback_form = feedbackForm()
        else:
            print(feedback_form.errors)
    context = {'form': feedback_form}
    return render(request, 'student_dashboard.html', context)

def slogout(request):
    return redirect('home')