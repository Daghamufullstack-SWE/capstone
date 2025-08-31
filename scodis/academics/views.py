from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Department, ClassRoom, Subject
from .serializers import DepartmentSerializer, ClassRoomSerializer, SubjectSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ClassRoomViewSet(viewsets.ModelViewSet):
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSerializer
    permission_classes = [permissions.IsAuthenticated]


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [permissions.IsAuthenticated]


from rest_framework import generics, permissions
from .models import Guardian, Student
from .serializers import GuardianSerializer, StudentSerializer
from users.permissions import IsGuardian, IsAdmin

# Guardian portal view
class GuardianPortalView(generics.RetrieveAPIView):
    queryset = Guardian.objects.all()
    serializer_class = GuardianSerializer
    permission_classes = [permissions.IsAuthenticated, IsGuardian]

    def get_object(self):
        return Guardian.objects.get(user=self.request.user)


# Admin-only list of all students
class StudentListView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
