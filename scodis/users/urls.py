from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserListCreateView, UserDetailView, RegisterView

urlpatterns = [
    # User management
    path("", UserListCreateView.as_view(), name="user-list-create"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),

    # Authentication
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
