from django.urls import path
from .views import GetStudentApiView,GetCoursesApiView,GetTeacherApiView,GetSingStudentApiView,GetSingCourseApiView,GetSingTeacherApiView

urlpatterns = [
    path('students/', GetStudentApiView.as_view()),
    path('courses/', GetCoursesApiView.as_view()),
    path('teachers/', GetTeacherApiView.as_view()),
    path('student/<int:student_id>/', GetSingStudentApiView.as_view()),
    path('course/<int:pk>/', GetSingCourseApiView.as_view()),
    path('teacher/<int:pk>/', GetSingTeacherApiView.as_view()),



]
