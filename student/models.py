from django.db import models

# Create your models here.
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
        ('St. Gregory’s High School', 'St. Gregory’s High School'),
        ('Motijheel Government Boys High school',
         'Motijheel Government Boys High school'),
        ('Mirpur Govt. High School', 'Mirpur Govt. High School'),
        ('Django', 'Django')
    ]
    feedback = models.TextField(blank=False)
    school = models.CharField(max_length=300, blank=False, choices=select_school)

    def __str__(self):
        return self.school