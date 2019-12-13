from django.db import models

# Create your models here.


class officer_account(models.Model):
    oname = models.CharField(max_length=100)
    oemail = models.CharField(max_length=100)
    oempid = models.CharField(max_length=50)
    opass = models.CharField(max_length=50)
    oworkp = models.CharField(max_length=50)

    def __str__(self):
        return self.oempid

class coordiinator(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name

class assign_cordinator(models.Model):
    name = models.CharField(max_length=50, blank=False)
    phone = models.CharField(max_length=11)
    sch_eiin = models.CharField(max_length=20)
    