from django.urls import path
from .views import AcademicDashboardView

urlpatterns = [
    path('dashboard/', AcademicDashboardView.as_view(), name='academic_dashboard'),
]
