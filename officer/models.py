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
