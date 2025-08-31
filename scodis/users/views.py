from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions
from .models import User
from .serializers import UserSerializer,RegisterSerializer

User = get_user_model()

class UserListCreateView(generics.ListCreateAPIView):
    """
    API endpoint for listing all registered Users and
    APIEndpoint  for creating a User
      GET : List all Users
      POST : Create new User
    Requires Authetication

    """
    queryset = User.objects.all()
    serializer_class =UserSerializer
    #permission_classes =[permissions.IsAuthenticated]

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    APIEndpoint for retrieving, updating and deleting a user
       * GET : single user details
       * PUT/PATCH : Update User
       * DELETE : delete a User
    
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]





class RegisterView(generics.CreateAPIView):
    """
    Endpoint for new user registration.
    """
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
