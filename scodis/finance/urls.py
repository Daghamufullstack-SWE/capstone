
from django.urls import path, include
from guardian_portal.views import GuardianDashboardView  

urlpatterns = [
    path("", GuardianDashboardView.as_view()),

]
