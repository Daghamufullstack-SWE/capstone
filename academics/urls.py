from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, ClassRoomViewSet, SubjectViewSet

router = DefaultRouter()
router.register("departments", DepartmentViewSet)
router.register("classes", ClassRoomViewSet)
router.register("subjects", SubjectViewSet)



from .views import GuardianPortalView, StudentListView

urlpatterns = [
     path("", include(router.urls)),
    path("students/", StudentListView.as_view(), name="students"),
    path("guardian/portal/", GuardianPortalView.as_view(), name="guardian-portal"),
]
