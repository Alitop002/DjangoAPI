from rest_framework.views import APIView
from rest_framework.response import Response
from django.template.context_processors import request
from rest_framework import status
from .models import Student, Course, Teacher
from .serializers import TeacherSerialuzers, CourseSerializers, StudentSerializers

class GetStudentApiView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializers(students, many=True)

        data = {
            "message": "Students were successfully found",
            "status": True,
            "data":serializer.data
        }
        return Response(data,status=status.HTTP_200_OK)

class GetCoursesApiView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializers(courses, many=True)
        
        data = {
            "message": "Courses were successfully found",
            "status": True,
            "data":serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
class GetTeacherApiView(APIView):
    def get(self, request):
        teachers = Teacher.objects.all()
        serializer = TeacherSerialuzers(teachers, many=True)
        
        data = {
            "message": "Teachers were successfully found",
            "status": True,
            "data":serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

# class GetProductApiView(APIView):
#     def get(self, request):
#         product = Product.objects.all()
#         serializer = ProductSerializer(product, many=True)
#         serializer.is_valid(raise_exception=True)

#         data = {
#             "message": "Products fetched successfully",
#             "status":True,
#             "data": serializer.data
#         }

#         return Response(data,status=status.HTTP_200_OK)
    
        