from django.db import models
import datetime


class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Manager(models.Model):
    mangername = models.CharField(max_length=50)
    departmentid = models.ForeignKey('Department', blank=True, default='', on_delete=models.CASCADE)

    def __str__(self):
        return self.mangername


class Department(models.Model):
    departmentname = models.CharField(max_length=70)
    managerid = models.OneToOneField(Manager, default='', on_delete=models.CASCADE,)

    def __str__(self):
        return self.departmentname


class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    password = models.CharField(max_length=50)
    #empcode = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    email = models.CharField(max_length=30)
    manager = models.ForeignKey(Manager,  on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    date_of_joining = models.DateField(("Date"), default=datetime.date.today)