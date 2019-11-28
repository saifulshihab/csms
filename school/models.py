from django.db import models
from django import forms
# Create your models here.


class schoolInfo(models.Model):
    school_select = [
        ('Government Laboratory High School', 'Government Laboratory High School'),
        ('Viqarunnisa Noon School', 'Viqarunnisa Noon School'),
        ('Rifles Public School and College', 'Rifles Public School and College'),
        ('Dhaka Residential Model School and College',
         'Dhaka Residential Model School and College'),
        ('Rajuk Uttara Model School & College',
         'Rajuk Uttara Model School & College'),
        ('Dhanmondi Government Boys’ High School',
         'Dhanmondi Government Boys’ High School'),
        ('Saint Joseph Higher Secondary School',
         'Saint Joseph Higher Secondary School'),
        ('St. Gregory’s High School', 'St. Gregory’s High School'),
        ('Motijheel Government Boys High school',
         'Motijheel Government Boys High school'),
        ('Mirpur Govt. High School', 'Mirpur Govt. High School'),
        ('Django', 'Django')
    ]
    SchoolEIIN = models.CharField(
        primary_key=True, max_length=25, blank=False, null=False)
    schoolName = models.CharField(
        max_length=300, blank=False, null=False, choices=school_select)
    schoolAddress = models.CharField(max_length=100, blank=False, null=False)
    totalStudent = models.IntegerField(blank=False, null=False)
    totalTeacher = models.IntegerField(blank=False, null=False)
    attendance_percentage = models.IntegerField(
        blank=False, null=False, default=1)
    pass_percentage = models.IntegerField(blank=False, null=False, default=1)

    def __str__(self):
        return self.SchoolEIIN

    def get_absolute_url(self):
        return f"/school_detail/{self.SchoolEIIN}/"
