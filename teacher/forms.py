from django import forms
from initapp.models import student_account


class addstudentform(forms.ModelForm):
    roll = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Student Roll'}))

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = student_account
        fields = ['roll', 's_class', 'password']
