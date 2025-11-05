from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.models import Instructor
from api.serializers import InstructorSerializers

class InstructorListCreateApiView(ListCreateAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializers
    search_fields = ['full_name', 'specialzation']

class InstructorRetrieve(RetrieveUpdateDestroyAPIView):
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializers