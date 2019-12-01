from django.contrib import admin
from .models import headmaster_account, student_account, teacher_account, headmaster_verify
# Register your models here.
admin.site.register(headmaster_account)
admin.site.register(student_account)
admin.site.register(teacher_account)
admin.site.register(headmaster_verify)
