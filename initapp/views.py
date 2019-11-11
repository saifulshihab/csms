from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from initapp.models import student_account


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

def userregistration(request):
    if request.method=='POST':
        user_select = request.POST.get('selecteduser')
        if user_select=="Headmaster":
            userfullname = request.POST['userfullname']
            useremail = request.POST['useremail']
            userempid = request.POST['userempid']
            userpass = request.POST['userpass']
            usercpass = request.POST['usercpass']
            userschool = request.POST['userschool']
            userphone = request.POST['userphone']
        elif user_select=="Teacher":
            userfullname = request.POST['userfullname']
            useremail = request.POST['useremail']
            userempid = request.POST['userempid']
            userpass = request.POST['userpass']
            usercpass = request.POST['usercpass']
            userschool = request.POST['userschool']
            userphone = request.POST['userphone']
        else:
            student_roll = request.POST['student_roll']
            student_pass = request.POST['student_pass']
            student_cpass =request.POST['student_cpass']
            student_class = request.POST['student_class']
            student_school = request.POST['student_school']

            check_roll = student_account.objects.all().filter(s_roll=student_roll,s_class=student_class,s_school=student_school)
            if check_roll:
                messages.success(request,"This Roll is already registered!")
                return render(request, 'usersignup.html')
            else:
                if student_pass==student_cpass:
                    std_acc_create = student_account(s_roll=student_roll, s_pass=student_pass, s_class=student_class,
                                                     s_school=student_school)
                    std_acc_create.save()
                    messages.success(request, "Student account created successfully!")
                    return render(request, 'usersignup.html')
                else:
                    messages.success(request, "Password doesn't match!")
                    return render(request, 'usersignup.html')


