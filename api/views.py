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

class GetSingStudentApiView(APIView):
    def get(self,request,student_id):
        try:
            student = Student.objects.get(id=student_id)
        except Exception:
            return Response({'message': "Student not fount", "status":False}, status=status.HTTP_404_NOT_FOUND)
        serializer = StudentSerializers(student)
        data = {
            "message": "Student fetched successfully",
            "status":True,
            "data":serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

        
class GetSingCourseApiView(APIView):
    def get(self,request,pk):
        try:
            course = Course.objects.get(id=pk)
        except Exception:
            return Response({'message': "Course not fount", "status":False}, status=status.HTTP_404_NOT_FOUND)
        serializer = CourseSerializers(course)
        data = {
            "message": "Course fetched successfully",
            "status":True,
            "data":serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    
class GetSingTeacherApiView(APIView):
    def get(self,request,pk):
        try:
            teacher = Teacher.objects.get(id=pk)
        except Exception:
            return Response({'message': "Teacher not fount", "status":False}, status=status.HTTP_404_NOT_FOUND)
        serializer = TeacherSerialuzers(teacher)
        data = {
            "message": "Teacher fetched successfully",
            "status":True,
            "data":serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)
    

        