from django.urls import path
from .views import MaintenanceDashboardView

urlpatterns = [
    path('dashboard/', MaintenanceDashboardView.as_view(), name='maintenance_dashboard'),
]
