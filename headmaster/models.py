from django.db import models
from initapp.models import teacher_account
# Create your models here.


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

