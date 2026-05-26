from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.rbac import HasRole, ROLE_ADMINISTRADOR, ROLE_SOPORTE_TECNICO

class MaintenanceDashboardView(APIView):
    """
    Endpoint de prueba para el módulo de Mantenimiento e Incidencias.
    Solo accesible para Administradores y Soporte Técnico.
    """
    permission_classes = [IsAuthenticated, HasRole.for_roles(ROLE_ADMINISTRADOR, ROLE_SOPORTE_TECNICO)]

    def get(self, request):
        return Response({
            "modulo": "Mantenimiento",
            "alcance": "Control de activos físicos, reporte de roturas en laboratorios y reparaciones del campus universitario.",
            "datos": {
                "solicitudes_pendientes": 8,
                "reparaciones_en_curso": 3,
                "laboratorios_inspeccionados": ["Laboratorio de Redes UHO", "Laboratorio de Robótica y IA"]
            }
        })
