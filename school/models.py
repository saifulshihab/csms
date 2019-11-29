from django.db import models
# Create your models here.


class schoolInfo(models.Model):

    SchoolEIIN = models.CharField(
        primary_key=True, max_length=25, blank=False, null=False)
    schoolName = models.CharField(
        max_length=300, blank=False, null=False)
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
