from rest_framework.views import APIView
from rest_framework.response import Response
from django.template.context_processors import request
from rest_framework import status
from .models import Student, Course, Teacher, Product
from .serializers import TeacherSerialuzers, CourseSerializers, StudentSerializers, ProductSerializer

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
    
class GetProductApiView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = ProductSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
class GetSingApiView(APIView):
    def get(self,request,pk):
        try:
            product = Product.objects.get(pk=pk)

        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self,request,pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
