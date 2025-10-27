from django.contrib import admin
from .models import Course, Teacher, Student

admin.site.register([Course, Teacher, Student])

