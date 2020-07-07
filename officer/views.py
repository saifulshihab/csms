from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import redirect
from officer.models import officer_account, coordiinator, assign_cordinator
from django.contrib import messages
from school.models import schoolInfo
from headmaster.models import headmaster_account, headmaster_verify
from teacher.models import teacher_account
from student.models import student_account
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
        has_headmaster = headmaster_account.objects.filter(
            sch_eiin=school_eiin)
        if has_headmaster:
            total_student = student_account.objects.filter(
            SchoolEIIN=school_eiin).count()
            total_teacher = teacher_account.objects.filter(
                sch_eiin=school_eiin).count()
            headmaster_obj = headmaster_account.objects.get(
                sch_eiin=school_eiin)
            teacher_list_obj = teacher_account.objects.filter(sch_eiin=school_eiin)
            total_male_t = teacher_account.objects.filter(sch_eiin=school_eiin, gender='Male').count()
            total_female_t = teacher_account.objects.filter(sch_eiin=school_eiin, gender='Female').count()
            co = coordiinator.objects.all()
            s_feedback = student_feedback.objects.filter(
                school=school_obj.schoolName)
            context = {
                'school': school_obj,
                'headmaster': headmaster_obj,
                'feedback': s_feedback,
                'total_student': total_student,
                'total_teacher': total_teacher,
                'co':co,
                'total_male_t': total_male_t,
                'total_female_t': total_female_t,
                'teacher_list_obj': teacher_list_obj
            }     
            return render(request, 'school_detail_view.html', context)
        else:
            return render(request, 'school_detail_view.html', {'school': school_obj})
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


def reject_head(request, h_empid):
    headmaster_verify.objects.filter(h_empid=h_empid).delete()
    hv = headmaster_verify.objects.all()
    return render(request, 'hverify.html', {'hv': hv})


def head_approve(request, h_empid):
    ch = headmaster_verify.objects.get(h_empid=h_empid)
    head_account_create = headmaster_account(
        h_fullname=ch.h_fullname, h_email=ch.h_email, dp=ch.dp, h_empid=ch.h_empid, h_pass=ch.h_pass, h_phone=ch.h_phone, sch_eiin=ch.sch_eiin)
    head_account_create.save()
    headmaster_verify.objects.filter(h_empid=h_empid).delete()
    hv = headmaster_verify.objects.all()
    return render(request, 'hverify.html', {'hv': hv})


def allheadmasters(request):
    obj = headmaster_account.objects.all()
    return render(request, 'allheadmaster.html', {'headmasters': obj})


def registered_schools(request):
    obj = schoolInfo.objects.all()
    return render(request, 'registered_schools.html', {'schools': obj})


def assign_co(request, se):
    if request.method=='POST':
        name = request.POST['name']        
        phn = coordiinator.objects.get(name=name).h_phone
        assign_cordinator.objects.create(name=name, phone=phn, sch_eiin = se)
        return render(request, 'school_detail_view.html')