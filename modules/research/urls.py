from django.urls import path
from .views import ResearchDashboardView

urlpatterns = [
    path('dashboard/', ResearchDashboardView.as_view(), name='research_dashboard'),
]
