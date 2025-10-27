from django.urls import path
from .views import GetStudentApiView,GetCoursesApiView,GetTeacherApiView

urlpatterns = [
    path('students/', GetStudentApiView.as_view()),
    path('courses/', GetCoursesApiView.as_view()),
    path('teachers/', GetTeacherApiView.as_view()),


]
