from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Invoice
from .serializers import InvoiceSerializer
from users.permissions import IsGuardian
from students.views import get_guardian_student

class GuardianFeesView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, IsGuardian]
    serializer_class = InvoiceSerializer

    def get_queryset(self):
        student = get_guardian_student(self.request.user)
        return Invoice.objects.filter(student=student).order_by("-created_at")
