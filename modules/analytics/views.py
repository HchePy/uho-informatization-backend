from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.rbac import HasRole, ROLE_ADMINISTRADOR, ROLE_DECANO

class AnalyticsDashboardView(APIView):
    """
    Endpoint de prueba para el módulo de Analítica Universitaria.
    Solo accesible para Administradores y Decanos debido a la sensibilidad estratégica.
    """
    permission_classes = [IsAuthenticated, HasRole.for_roles(ROLE_ADMINISTRADOR, ROLE_DECANO)]

    def get(self, request):
        return Response({
            "modulo": "Analítica Universitaria",
            "alcance": "Cuadros de mando gerenciales, estadísticas de rendimiento académico y reportes de eficiencia institucional UHO.",
            "datos": {
                "tasa_promocion": "87.4%",
                "eficiencia_terminal": "91.2%",
                "estudiantes_becados": 340,
                "consumo_energetico_promedio": "4.2 MWh"
            }
        })
