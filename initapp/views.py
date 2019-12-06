from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from initapp.models import student_account, headmaster_account, teacher_account, headmaster_verify, teacher_verify
from school.models import schoolInfo


def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def index(request):
    return render(request, 'index.html')


def usersignup(request):
    return render(request, 'usersignup.html')


def userbacklogin(request):
    return render(request, 'userlogin.html')


def userregistration(request):
    if request.method == 'POST':
        user_select = request.POST['selecteduser']       
        if user_select == "headmaster":
            check_eiin = schoolInfo.objects.filter(
                SchoolEIIN=request.POST['user_eiin'])
            if check_eiin:
                check_multi_head = headmaster_verify.objects.filter(
                    sch_eiin=request.POST['user_eiin'])
                if check_multi_head:
                    messages.success(
                        request, 'Headmaster already registered!')
                    return render(request, 'usersignup.html')
                else:
                    if request.POST['userpass'] == request.POST['usercpass']:
                        head_account_create = headmaster_verify(
                            h_fullname=request.POST['userfullname'], h_email=request.POST['useremail'], h_empid=request.POST['userempid'], h_pass=request.POST['userpass'], h_phone=request.POST['userphone'], sch_eiin=request.POST['user_eiin'])
                        head_account_create.save()
                        messages.success(
                            request, "Headmaster account created successfully. Wait for verification!")
                        return render(request, 'usersignup.html')
                    else:
                        messages.success(request, "Password doesn't match!")
                        return render(request, 'usersignup.html')
            else:
                messages.success(
                    request, "This school info isn't registered yet in system! Try back later. ..")
                return render(request, 'usersignup.html')
        elif user_select == "teacher":
            check_eiin = schoolInfo.objects.filter(
                SchoolEIIN=request.POST['user_eiin'])
            if check_eiin:
                check_teach_id = teacher_verify.objects.filter(
                    t_empid=request.POST['userempid'])
                if(check_teach_id):
                    messages.success(
                        request, 'This employee id is already taken! Try again..')
                    return render(request, 'usersignup.html')
                else:
                    if request.POST['userpass'] == request.POST['usercpass']:
                        teach_account_verify_create = teacher_verify(
                            t_fullname=request.POST['userfullname'], t_email=request.POST['useremail'], t_empid=request.POST['userempid'], t_pass=request.POST['userpass'], t_phone=request.POST['userphone'], sch_eiin=request.POST['user_eiin'])
                        teach_account_verify_create.save()
                        messages.success(
                            request, "Teacher account created successfully. Wait for verification!")
                        return render(request, 'usersignup.html')
                    else:
                        messages.success(request, "Password doesn't match!")
                        return render(request, 'usersignup.html')
            else:
                messages.success(
                    request, "This school isn't registered yet in the system! Try back later. ..")
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
            userempid = request.POST['userempid']
            userpass = request.POST['userpass']
            login = headmaster_account.objects.filter(
                h_empid=userempid, h_pass=userpass)
            if login:
                request.session['headmaster_eid'] = userempid
                return redirect('headmaster/')

            else:
                messages.success(request, "Invalid credential! Try again..")
                return render(request, 'userlogin.html')

        elif user_select == "teacher":
            userempid = request.POST['userempid']
            userpass = request.POST['userpass']
            login = teacher_account.objects.filter(
                t_empid=userempid, t_pass=userpass)
            if login:
                request.session['teacher_eid'] = userempid
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
                s_roll=std_roll, s_pass=std_pass, s_school=std_sch, s_class=std_cls)
            if stdlogin:
                # request.session['teacher_eid'] = userempid
                return redirect('student/loginsuccess/')
            else:
                messages.success(
                    request, "Wrong login credential! Try again. ..")
                return render(request, 'userlogin.html')
    else:
        '''if request.session.has_key('headmaster_eid'):
            return redirect('headmaster/')
        elif request.session.has_key('teacher_eid'):
            return redirect('teacher/')
        else:'''
        return render(request, 'userlogin.html')
