from django.shortcuts import render, redirect
from .models import teacher
from initapp.models import student_account,teacher_account
from school.models import schoolInfo
from .forms import addstudentform


# Create your views here.


def dashboard(request):
    if request.session.has_key('teacher_eid'):
        return render(request, 'teacher/dashboard.html')
    else:
        return redirect('userlogin')


def teach_logout(request):
    try:
        del request.session['teacher_eid']
    except KeyError:
        pass
    return redirect('home')


def addstudent(request):
    if request.method == 'POST':
        teacherSession = request.session.get('teacher_eid')
        print(teacherSession)
        tea_obj = teacher_account.objects.get(t_empid=teacherSession)
        sc_eiin = str(tea_obj.sch_eiin)
        print(sc_eiin)
        schobj = schoolInfo.objects.get(SchoolEIIN=sc_eiin)
        sch_name = schobj.schoolName
        print(sch_name)
        stuRoll = request.POST['roll']
        stuClass = request.POST['class']
        stuPass = request.POST['password']
        student_account_create = student_account(s_roll=stuRoll, s_pass=stuPass, s_class=stuClass, s_school=sch_name,
                                                 SchoolEIIN=sc_eiin)
        student_account_create.save()
        sa = student_account.objects.filter(SchoolEIIN=sc_eiin)

        return render(request, 'teacher/add_student.html', {'sa': sa})
    else:
        teacherSession = request.session.get('teacher_eid')
        print(teacherSession)
        tea_obj = teacher_account.objects.get(t_empid=teacherSession)
        sc_eiin = str(tea_obj.sch_eiin)
        sa = student_account.objects.filter(SchoolEIIN=sc_eiin)
        return render(request, 'teacher/add_student.html', {'sa': sa})




def addstu(request):
   pass



def allstudent(request):
    teacherSession = request.session.get('teacher_eid')
    print(teacherSession)
    tea_obj = teacher_account.objects.get(t_empid=teacherSession)
    sc_eiin = str(tea_obj.sch_eiin)
    sa = student_account.objects.filter(SchoolEIIN=sc_eiin)
    return render(request, 'teacher/add_student.html', {'sa': sa})








