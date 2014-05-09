from django.db import models

class Package(models.Model):
    package_id = models.CharField(max_length=50)
    address = models.CharField(max_length=100)


class Employee(models.Model):
    emp_name = models.CharField(max_length=30)
    emp_id = models.CharField(max_length=50)
