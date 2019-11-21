from django.db import models

# Create your models here.


class headmaster_account(models.Model):
    h_fullname = models.CharField(max_length=100, blank=False, null=False)
    h_email = models.CharField(max_length=100, blank=False, null=False)
    h_empid = models.CharField(max_length=100, primary_key=True)
    h_pass = models.CharField(max_length=50, blank=False, null=False)
    h_school = models.CharField(max_length=250, blank=False, null=False)
    h_phone = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.h_fullname


class teacher_account(models.Model):
    t_fullname = models.CharField(max_length=100, blank=False, null=False)
    t_email = models.CharField(max_length=100, blank=False, null=False)
    t_empid = models.CharField(max_length=100, primary_key=True)
    t_pass = models.CharField(max_length=50, blank=False, null=False)
    t_school = models.CharField(max_length=250, blank=False, null=False)
    t_phone = models.CharField(max_length=50, blank=False, null=False)

    def __str__(self):
        return self.t_fullname


class student_account(models.Model):
    s_roll = models.CharField(max_length=50, blank=False, null=False)
    s_pass = models.CharField(max_length=50, blank=False, null=False)
    s_class = models.CharField(max_length=10, blank=False, null=False)
    s_school = models.CharField(max_length=200, blank=False, null=False)

    def __str__(self):
        return self.s_school
