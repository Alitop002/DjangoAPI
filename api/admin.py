from django.contrib import admin
from .models import Course, Teacher, Student,Product
from unfold.admin import ModelAdmin

@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ("name", "course_price", "course_Topics")

admin.site.register(Teacher)
admin.site.register(Product)
admin.site.register(Student)

    


