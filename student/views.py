from django.shortcuts import render, redirect
from .forms import feedbackForm
from .models import student_feedback
from initapp.models import student_account
from school.models import schoolInfo
from django.contrib import messages
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

def stuChangePass(request):    
    # passChange_form = passChangeform()
    if request.method=='POST':
        current_pass = request.POST['c_pass']
        new_pass = request.POST['n_pass']
        get_eiin = schoolInfo.objects.get(
            schoolName=request.session.get('std_sch')
        )#Figure out school eiin as student dont know eiin#
        std_obj = student_account.objects.get(
            s_roll=request.session.get('std_roll'),
            s_class=request.session.get('std_class'),
            SchoolEIIN=get_eiin.SchoolEIIN
        )        
        if current_pass==std_obj.s_pass:           
            student_account.objects.filter(
            s_roll=request.session.get('std_roll'),
            s_class=request.session.get('std_class'),
            SchoolEIIN=get_eiin.SchoolEIIN
        ).update(s_pass=new_pass)        
            msg='success'
            context = {'msgsuccess':msg}
            
            messages.success(request, "Password changed !")
            return render(request, 'passwordChange.html', context)
        else:
            msg='failed'
            context = {'msgsuccess':msg}
            messages.success(request, "Current password doesn't match. Try again. ..")
            return render(request, 'passwordChange.html', context)
    return render(request, 'passwordChange.html')

def slogout(request):
    return redirect('home')
