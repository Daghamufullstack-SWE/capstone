from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, AttendanceViewSet, GradeViewSet, GuardianOverview, GuardianAttendanceView, GuardianGradesView

router = DefaultRouter()
router.register("students", StudentViewSet)
router.register("attendance", AttendanceViewSet)
router.register("grades", GradeViewSet)



urlpatterns = [
    path("", include(router.urls)),
    path("guardian/overview/", GuardianOverview.as_view(), name="guardian-overview"),
    path("guardian/attendance/", GuardianAttendanceView.as_view(), name="guardian-attendance"),
    path("guardian/grades/", GuardianGradesView.as_view(), name="guardian-grades"),
]

