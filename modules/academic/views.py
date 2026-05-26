from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class AcademicDashboardView(APIView):
    """
    Endpoint de prueba para el módulo de Procesos Académicos.
    Accesible para todos los usuarios autenticados.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "modulo": "Procesos Académicos",
            "alcance": "Planificación docente, gestión de asignaturas, horarios de clase y evaluaciones universitarias.",
            "datos": {
                "semestre_actual": "Segundo Semestre 2026",
                "total_asignaturas": 45,
                "planes_de_estudio_activos": ["Plan E - Informática", "Plan E - Industrial", "Plan E - Mecánica"]
            }
        })
