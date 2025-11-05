from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from api.models import Course
from api.serializers import CourseSerializers
from api.pagination import CoursePagination

class CourseGetPostApiView(APIView):
    serializer_class = CourseSerializers
    def get(self, request):
        courses = Course.objects.all()
        paginator = CoursePagination()
        paginated_course = paginator.paginate_queryset(courses, request)
        serializer = self.serializer_class(paginated_course, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )


class CourseDetailApiView(APIView):
    serializer_class = CourseSerializers
    def get(self, request, pk):
        course = Course.objects.get(pk=pk)
        if not course:
            return Response({"detail": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(course)
        return Response(serializer.data)
    def put(self, request, pk):
        course = Course.objects.get(pk=pk)
        if not course:
            return Response({"detail": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        course = Course.objects.get(pk=pk)
        if not course:
            return Response({"detail": "Course not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
    