from django.contrib import admin

# Register your models here
from Track.models import Package, Employee

admin.site.register(Package)
admin.site.register(Employee)