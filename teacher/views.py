from django.shortcuts import render, redirect
from initapp.models import student_account, teacher_account
from school.models import schoolInfo
from .forms import addstudentform
from django.contrib import messages
from headmaster.models import assign_teacher

# Create your views here.


def dashboard(request):
    if request.session.has_key('teacher_eid'):
        tb = teacher_account.objects.get(
            t_empid=request.session.get('teacher_eid'))  # get teacher empid from session
        obj = schoolInfo.objects.get(SchoolEIIN=tb.sch_eiin)
        context = {'school': obj}
        return render(request, 'teacher/dashboard.html', context)
    else:
        return redirect('userlogin')


def classes(request):
    if request.session.has_key('teacher_eid'):
        getclass = assign_teacher.objects.filter(
            t_empid=request.session.get('teacher_eid'))
        return render(request, 'teacher/classes.html', {'clas': getclass})
    else:
        return redirect('userlogin')


def teach_logout(request):
    try:
        del request.session['teacher_eid']
    except KeyError:
        pass
    return redirect('home')

def allstudent(request):
    teacherSession = request.session.get('teacher_eid')
    print(teacherSession)
    tea_obj = teacher_account.objects.get(t_empid=teacherSession)
    sc_eiin = str(tea_obj.sch_eiin)
    sa = student_account.objects.filter(SchoolEIIN=sc_eiin)
    return render(request, 'teacher/add_student.html', {'sa': sa})


def enterClass(request, classno):
    teacherSession = request.session.get('teacher_eid')
    # print(teacherSession)
    cls = classno
    # print(cls)
    if (cls == '6'):
        stuClass = 'Six'
    elif (cls == '7'):
        stuClass = 'Seven'
    elif (cls == '8'):
        stuClass = 'Eight'
    elif (cls == '9'):
        stuClass = 'Nine'
    elif (cls == '10'):
        stuClass = 'Ten'
    # print(stuClass)
    tea_obj = teacher_account.objects.get(t_empid=teacherSession)
    sc_eiin = str(tea_obj.sch_eiin)
    sad = student_account.objects.filter(SchoolEIIN=sc_eiin, s_class=classno)
    schobj = schoolInfo.objects.get(SchoolEIIN=sc_eiin)

    sch_name = schobj.schoolName
    # print(sch_name)
    if request.method == 'POST':
        stuRoll = request.POST['roll']
        stuPass = request.POST['password']
        check_multiple = student_account.objects.filter(s_roll=stuRoll, s_pass=stuPass, s_class=stuClass,
                                                        s_school=sch_name,
                                                        SchoolEIIN=sc_eiin)
        if check_multiple:
            messages.success(request, 'This student registered already.')
            sa = student_account.objects.filter(
                SchoolEIIN=sc_eiin, s_class=stuClass)

            return render(request, 'teacher/enter_class.html', {'sa': sa})
        else:

            student_account_create = student_account(s_roll=stuRoll, s_pass=stuPass, s_class=stuClass,
                                                     s_school=sch_name,
                                                     SchoolEIIN=sc_eiin)
            student_account_create.save()
            sa = student_account.objects.filter(
                SchoolEIIN=sc_eiin, s_class=stuClass)

            return render(request, 'teacher/enter_class.html', {'sa': sa})
    else:
        teacherSession = request.session.get('teacher_eid')
        print(teacherSession)
        tea_obj = teacher_account.objects.get(t_empid=teacherSession)
        sc_eiin = str(tea_obj.sch_eiin)
        sa = student_account.objects.filter(
            SchoolEIIN=sc_eiin, s_class=stuClass)
        context = {'sad': sad, 'classno': classno, 'sa': sa}
        return render(request, 'teacher/enter_class.html', context)

    #context = {'sad': sad, 'classno': classno}
    # return render(request, 'teacher/enter_class.html', context)

   # return render(request, 'teacher/enter_class.html', {'sa': sa})
