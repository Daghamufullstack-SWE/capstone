from django.db import models
from users.models import User

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ClassRoom(models.Model):
    name = models.CharField(max_length=50, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="classes")

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    classroom = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, related_name="subjects")

    def __str__(self):
        return f"{self.name} ({self.code})"
    



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="academic_student_profile")
    admission_number = models.CharField(max_length=20, unique=True)
    grade_level = models.CharField(max_length=20)
    department = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.admission_number}"


class Guardian(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="guardian_profile")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="guardians")
    relationship = models.CharField(max_length=20, choices=(
        ('FATHER', 'Father'),
        ('MOTHER', 'Mother'),
        ('OTHER', 'Other'),
    ))

    def __str__(self):
        return f"{self.user.get_full_name()} (Guardian of {self.student.user.get_full_name()})"

