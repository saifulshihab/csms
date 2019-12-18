from django.contrib import admin
from .models import officer_account, coordiinator, assign_cordinator
# Register your models here.
admin.site.register(officer_account)
admin.site.register(coordiinator)
admin.site.register(assign_cordinator)