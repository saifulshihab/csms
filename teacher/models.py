from django.db import models
from django.utils import timezone
from PIL import Image

class teacher_account(models.Model):
    t_fullname = models.CharField(max_length=100, blank=False, null=False)
    t_email = models.CharField(max_length=100, blank=False, null=False)
    dp = models.ImageField(default='default.jpg', upload_to='teacher')
    t_empid = models.CharField(max_length=100, primary_key=True)
    t_pass = models.CharField(max_length=50, blank=False, null=False)
    gender_select = [
                ('Male', 'Male'),
                ('Female', 'Female')                
            ]
    gender = models.CharField(max_length=10, blank=False, choices=gender_select)
    t_phone = models.CharField(max_length=11, blank=False, null=False)
    sch_eiin = models.CharField(
        max_length=25, blank=False, null=False, default=None)

    def __str__(self):
        return self.t_empid

    def save(self, *args, **kwargs):

        super(teacher_account, self).save(*args, **kwargs)
        img = Image.open(self.dp.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.dp.path)

class student_attendance(models.Model):
    clss = models.CharField(max_length=5)
    todays_attendance = models.IntegerField()
    eiin = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)

class teacher_verify(models.Model):
    t_fullname = models.CharField(max_length=100, blank=False, null=False)
    t_email = models.CharField(max_length=100, blank=False, null=False)
    t_empid = models.CharField(max_length=100, primary_key=True)
    dp = models.ImageField(default='default.jpg', upload_to='teacher')
    t_pass = models.CharField(max_length=11, blank=False, null=False)
    gender_select = [
        ('Male', 'Male'),
        ('Female', 'Female')                    
    ]
    gender = models.CharField(max_length=10, blank=False, choices=gender_select)
    t_phone = models.CharField(max_length=50, blank=False, null=False)
    sch_eiin = models.CharField(
        max_length=25, blank=False, null=False, default=None)

    def __str__(self):
        return self.t_fullname

    def save(self, *args, **kwargs):

        super(teacher_verify, self).save(*args, **kwargs)
        img = Image.open(self.dp.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.dp.path)

    def approve_teacher(self):
        return f"./teacher_approve/{self.t_empid}/"

    def reject_teacher(self):
        return f"./teacher_reject/{self.t_empid}/"

class scholl_result(models.Model):
    year_select = [
        ('2019','2019'),
        ('2020','2020'),
        ('2021','2021'),
        ('2022','2022'),
        ('2023','2023'),
        ('2024','2024')
    ]
    exam_type_select = [
        ('Half yearly exam', 'Half yearly exam'),
        ('Final exam', 'Final exam')
    ]
    sch_class = models.CharField(max_length=50, blank=False, default=6)
    eiin = models.CharField(max_length=100, blank=False)
    year = models.CharField(max_length=100, blank=False, choices=year_select)        
    exam_type = models.CharField(max_length=100, blank=False, choices=exam_type_select)    
    total_pass = models.IntegerField()