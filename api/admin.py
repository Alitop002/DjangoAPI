from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Course, Instructor
@admin.register(Course)
class CourseAdmin(ModelAdmin):
    list_display = ("title", "price", "created_at")

admin.site.register(Instructor)