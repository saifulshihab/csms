from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from officer.models import officer_account
from django.contrib import messages
from school.models import schoolInfo
from initapp.models import headmaster_account, teacher_account, headmaster_verify
from student.models import student_feedback
# Create your views here.


def enterOfficer(request):
    if request.session.has_key('empid'):
        school = schoolInfo.objects.all()
        return render(request, 'dashboard.html', {'school': school})
    else:
        return render(request, 'login.html')


def registration(request):
    if request == "POST":
        pass
    else:
        return render(request, 'registration.html')


def backlogin(request):
    return render(request, 'login.html')


def officerReg(request):
    if request.method == "POST":
        oname = request.POST['oname']
        oemail = request.POST['oemail']
        oempid = request.POST['oempid']
        opass = request.POST['opass']
        ocpass = request.POST['ocpass']
        oworkp = request.POST['oworkp']
        check_eid = officer_account.objects.filter(oempid=oempid)
        if check_eid:
            messages.success(request, 'Employee ID is already taken!')
            return render(request, 'registration.html')
        else:
            if opass == ocpass:
                acc_save = officer_account(
                    oname=oname, oemail=oemail, oempid=oempid, opass=opass, oworkp=oworkp)
                acc_save.save()
                messages.success(request, 'Registration successfull!')
                return render(request, 'registration.html')
            else:
                messages.success(request, "Password doesn't match!")
                return render(request, 'registration.html')

    else:
        return render(request, 'registration.html')


def offcierLogin(request):
    if request.method == "POST":
        oempid = request.POST['oempid']
        opass = request.POST['opass']
        login = officer_account.objects.filter(oempid=oempid, opass=opass)
        if login:
            request.session['empid'] = oempid
            school = schoolInfo.objects.all()
            return render(request, 'dashboard.html', {'school': school})
        else:
            messages.success(request, "Invalid credential! Try again..")
            return render(request, 'login.html')
    else:
        if request.session.has_key('empid'):
            school = schoolInfo.objects.all()
            return render(request, 'dashboard.html', {'school': school})
        else:
            return render(request, 'login.html')


def logout(request):
    try:
        del request.session['empid']
    except KeyError:
        pass
    return redirect('home')


def school_detail(request, school_eiin):
    try:
        school_obj = schoolInfo.objects.get(SchoolEIIN=school_eiin)
        headmaster_obj = headmaster_account.objects.filter(
            sch_eiin=school_eiin)
        teacher_list_obj = teacher_account.objects.filter(sch_eiin=school_eiin)
        context = {'school': school_obj, 'headmaster': headmaster_obj}
        if headmaster_obj and teacher_list_obj:
            headmaster_obj = headmaster_account.objects.get(
                sch_eiin=school_eiin)
            teacher_list_obj = teacher_account.objects.all()
            context = {'school': school_obj,
                       'headmaster': headmaster_obj, 'teacher': teacher_list_obj}
            return render(request, 'school_detail_view.html', context)
        elif headmaster_obj:
            headmaster_obj = headmaster_account.objects.get(
                sch_eiin=school_eiin)
            context = {'school': school_obj, 'headmaster': headmaster_obj}
            messages.success(
                request, "This school's teacher is not registered yet!")
            return render(request, 'school_detail_view.html', context)
        elif teacher_list_obj:
            teacher_list_obj = teacher_account.objects.all()
            context = {'school': school_obj, 'teacher': teacher_list_obj}
            messages.success(request, "This headmaster is not registered yet!")
            return render(request, 'school_detail_view.html', context)
        else:
            context = {'school': school_obj}
            messages.success(
                request, "There are no headmaster/teacher yet registered!")
            return render(request, 'school_detail_view.html', context)
    except schoolInfo.DoesNotExist:
        raise Http404


def dash(request):
    school = schoolInfo.objects.all()
    return render(request, 'dashboard.html', {'school': school})


def hpend(request):
    hv = headmaster_verify.objects.all()
    return render(request, 'hverify.html', {'hv': hv})


def student_feedbacks(request):
    if request.session.has_key('empid'):
        obj = student_feedback.objects.all()
        return render(request, 'student_feedback.html', {'feedback': obj})
