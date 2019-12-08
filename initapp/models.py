from django.db import models
from school.models import schoolInfo


# Create your models here.


class headmaster_account(models.Model):
    h_fullname = models.CharField(max_length=100, blank=False, null=False)
    h_email = models.CharField(max_length=100, blank=False, null=False)
    h_empid = models.CharField(max_length=100, primary_key=True)
    h_pass = models.CharField(max_length=50, blank=False, null=False)
    h_phone = models.CharField(max_length=50, blank=False, null=False)
    sch_eiin = models.CharField(max_length=25, blank=False, null=False, default=None)

    def __str__(self):
        return self.h_fullname


class headmaster_verify(models.Model):
    h_fullname = models.CharField(max_length=100, blank=False, null=False)
    h_email = models.CharField(max_length=100, blank=False, null=False)
    h_empid = models.CharField(max_length=100, primary_key=True)
    h_pass = models.CharField(max_length=50, blank=False, null=False)
    h_phone = models.CharField(max_length=50, blank=False, null=False)
    sch_eiin = models.CharField(max_length=25, blank=False, null=False, default=None)

    def __str__(self):
        return self.h_empid

    def approve_head(self):
        return f"/head_approve/{self.h_empid}/"

    def get_absolute_url(self):
        return f"/reject_head/{self.h_empid}/"


class teacher_account(models.Model):
    t_fullname = models.CharField(max_length=100, blank=False, null=False)
    t_email = models.CharField(max_length=100, blank=False, null=False)
    t_empid = models.CharField(max_length=100, primary_key=True)
    t_pass = models.CharField(max_length=50, blank=False, null=False)
    t_phone = models.CharField(max_length=50, blank=False, null=False)
    sch_eiin = models.CharField(max_length=25, blank=False, null=False, default=None)

    def __str__(self):
        return self.t_fullname


class student_account(models.Model):
    school_class = [
        ('One', 'One'),
        ('Two', 'Two'),
        ('Three', 'Three'),
        ('Four', 'Four'),
        ('Five', 'Five'),
        ('Six', 'Six'),
        ('Seven', 'Seven'),
        ('Eight', 'Eight'),
        ('Nine', 'Nine'),
        ('Ten', 'Ten')

    ]
    s_roll = models.CharField(max_length=50, blank=False, null=False)
    s_pass = models.CharField(max_length=50, blank=False, null=False)
    s_class = models.CharField(max_length=10, blank=False, null=False, choices=school_class)
    s_school = models.CharField(max_length=200, blank=False, null=False)
    SchoolEIIN = models.CharField(max_length=25, blank=False, null=False, default=None)

    def __str__(self):
        return self.s_school


class teacher_verify(models.Model):
    t_fullname = models.CharField(max_length=100, blank=False, null=False)
    t_email = models.CharField(max_length=100, blank=False, null=False)
    t_empid = models.CharField(max_length=100, primary_key=True)
    t_pass = models.CharField(max_length=50, blank=False, null=False)
    t_phone = models.CharField(max_length=50, blank=False, null=False)
    sch_eiin = models.CharField(max_length=25, blank=False, null=False, default=None)

    def __str__(self):
        return self.t_fullname

    def approve_teacher(self):
        return f"./teacher_approve/{self.t_empid}/"

    def reject_teacher(self):
        return f"./teacher_reject/{self.t_empid}/"
