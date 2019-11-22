from django.contrib import admin
from .models import headmaster_account, student_account, teacher_account
# Register your models here.
admin.site.register(headmaster_account)
admin.site.register(student_account)
admin.site.register(teacher_account)
