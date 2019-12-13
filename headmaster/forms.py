from django import forms
from .models import assign_teacher
from initapp.models import teacher_account
#from django.contrib.sessions.backends.db import SessionStore


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
