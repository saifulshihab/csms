from django.db import models
from django.utils import timezone

class student_account(models.Model):    
    s_roll = models.CharField(max_length=50, blank=False, null=False)
    s_pass = models.CharField(max_length=50, blank=False, null=False)
    s_class = models.CharField(
        max_length=10, blank=False, null=False)
    s_school = models.CharField(max_length=200, blank=False, null=False)
    SchoolEIIN = models.CharField(
        max_length=25, blank=False, null=False, default=None)

    def __str__(self):
        return self.s_school
        
class student_feedback(models.Model):
    select_school = [
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
        ('Sholla High School',
         'Sholla High School'),
        ('St. Gregory’s High School', 'St. Gregory’s High School'),
        ('Motijheel Government Boys High school',
         'Motijheel Government Boys High school'),
        ('Mirpur Govt. High School', 'Mirpur Govt. High School'),
        ('Django', 'Django')
    ]
    feedback = models.TextField(blank=False)
    school = models.CharField(max_length=300, blank=False, choices=select_school)
    posted_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.school
