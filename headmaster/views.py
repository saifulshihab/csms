from django.shortcuts import render, redirect
from initapp.models import teacher_verify, headmaster_account, teacher_account, student_account
from school.models import schoolInfo
from .forms import assign_teacher_form
from .models import assign_teacher


def dashboard(request):
    if request.session.has_key('headmaster_eid'):
        hob = headmaster_account.objects.get(
            h_empid=request.session.get('headmaster_eid'))
        obj = schoolInfo.objects.get(SchoolEIIN=hob.sch_eiin)
        total_student = student_account.objects.filter(
            SchoolEIIN=hob.sch_eiin).count()
        total_teacher = teacher_account.objects.filter(
            sch_eiin=hob.sch_eiin).count()
        context = {'school': obj, 'total_student': total_student,
                   'total_teacher': total_teacher}
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
    s_eiin = headmaster_account.objects.get(
        h_empid=request.session.get('headmaster_eid'))
    check_ein = s_eiin.sch_eiin
    tv = teacher_verify.objects.filter(sch_eiin=check_ein)
    return render(request, 'headmaster/teacher_verification.html', {'tv': tv})


def teacher_reject(request, t_empid):
    teacher_verify.objects.filter(t_empid=t_empid).delete()
    return teacherverification(request)


def teacher_approve(request, t_empid):
    ch = teacher_verify.objects.get(t_empid=t_empid)
    teach_account_create = teacher_account(
        t_fullname=ch.t_fullname, t_email=ch.t_email, t_empid=ch.t_empid, t_pass=ch.t_pass, t_phone=ch.t_phone,
        sch_eiin=ch.sch_eiin)
    teach_account_create.save()
    tt = teacher_account.objects.filter(sch_eiin=ch.sch_eiin).count()
    schoolInfo.objects.filter(
        SchoolEIIN=ch.sch_eiin).update(totalTeacher=tt)
    teacher_verify.objects.filter(t_empid=t_empid).delete()
    return teacherverification(request)


def allteachers(request):
    he = headmaster_account.objects.get(
        h_empid=request.session.get('headmaster_eid'))
    t_list = teacher_account.objects.filter(sch_eiin=he.sch_eiin)
    return render(request, 'headmaster/allteacher.html', {'teacher': t_list})


def assign_teacherr(request):
    form = assign_teacher_form()
    """ form.fields["t_empid"] = models.forms.ModelMultipleChoiceField(
        queryset=teacher_account.objects.filter(sch_eiin=request.session.get('headmaster_eid'))) """
    if request.method == 'POST':
        form = assign_teacher_form(request.POST)
        if form.is_valid():
            """ form.initial['sch_eiin'] = request.session.get(
                'headmaster_eid') """
            eiin = headmaster_account.objects.get(h_empid=request.session.get('headmaster_eid'))           
            assign_teacher.objects.create(**form.cleaned_data,sch_eiin=eiin.sch_eiin)
            form = assign_teacher_form()
        else:
            print(form.errors)
    he = headmaster_account.objects.get(
        h_empid=request.session.get('headmaster_eid'))
    obj = assign_teacher.objects.filter(sch_eiin=he.sch_eiin)
    context = {'form': form, 'teacher': obj}
    return render(request, 'headmaster/assign_teacher.html', context)


def change_tname(request):
    ids = request.GET.get('ids')
    obj = teacher_account.objects.get(t_empid=ids)
    print(obj.t_fullname)
    context = {'tname': obj}
    return render(request, 'headmaster/assign_teacher.html', context)


def delete_teacher(request, id):
    assign_teacher.objects.filter(id=id).delete()
    he = headmaster_account.objects.get(
        h_empid=request.session.get('headmaster_eid'))
    obj = assign_teacher.objects.filter(sch_eiin=he.sch_eiin)
    context = {'teacher': obj}
    return assign_teacherr(request)
    return render(request, 'headmaster/assign_teacher.html', context)
