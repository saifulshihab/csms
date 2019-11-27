from django.db import models

# Create your models here.
class schoolInfo(models.Model):
    schoolId = models.IntegerField(blank=False, null=False)
    schoolName = models.CharField(max_length=100, blank=False, null=False)
    schoolAddress = models.CharField(max_length=100, blank=False, null=False)
    SchoolEIIN = models.CharField(max_length=25, blank=False, null=False)
    totalStudent = models.IntegerField()
    totalTeacher = models.IntegerField()
