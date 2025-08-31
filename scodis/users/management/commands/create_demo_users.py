from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates demo users for SCODIS'

    def handle(self, *args, **options):
        User = get_user_model()
        users_data = [
            {'username': 'office_secretary', 'role': 'ADMIN', 'password': 'admin123'},
            {'username': 'kasimba-n2025', 'role': 'TEACHER', 'password': 'math123'},
            {'username': 'chinoinno', 'role': 'STUDENT', 'password': 'stu123'},
            {'username': 'Tembo-n2025', 'role': 'TEACHER', 'password': 'math123'},
            {'username': 'mercy', 'role': 'STUDENT', 'password': 'stu123'},
            {'username': 'mwale-n2025', 'role': 'TEACHER', 'password': 'math123'},
            {'username': 'zikhale-n2025', 'role': 'TEACHER', 'password': 'math23'},
            {'username': 'Mwale-n2025', 'role': 'TEACHER', 'password': 'math123'},
            {'username': 'Jamen', 'role': 'STUDENT', 'password': 'stu123'}
        ]
        
        for data in users_data:
            User.objects.create_user(**data)
        self.stdout.write(self.style.SUCCESS('Demo users created!'))