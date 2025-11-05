from django.urls import path
from api.views import CourseGetPostApiView, CourseDetailApiView, InstructorRetrieve, InstructorListCreateApiView

urlpatterns = [
    path('courses/', CourseGetPostApiView.as_view()),
    path('course/<int:pk>/', CourseDetailApiView.as_view()),
    path('instructors/', InstructorListCreateApiView.as_view()),
    path('instructors/<int:pk>/', InstructorRetrieve.as_view()),
    

]
