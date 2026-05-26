from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # Panel de Administración de Django
    path('admin/', admin.site.urls),
    
    # Documentación de API (Swagger / OpenAPI 3.0)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    
    # Módulo de Autenticación
    path('api/auth/', include('authentication.urls')),
    
    # Skeletons de Módulos Universitarios (Modularidad Escalable)
    path('api/students/', include('modules.students.urls')),
    path('api/academic/', include('modules.academic.urls')),
    path('api/hr/', include('modules.hr.urls')),
    path('api/maintenance/', include('modules.maintenance.urls')),
    path('api/research/', include('modules.research.urls')),
    path('api/analytics/', include('modules.analytics.urls')),
    path('api/ai/', include('modules.ai_modules.urls')),
]
