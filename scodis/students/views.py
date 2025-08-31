from django.shortcuts import render

from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Student, Attendance, Grade
from .serializers import AttendanceSerializer, GradeSerializer, StudentSerializer
from users.permissions import IsGuardian

# Create your views here.
from rest_framework import viewsets, permissions
from .models import Student, Attendance, Grade
from .serializers import StudentSerializer, AttendanceSerializer, GradeSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [permissions.IsAuthenticated]



def get_guardian_student(user):
    """
    Simplest link: assume a guardian has exactly one student mapped using
    user.student_profile via a FK on Student.guardian or a mapping table.
    For now, we assume Guardian == parent user stored on Student via a custom field,
    or if you prefer, create a Guardian model and lookup there.
    Here we look up by email/username mapping for demo purposes.
    """
    
    return Student.objects.filter(user__email=user.email).first()  # placeholder approach

class GuardianOverview(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsGuardian]

    def get(self, request):
        student = get_guardian_student(request.user)
        if not student:
            return Response({"detail":"No linked student."}, status=404)
        s = StudentSerializer(student).data
        return Response({
            "student": s,
            "student_name": student.user.get_full_name() or student.user.username,
            "classroom": student.classroom.name if student.classroom else None,
            "admission_number": student.admission_number,
        })

class GuardianAttendanceView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsGuardian]
    serializer_class = AttendanceSerializer

    def get_queryset(self):
        student = get_guardian_student(self.request.user)
        return Attendance.objects.filter(student=student).order_by("-date")

class GuardianGradesView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsGuardian]
    serializer_class = GradeSerializer

    def get_queryset(self):
        student = get_guardian_student(self.request.user)
        return Grade.objects.filter(student=student).select_related("subject").order_by("-exam_date")

