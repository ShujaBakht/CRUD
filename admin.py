from django.contrib import admin

# Register your models here.
from . models import *


@admin.register(Employees)
class employeesadmin(admin.ModelAdmin):
    list_display= ['name' , 'email', 'address', 'phone' ]