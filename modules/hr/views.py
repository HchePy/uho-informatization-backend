from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.rbac import HasRole, ROLE_ADMINISTRADOR, ROLE_DECANO

class HRDashboardView(APIView):
    """
    Endpoint de prueba para el módulo de Recursos Humanos.
    Solo accesible para Administradores y Decanos debido a la sensibilidad de la nómina.
    """
    permission_classes = [IsAuthenticated, HasRole.for_roles(ROLE_ADMINISTRADOR, ROLE_DECANO)]

    def get(self, request):
        return Response({
            "modulo": "Recursos Humanos",
            "alcance": "Gestión de contratos de profesores, nóminas, plazas cubiertas e incidencias laborales universitarias.",
            "datos": {
                "total_profesores": 182,
                "plazas_disponibles": 12,
                "ultimo_pago_procesado": "2026-05-25"
            }
        })
