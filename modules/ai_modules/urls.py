from django.urls import path
from .views import AIDashboardView

urlpatterns = [
    path('dashboard/', AIDashboardView.as_view(), name='ai_dashboard'),
]
