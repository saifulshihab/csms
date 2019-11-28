from django import forms
from .models import student_feedback


class feedbackForm(forms.ModelForm):
    feedback = forms.CharField(label="Feedback",
                               widget=forms.Textarea(
                                   attrs={
                                       'placeholder': 'Write your feedback here. ..',

                                   }
                               ))
    class Meta:
        model = student_feedback
        fields = ['feedback', 'school']
