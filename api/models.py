from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

class Instructor(models.Model):
    full_name = models.CharField(max_length=201)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=102)
    specialization = models.CharField(max_length=301)
    joined_date = models.DateField(auto_now_add=True)
