from django.db import models

# Create your models here.


class teacher(models.Model):
    tname = models.CharField(max_length=100)
    temail = models.CharField(max_length=254)
    tpass = models.CharField(max_length=50)
