from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

@method_decorator(login_required, name="dispatch")
class GuardianDashboardView(TemplateView):

    permission_classes = [IsAuthenticated]

    
    template_name = "guardian_dashboard.html"


    def get(self, request, *args, **kwargs):
        context = {
            "guardian": request.user,
            # Later: include guardian’s students, payments, attendance, etc.
        }
        return render(request, self.template_name, context)


    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        # Provide minimal context; JS will fetch detailed data via APIs
        ctx["student_name"] = ""
        ctx["classroom"] = ""
        ctx["admission_number"] = ""
        return ctx