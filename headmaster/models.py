from django.db import models
from PIL import Image
from teacher.models import teacher_account

class headmaster_account(models.Model):
    h_fullname = models.CharField(max_length=100, blank=False, null=False)
    h_email = models.CharField(max_length=100, blank=False, null=False)
    h_empid = models.CharField(max_length=100, primary_key=True)
    dp = models.ImageField(default='default.jpg', upload_to='headmaster')
    h_pass = models.CharField(max_length=50, blank=False, null=False)
    h_phone = models.CharField(max_length=11, blank=False, null=False)
    sch_eiin = models.CharField(
        max_length=25, blank=False, null=False, default=None)

    def __str__(self):
        return self.h_fullname
    
    def save(self, *args, **kwargs):

        super(headmaster_account, self).save(*args, **kwargs)
        img = Image.open(self.dp.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.dp.path)

class headmaster_verify(models.Model):
    h_fullname = models.CharField(max_length=100, blank=False, null=False)
    h_email = models.CharField(max_length=100, blank=False, null=False)
    dp = models.ImageField(default='default.jpg', upload_to='headmaster')
    h_empid = models.CharField(max_length=100, primary_key=True)
    h_pass = models.CharField(max_length=50, blank=False, null=False)
    h_phone = models.CharField(max_length=11, blank=False, null=False)
    sch_eiin = models.CharField(
        max_length=25, blank=False, null=False, default=None)

    def __str__(self):
        return self.h_empid

    def save(self, *args, **kwargs):
        super(headmaster_verify, self).save(*args, **kwargs)
        img = Image.open(self.dp.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.dp.path)

    def approve_head(self):
        return f"/head_approve/{self.h_empid}/"

    def get_absolute_url(self):
        return f"/reject_head/{self.h_empid}/"


class assign_teacher(models.Model):
    select_class = [
        ('6', '6'),
        ('7', '7'),
        ('8', '8'),
        ('9', '9'),
        ('10', '10')
    ]
    classes = models.CharField(
        max_length=20, blank=False, choices=select_class)
    t_empid = models.ForeignKey(teacher_account, on_delete=models.CASCADE)
    sch_eiin = models.CharField(max_length=100, blank=False, default=None)

    def __str__(self):
        return self.sch_eiin

    def delete_teacher(self):
        return f"./delete_teacher/{self.id}/"

    def returnClassno(self):
        return f"./enterClass/{self.classes}"
