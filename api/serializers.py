from rest_framework import serializers


class CourseSerializers(serializers.Serializer):
    name = serializers.CharField(required=True)
    course_price = serializers.DecimalField(max_digits=5, decimal_places=2)
    course_Topics = serializers.CharField()

class StudentSerializers(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    age = serializers.IntegerField()

class TeacherSerialuzers(serializers.Serializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    experience = serializers.IntegerField()

