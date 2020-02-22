from django.db import models
import datetime


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Department(models.Model):
    departmentname = models.CharField(max_length=70)
    #manager = models.ForeignKey(Manager, default='', on_delete=models.CASCADE,)

    def __str__(self):
        return self.departmentname #, self.manager


class Manager(models.Model):
    mangername = models.CharField(max_length=50)
    department = models.ForeignKey(Department, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.mangername, self.department


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    password = models.CharField(max_length=50, default='Welcome@1234')
    empcode = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=30, default='')
    manager = models.ForeignKey(Manager,  default='', on_delete=models.CASCADE)
    department = models.ForeignKey(Department, default='', on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    date_of_joining = models.DateField(("Date"), default=datetime.date.today)