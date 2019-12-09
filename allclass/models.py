from django.db import models
from school.models import schoolInfo

# Create your models here.
class classSix(models.Model):
    class_no = models.CharField(primary_key=True, default=6, max_length=10)
    total_student = models.IntegerField()
    attendance = models.IntegerField()
    sch_eiin  = models.ForeignKey(schoolInfo, on_delete=models.CASCADE)