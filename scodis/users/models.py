from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """
    Custome user model that extends AbstractUser
    Custome Field [role,phonenumber,home_district]
    """

    class Meta:
        swappable ='AUTH_USER_MODEL'

    #roles for system access
    ROLE_CHOICES =[
        ("ADMIN","Administrator"),
        ("TEACHER","Teacher"),
        ("STUDENT","Student"),
        ("PARENT","Parent"),
        ("STAFF","Staff"),
    ]

    role = models.CharField(max_length= 20, choices=ROLE_CHOICES,default='STUDENT')
    phone = models.CharField(max_length=15, blank=True, null=True)
    groups = models.ManyToManyField('auth.Group',verbose_name='groups',blank=True,
                                    related_name='all_user_set',
                                    related_query_name='user',)
    
    user_permissions = models.ManyToManyField( 'auth.permission',
                                              verbose_name='user permission',
                                              blank = True,
                                              related_name='all_user_set',
                                              related_query_name='user',)

    def __str__(self):
        return f"{self.username} {self.role}"


