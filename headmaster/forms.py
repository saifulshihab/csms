from django import forms
from .models import headmaster_verify, headmaster_account, assign_teacher
from teacher.models import teacher_account
#from django.contrib.sessions.backends.db import SessionStore

class headmasterRegForm(forms.ModelForm):
    h_email = forms.CharField(widget=forms.EmailInput())
    h_pass = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = headmaster_verify
        fields = [
            'sch_eiin',
            'h_fullname',
            'h_email',
            'dp',
            'h_empid',
            'h_pass',
            'h_phone'
        ]

class headmasterLoginForm(forms.ModelForm):
    h_pass = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = headmaster_account
        fields = [
            'h_empid',
            'h_pass'
        ]

class assign_teacher_form(forms.ModelForm):
    class Meta:
        model = assign_teacher
        fields = ['classes', 't_empid']

    """ def __init__(self, *args, **kwargs):
       
        super(assign_teacher_form, self).__init__(*args, **kwargs)
        self.fields['t_empid'].queryset = teacher_account.objects.filter(
            sch_eiin=2356) """

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['t_empid'].widget.attrs.update({
    #         'class': '',
    #         'id': 't_empid'
    #     })
    #     self.fields['t_name'].widget.attrs.update({
    #         'class': '',
    #         'id': 't_name'
    #     })
    #     self.fields['sch_eiin'].widget.attrs.update({
    #         'class': '',
    #         'id': 'sch_eiin'
    #     })

class profileUpForm(forms.ModelForm):
    class Meta:
        model = headmaster_account
        fields = [
            'h_fullname',
            'h_email',
            'dp',
            'h_pass',
            'h_phone'
        ]