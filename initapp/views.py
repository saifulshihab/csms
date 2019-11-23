from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from initapp.models import student_account, headmaster_account, teacher_account


def home(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html')


def usersignup(request):
    return render(request, 'usersignup.html')


def userbacklogin(request):
    return render(request, 'userlogin.html')


def userregistration(request):
    if request.method == 'POST':
        user_select = request.POST['selecteduser']
        print(user_select)
        if user_select == "headmaster":
            userfullname = request.POST['userfullname']
            useremail = request.POST['useremail']
            userempid = request.POST['userempid']
            userpass = request.POST['userpass']
            usercpass = request.POST['usercpass']
            userschool = request.POST['userschool']
            userphone = request.POST['userphone']

            check_headeid = headmaster_account.objects.filter(
                h_empid=userempid)
            if(check_headeid):
                messages.success(
                    request, 'This employee id is already taken! Try again..')
                return render(request, 'usersignup.html')
            else:
                if userpass == usercpass:
                    head_account_create = headmaster_account(
                        h_fullname=userfullname, h_email=useremail, h_empid=userempid, h_pass=userpass, h_school=userschool, h_phone=userphone)
                    head_account_create.save()
                    messages.success(
                        request, "Headmaster account created successfully!")
                    return render(request, 'usersignup.html')
                else:
                    messages.success(request, "Password doesn't match!")
                    return render(request, 'usersignup.html')
        elif user_select == "teacher":
            userfullname = request.POST['userfullname']
            useremail = request.POST['useremail']
            userempid = request.POST['userempid']
            userpass = request.POST['userpass']
            usercpass = request.POST['usercpass']
            userschool = request.POST['userschool']
            userphone = request.POST['userphone']

            check_teacherid = teacher_account.objects.filter(
                t_empid=userempid)
            if (check_teacherid):
                messages.success(
                    request, 'This teacher id is already taken! Try again..')
                return render(request, 'usersignup.html')
            else:
                if userpass == usercpass:
                    teacher_account_create = teacher_account(
                        t_fullname=userfullname, t_email=useremail, t_empid=userempid, t_pass=userpass,
                        t_school=userschool, t_phone=userphone)
                    teacher_account_create.save()
                    messages.success(
                        request, "Teacher account created successfully!")
                    return render(request, 'usersignup.html')


                else:
                    messages.success(request, "Password doesn't match!")
                    return render(request, 'usersignup.html')
        else:
            student_roll = request.POST['student_roll']
            student_pass = request.POST['student_pass']
            student_cpass = request.POST['student_cpass']
            student_class = request.POST['student_class']
            student_school = request.POST['student_school']

            check_roll = student_account.objects.all().filter(
                s_roll=student_roll, s_class=student_class, s_school=student_school)
            if check_roll:
                messages.success(request, "This Roll is already registered!")
                return render(request, 'usersignup.html')
            else:
                if student_pass == student_cpass:
                    std_acc_create = student_account(s_roll=student_roll, s_pass=student_pass, s_class=student_class,
                                                     s_school=student_school)
                    std_acc_create.save()
                    messages.success(
                        request, "Student account created successfully!")
                    return render(request, 'usersignup.html')
                else:
                    messages.success(request, "Password doesn't match!")
                    return render(request, 'usersignup.html')


def userlogin(request):
    if request.method == 'POST':
        user_select = request.POST['selecteduser']

        if user_select == "headmaster":
            userempid= request.POST['userempid']
            userpass = request.POST['userpass']
            login = headmaster_account.objects.filter(h_empid=userempid, h_pass=userpass)
            if login:
                 return redirect('headmaster/')

            else:
                messages.success(request, "Invalid credential! Try again..")
                return render(request, 'userlogin.html')

        elif user_select == "teacher":
            userempid = request.POST['userempid']
            userpass = request.POST['userpass']
            login = teacher_account.objects.filter(t_empid=userempid, t_pass=userpass)
            if login:
                return redirect('teacher/')

            else:
                messages.success(request, "Invalid credential! Try again..")
                return render(request, 'userlogin.html')

        else:
            std_roll = request.POST['stdroll']
            std_pass = request.POST['stdpass']
            std_sch = request.POST['select_school']
            std_cls = request.POST['select_class']

            stdlogin = student_account.objects.filter(
                s_roll=std_roll, s_pass=std_pass,s_school = std_sch, s_class=std_cls)
            if stdlogin:
                return redirect('student/loginsuccess/')
            else:
                messages.success(request,"Wrong login credential! Try again. ..")
                return render(request, 'userlogin.html')
    else:
        return render(request, 'userlogin.html')
