from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=102)
    last_name = models.CharField(max_length=102)
    age = models.IntegerField()

class Course(models.Model):
    name = models.CharField(max_length=200)
    course_price = models.DecimalField(max_digits=5, decimal_places=2)
    course_Topics = models.TextField(null=True, blank=True)

class Teacher(models.Model):
    first_name = models.CharField(max_length=102)
    last_name = models.CharField(max_length=102)
    experience = models.IntegerField()

    
class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(null=True, blank=True)