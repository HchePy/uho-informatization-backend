from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.rbac import HasRole, ROLE_ADMINISTRADOR, ROLE_DECANO, ROLE_PROFESOR

class ResearchDashboardView(APIView):
    """
    Endpoint de prueba para el módulo de Proyectos de Investigación y Tesis.
    Solo accesible para Administradores, Decanos y Profesores.
    """
    permission_classes = [IsAuthenticated, HasRole.for_roles(ROLE_ADMINISTRADOR, ROLE_DECANO, ROLE_PROFESOR)]

    def get(self, request):
        return Response({
            "modulo": "Proyectos de Investigación",
            "alcance": "Seguimiento de investigaciones, proyectos de grado, publicaciones científicas y patentes de la UHO.",
            "datos": [
                {"titulo": "Optimización del Tránsito Ferroviario usando Algoritmos Genéticos", "lider": "Dr. Juan Pérez", "estado": "En Curso", "año_inicio": 2024},
                {"titulo": "Sistema de Monitoreo de Consumo Eléctrico UHO", "lider": "MSc. Elena Rost", "estado": "Completado", "año_inicio": 2023},
            ]
        })
