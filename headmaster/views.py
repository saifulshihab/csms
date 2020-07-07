from django.shortcuts import render, redirect
from teacher.models import teacher_verify, teacher_account
from school.models import schoolInfo
from student.models import student_account
from .models import assign_teacher, headmaster_account, headmaster_verify
from .forms import headmasterLoginForm, assign_teacher_form, headmasterRegForm, profileUpForm

def login(request):
    if request.session.has_key('headmaster_eid'):
        return redirect('../headmaster')
    else:
        context = {'loginForm': headmasterLoginForm()}
        if request.method == 'POST':        
            form = headmasterLoginForm(request.POST)
            check_pending_registration = headmaster_verify.objects.filter(h_empid=form.data['h_empid'], h_pass=form.data['h_pass'])    
            loggedin = headmaster_account.objects.filter(h_empid=form.data['h_empid'], h_pass=form.data['h_pass'])    
            if loggedin:
                request.session['headmaster_eid'] = form.data['h_empid']
                return redirect('../headmaster')
            elif check_pending_registration:
                context.update({'message': 'Your account is under review! Check back later.. .'})        
            else:
                context.update({'message': 'Invalid credential!'})        
        return render(request, 'headmaster/login.html', context)

def headmasterSession(request):
    return headmaster_account.objects.get(
        h_empid=request.session.get('headmaster_eid'))

def signup(request):
    form = headmasterRegForm()
    context = {
        'regForm': form,
        'msgtype': 'failed',
        'message': ''
    }
    if request.method == 'POST':
        form = headmasterRegForm(request.POST, request.FILES)        
        if form.is_valid():
            sch_exist = schoolInfo.objects.filter(SchoolEIIN=form.data['sch_eiin'])
            if sch_exist:
                head_exist = headmaster_verify.objects.filter(sch_eiin=form.data['sch_eiin'])
                head_exist2 = headmaster_account.objects.filter(sch_eiin=form.data['sch_eiin'])
                if head_exist or head_exist2:
                    context.update({                    
                        'message': 'This headmaster is already registered!'                    
                    })
                else:
                    empidtaken = headmaster_verify.objects.filter(h_empid=form.data['h_empid'])
                    empidtaken2 = headmaster_account.objects.filter(h_empid=form.data['h_empid'])
                    if empidtaken or empidtaken2: 
                        context.update({
                            'message': 'This Employee Id is taken!'
                        })                       
                    else:
                        form.save()
                        context.update({
                            'message': 'Registration successful! Wait for officer varification.',
                            'msgtype': 'pending'
                        })  
            else:
                context.update({
                    'message': 'This school with EIIN is not registered yet!'                    
                })
    return render(request, 'headmaster/signup.html', context)

def dashboard(request):
    if request.session.has_key('headmaster_eid'):
        hob = headmasterSession(request)
        sobj = schoolInfo.objects.get(SchoolEIIN=hob.sch_eiin)
        total_teacher = teacher_account.objects.filter(sch_eiin=hob.sch_eiin).count()
        total_male_t = teacher_account.objects.filter(sch_eiin=hob.sch_eiin, gender='Male').count()
        total_female_t = teacher_account.objects.filter(sch_eiin=hob.sch_eiin, gender='Female').count()        
        total_student = student_account.objects.filter(SchoolEIIN=hob.sch_eiin).count()
        context = {
            'school': sobj, 
            'total_student': total_student,
            'total_teacher': total_teacher,
            'total_female_t': total_female_t,
            'total_male_t': total_male_t
        }
        return render(request, 'headmaster/dashboard.html', context)
    else:
        return redirect('h-login')

def head_logout(request):
    try:
        del request.session['headmaster_eid']
    except KeyError:
        pass
    return redirect('home')

def teacherverification(request):
    s_eiin = headmasterSession(request)
    check_ein = s_eiin.sch_eiin
    tv = teacher_verify.objects.filter(sch_eiin=check_ein)
    return render(request, 'headmaster/teacher_verification.html', {'tv': tv})


def teacher_reject(request, t_empid):
    teacher_verify.objects.filter(t_empid=t_empid).delete()
    return teacherverification(request)


def teacher_approve(request, t_empid):
    ch = teacher_verify.objects.get(t_empid=t_empid)
    teach_account_create = teacher_account(
        t_fullname=ch.t_fullname, 
        t_email=ch.t_email, 
        t_empid=ch.t_empid,
        dp=ch.dp,
        t_pass=ch.t_pass, 
        t_phone=ch.t_phone,
        gender=ch.gender,
        sch_eiin=ch.sch_eiin
    )
    teach_account_create.save()
    tt = teacher_account.objects.filter(sch_eiin=ch.sch_eiin).count()
    schoolInfo.objects.filter(
        SchoolEIIN=ch.sch_eiin).update(totalTeacher=tt)
    teacher_verify.objects.filter(t_empid=t_empid).delete()
    return teacherverification(request)


def allteachers(request):
    he = headmasterSession(request)
    t_list = teacher_account.objects.filter(sch_eiin=he.sch_eiin)
    return render(request, 'headmaster/allteacher.html', {'teacher': t_list})


def assign_teacherr(request):
    form = assign_teacher_form()
    he = headmasterSession(request)
    obj = assign_teacher.objects.filter(sch_eiin=he.sch_eiin)
    context = {'form': form, 'teacher': obj}
    """ form.fields["t_empid"] = models.forms.ModelMultipleChoiceField(
        queryset=teacher_account.objects.filter(sch_eiin=request.session.get('headmaster_eid'))) """
    if request.method == 'POST':
        form = assign_teacher_form(request.POST)
        if form.is_valid():
            """ form.initial['sch_eiin'] = request.session.get(
                'headmaster_eid') """
            is_assigned = assign_teacher.objects.filter(classes=form.data['classes'])
            if is_assigned:
                context.update({'hasAssigned':True})
                return render(request, 'headmaster/assign_teacher.html', context)
            else:
                context.update({'hasAssigned':False})
                eiin = headmaster_account.objects.get(h_empid=request.session.get('headmaster_eid'))           
                assign_teacher.objects.create(**form.cleaned_data,sch_eiin=eiin.sch_eiin)
        else:
            print(form.errors)       
    return render(request, 'headmaster/assign_teacher.html', context)


def change_tname(request):
    ids = request.GET.get('ids')
    obj = teacher_account.objects.get(t_empid=ids)
    context = {'tname': obj}
    return render(request, 'headmaster/assign_teacher.html', context)


def delete_teacher(request, id):
    assign_teacher.objects.filter(id=id).delete()
    he = headmasterSession(request)
    obj = assign_teacher.objects.filter(sch_eiin=he.sch_eiin)
    context = {'teacher': obj}
    return assign_teacherr(request)
    return render(request, 'headmaster/assign_teacher.html', context)

def account_details(request):
    obj = headmasterSession(request)
    context = {'headmaster': obj}
    return render(request, 'headmaster/account.html', context)

def profileUpdate(request):
    hobj = headmasterSession(request)
    form = profileUpForm(instance=hobj)
    context = {'profileUpForm': form }
    if request.method == 'POST':
        form = profileUpForm(request.POST, request.FILES, instance=hobj)
        if form.is_valid():
            form.save()
            context.update({
                'profileUpForm': '',
                'message': 'Profile Updated!',
                'headmaster': hobj
            })
            # return redirect('account_details')                        
    # else:
    return render(request, 'headmaster/account.html', context)
