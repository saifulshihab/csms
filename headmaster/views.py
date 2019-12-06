from django.shortcuts import render, redirect
from initapp.models import teacher_verify, headmaster_account, teacher_account
from school.models import schoolInfo


# Create your views here.


def dashboard(request):
    if request.session.has_key('headmaster_eid'):
        hob = headmaster_account.objects.get(h_empid=request.session.get('headmaster_eid'))
        print(hob.sch_eiin)
        obj = schoolInfo.objects.get(SchoolEIIN=hob.sch_eiin)
        context = {'school': obj}
        return render(request, 'headmaster/dashboard.html', context)
    else:
        return redirect('userlogin')


def head_logout(request):
    try:
        del request.session['headmaster_eid']
    except KeyError:
        pass
    return redirect('home')


def about(request):
    return render(request, 'about.html')


def teacherverification(request):
    s_eiin = headmaster_account.objects.get(h_empid = request.session.get('headmaster_eid'))
    check_ein = s_eiin.sch_eiin
    tv = teacher_verify.objects.filter(sch_eiin=check_ein)    
    return render(request, 'headmaster/teacher_verification.html', {'tv': tv})

def teacher_reject(request, t_empid):    
    teacher_verify.objects.filter(t_empid=t_empid).delete()
    return teacherverification(request)

def teacher_approve(request, t_empid):
    ch = teacher_verify.objects.get(t_empid=t_empid)
    teach_account_create = teacher_account(
                            t_fullname=ch.t_fullname, t_email=ch.t_email, t_empid=ch.t_empid, t_pass=ch.t_pass, t_phone=ch.t_phone, sch_eiin=ch.sch_eiin)
    teach_account_create.save()
    teacher_verify.objects.filter(t_empid=t_empid).delete()
    return teacherverification(request)

def allteachers(request):
    he = headmaster_account.objects.get(h_empid = request.session.get('headmaster_eid'))
    t_list = teacher_account.objects.filter(sch_eiin = he.sch_eiin)
    return render(request, 'headmaster/allteacher.html', {'teacher':t_list})