from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.rbac import HasRole, ROLE_ADMINISTRADOR, ROLE_DECANO, ROLE_PROFESOR

class StudentDashboardView(APIView):
    """
    Endpoint de prueba para el módulo de Gestión de Estudiantes.
    Solo accesible para Administradores, Decanos y Profesores.
    """
    permission_classes = [IsAuthenticated, HasRole.for_roles(ROLE_ADMINISTRADOR, ROLE_DECANO, ROLE_PROFESOR)]

    def get(self, request):
        return Response({
            "modulo": "Gestión de Estudiantes",
            "alcance": "Control y seguimiento de la matrícula escolar, expedientes de estudiantes y becas.",
            "datos": [
                {"id": 1, "nombre": "Carlos Gómez", "carrera": "Ingeniería Informática", "año": 4, "estado": "Activo"},
                {"id": 2, "nombre": "Ana Leyva", "carrera": "Ingeniería Informática", "año": 3, "estado": "Activo"},
                {"id": 3, "nombre": "Luis Pérez", "carrera": "Ingeniería Industrial", "año": 1, "estado": "Licencia Médica"},
            ]
        })
