from django.db import models

# Create your models here.
class classInfo(models.Model):
    classSelect = [
        ('Class One', 'Class One'),
        ('Class Two', 'Class Two'),
        ('Class Three', 'Class Three'),
        ('Class Four', 'Class Four'),
        ('Class Five', 'Class Five'),
        ('Class Six', 'Class Six'),
        ('Class Seven', 'Class Seven'),
        ('Class Eight', 'Class Eight'),
        ('Class Nine', 'Class Nine'),
        ('Class Ten', 'Class Ten')
    ]
    classId = models.IntegerField(blank=False, null=False)
    classNumber = models.CharField(
        max_length=300, blank=False, null=False, choices=classSelect)
    def __str__(self):
        return self.classNumber

