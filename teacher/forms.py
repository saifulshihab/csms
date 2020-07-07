from django import forms
from student.models import student_account
from .models import teacher_verify, teacher_account, student_attendance, scholl_result

class teacherRegForm(forms.ModelForm):
    t_email = forms.CharField(widget=forms.EmailInput())
    t_pass = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = teacher_verify
        fields = [
            'sch_eiin',
            't_fullname',
            't_email',
            'dp',
            't_empid',
            't_pass',
            'gender',
            't_phone'
        ]
        
class teacherLoginForm(forms.ModelForm):
    t_pass = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = teacher_account
        fields = [
            't_empid',
            't_pass'
        ]

class student_registration_Form(forms.ModelForm):
    s_roll = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Student Roll'        
    }))
    class Meta:
        model = student_account
        fields = ['s_roll', 's_pass']

class attendanceForm(forms.ModelForm):    
    class Meta: 
        model = student_attendance
        fields = ['todays_attendance', 'date']

class publishResultForm(forms.ModelForm):
    class Meta:
        model = scholl_result
        fields = ['year', 'exam_type', 'total_pass']

class profileUpForm(forms.ModelForm):
    class Meta:
        model = teacher_account
        fields = [
            't_fullname',
            't_email',
            'dp',
            't_pass',
            'gender',
            't_phone'
        ]