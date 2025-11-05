from rest_framework import serializers
from api.models import Course, Instructor

class CourseSerializers(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
        

class InstructorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = "__all__"
        