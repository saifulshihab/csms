from django.db import models
from school.models import schoolInfo
from classInformation.models import classInfo
from officer.models import officer_account

# Create your models here.


class headmaster_account(models.Model):
    h_fullname = models.CharField(max_length=100, blank=False, null=False)
    h_email = models.CharField(max_length=100, blank=False, null=False)
    h_empid = models.CharField(max_length=100, primary_key=True)
    h_pass = models.CharField(max_length=50, blank=False, null=False)
    h_School = models.ForeignKey(schoolInfo, on_delete=models.CASCADE)
    h_phone = models.CharField(max_length=50, blank=False, null=False)
    offcr= models.ForeignKey(officer_account, on_delete=models.CASCADE)

    def __str__(self):
        return self.h_empid


class teacher_account(models.Model):
    t_fullname = models.CharField(max_length=100, blank=False, null=False)
    t_email = models.CharField(max_length=100, blank=False, null=False)
    t_empid = models.CharField(max_length=100, primary_key=True)
    t_pass = models.CharField(max_length=50, blank=False, null=False)
    teacherSchool = models.ForeignKey(schoolInfo, on_delete=models.CASCADE)
    t_phone = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.t_empid


class student_account(models.Model):
    s_roll = models.CharField(max_length=50, blank=False, null=False)
    s_pass = models.CharField(max_length=50, blank=False, null=False)
    StuSchool = models.ForeignKey(schoolInfo, on_delete=models.CASCADE)
    Cls=models.ForeignKey(classInfo, on_delete=models.CASCADE)

    def __str__(self):
        return self.s_roll
