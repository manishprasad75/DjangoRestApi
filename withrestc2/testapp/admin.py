from django.contrib import admin
from testapp.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'eno', 'ename', 'esal', 'eaddr']
    list_filter = ['eaddr']

admin.site.register(Employee, EmployeeAdmin)
