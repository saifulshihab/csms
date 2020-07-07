from django.shortcuts import render, redirect
from school.models import schoolInfo
from headmaster.models import assign_teacher
from .models import teacher_account, student_attendance, scholl_result, teacher_verify
from student.models import student_account 
from .forms import student_registration_Form, attendanceForm, publishResultForm, teacherRegForm, teacherLoginForm, profileUpForm

def login(request):
    if request.session.has_key('teacher_eid'):
        return redirect('../teacher')
    else:
        context = {'loginForm': teacherLoginForm()}
        if request.method == 'POST':        
            form = teacherLoginForm(request.POST)
            check_pending_registration = teacher_verify.objects.filter(t_empid=form.data['t_empid'], t_pass=form.data['t_pass'])    
            loggedin = teacher_account.objects.filter(t_empid=form.data['t_empid'], t_pass=form.data['t_pass'])    
            if loggedin:
                request.session['teacher_eid'] = form.data['t_empid']
                return redirect('../teacher')
            elif check_pending_registration:
                context.update({'message': 'Your account is under review! Check back later.. .'})        
            else:
                context.update({'message': 'Invalid credential!'})        
        return render(request, 'teacher/login.html', context)

def teacherSession(request):
    return teacher_account.objects.get(
        t_empid=request.session.get('teacher_eid'))

def signup(request):
    form = teacherRegForm()
    context = {
        'regForm': form,
        'msgtype': 'failed',
        'message': ''
    }
    if request.method == 'POST':
        form = teacherRegForm(request.POST, request.FILES)        
        if form.is_valid():
            sch_exist = schoolInfo.objects.filter(SchoolEIIN=form.data['sch_eiin'])
            if sch_exist:                               
                empidtaken = teacher_verify.objects.filter(t_empid=form.data['t_empid'])
                empidtaken2 = teacher_account.objects.filter(t_empid=form.data['t_empid'])
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
    return render(request, 'teacher/signup.html', context)

def dashboard(request):
    if request.session.has_key('teacher_eid'):
        tb = teacher_account.objects.get(
            t_empid=request.session.get('teacher_eid'))  # get teacher empid from session
        obj = schoolInfo.objects.get(SchoolEIIN=tb.sch_eiin)
        total_student = student_account.objects.filter(
            SchoolEIIN=tb.sch_eiin).count()
        total_teacher = teacher_account.objects.filter(
            sch_eiin=tb.sch_eiin).count()
        total_male_t = teacher_account.objects.filter(
            sch_eiin=tb.sch_eiin, gender='Male').count()
        total_female_t = teacher_account.objects.filter(
            sch_eiin=tb.sch_eiin, gender='Female').count()        
        context = {'school': obj,
         'total_student': total_student,         
        'total_teacher': total_teacher,
        'total_female_t': total_female_t,
        'total_male_t': total_male_t
        }
        return render(request, 'teacher/dashboard.html', context)
    else:
        return redirect('userlogin')


def classes(request):
    if request.session.has_key('teacher_eid'):        
        getclass = assign_teacher.objects.filter(
            t_empid=request.session.get('teacher_eid'))        
        context = {'clas': getclass}
        return render(request, 'teacher/classes.html', context)
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
    if request.session.has_key('teacher_eid'):        
        teacherSession = request.session.get('teacher_eid')
        cls = classno            
        tea_obj = teacher_account.objects.get(t_empid=teacherSession)
        sc_eiin = str(tea_obj.sch_eiin)
        schobj = schoolInfo.objects.get(SchoolEIIN=sc_eiin)
        sch_name = schobj.schoolName                
        student_list = student_account.objects.filter(SchoolEIIN=sc_eiin, s_class=cls)            
        total_student = student_list.count()
        attendance_by_date = student_attendance.objects.filter(eiin=sc_eiin, clss=cls).order_by('-id')
        resultData = scholl_result.objects.filter(eiin=sc_eiin, sch_class=cls)
        context = {            
            'classno': classno, 
            'student_list': student_list, 
            'total_nof_student': total_student, 
            'attendance_form': attendanceForm(),
            'attendance_by_date': attendance_by_date,
            'ResultForm': publishResultForm(),
            'result_data': resultData,
            'studentRegistrationForm': student_registration_Form(),
            'msg_type': 'failed'
        }   
        if request.method == 'POST':    
            attendance_form = attendanceForm(request.POST)
            result_form = publishResultForm(request.POST)
            studentRegistrationForm = student_registration_Form(request.POST)
        #Add student section start                        
            if studentRegistrationForm.is_valid():                
                is_multiple = student_account.objects.filter(s_roll=studentRegistrationForm.data['s_roll'], s_class=cls,s_school=sch_name,SchoolEIIN=sc_eiin)
                if is_multiple:
                    context.update({
                        'att_msg': 'Failed! This student is registered already!'               
                    })
                    return render(request, 'teacher/enter_class.html', context)
                else:
                    context.update({
                        'att_msg': 'Success! New student registered.',
                        'msg_type': 'success'               
                    })                
                    student_account.objects.create(s_class=cls,s_school=sch_name,SchoolEIIN=sc_eiin, **studentRegistrationForm.cleaned_data)
                    school_total_student = student_account.objects.filter(SchoolEIIN=sc_eiin).count()                                       
                    schoolInfo.objects.filter(SchoolEIIN=sc_eiin).update(totalStudent=school_total_student)   
                    return render(request, 'teacher/enter_class.html', context)
            # Attendance section start
            if attendance_form.is_valid():
                has_attendance = student_attendance.objects.filter(date=attendance_form.data['date'], clss=cls)                
                if int(attendance_form.data['todays_attendance']) > total_student:
                        context.update({                            
                            'att_msg': "Failed! Presence can't be greater then total student!"                 
                        })                                           
                        return render(request, 'teacher/enter_class.html', context)
                elif has_attendance:                
                    count_attendance_percent(request, sc_eiin)
                    student_attendance.objects.filter(date=attendance_form.data['date'], clss=cls).update(**attendance_form.cleaned_data)
                else:       
                    count_attendance_percent(request, sc_eiin)          
                    student_attendance.objects.create(**attendance_form.cleaned_data, clss=cls, eiin=sc_eiin)                                              
                context.update({                    
                    'att_msg': 'Success! Attendance Update.',
                    'msg_type': 'success'
                })
                return render(request, 'teacher/enter_class.html', context)
            #Result upload section start
            if result_form.is_valid():
                has_result = scholl_result.objects.filter(sch_class=cls, year=result_form.data['year'], exam_type=result_form.data['exam_type'])
                
                if int(result_form.data['total_pass']) > total_student:
                    context.update({                       
                        'att_msg': 'Failed! Total pass can not be greater then total student!'                              
                    })
                    return render(request, 'teacher/enter_class.html', context)
                else:
                    if has_result:
                        scholl_result.objects.filter(year=result_form.data['year'], exam_type=result_form.data['exam_type']).update(**result_form.cleaned_data)
                        exam_result(request)
                    else:
                        scholl_result.objects.create(eiin=sc_eiin, sch_class=cls, **result_form.cleaned_data)                                      
                        return exam_result(request)
                        context.update({                    
                            'att_msg': 'Success! Result Submitted.',
                            'msg_type': 'success'
                            })
                return render(request, 'teacher/enter_class.html', context)            
        else:                          
            return render(request, 'teacher/enter_class.html', context)
    else:
        return redirect('userlogin')      

def taccount_details(request):
    obj = teacherSession(request)
    context = {'teacher': obj}
    return render(request, 'teacher/account.html', context)

def profileUpdate(request):
    tobj = teacherSession(request)
    form = profileUpForm(instance=tobj)
    context = {'profileUpForm': form }
    if request.method == 'POST':
        form = profileUpForm(request.POST, request.FILES, instance=tobj)
        if form.is_valid():
            form.save()
            """ context.update({
                'profileUpForm': '',
                'message': 'Profile Updated!',
                'teacher': tobj
            }) """
            return redirect('taccount_details')                        
    else:
        return render(request, 'teacher/account.html', context)

def count_attendance_percent(request, sch_eiin):    
    total_std = schoolInfo.objects.get(SchoolEIIN=sch_eiin).totalStudent
    get_attendance_days = student_attendance.objects.filter(eiin=sch_eiin).order_by('-id')[:7].count()    
    if get_attendance_days > 6:      
        get_attendance_presence = student_attendance.objects.filter(eiin=sch_eiin).order_by('-id')[:7]
        sum = 0
        for a in get_attendance_presence:
            sum = sum + a.todays_attendance           
        att_per = 100 / ((total_std * get_attendance_days)/sum)
        schoolInfo.objects.filter(SchoolEIIN=sch_eiin).update(attendance_percentage=att_per)      

def exam_result(request):
    pass    

