from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.rbac import IsInstitutionalStaff

class AIDashboardView(APIView):
    """
    Endpoint de prueba para el módulo de Inteligencia Artificial.
    Solo accesible para Personal Institucional (excluye Estudiantes).
    """
    permission_classes = [IsAuthenticated, IsInstitutionalStaff]

    def get(self, request):
        return Response({
            "modulo": "Inteligencia Artificial UHO",
            "alcance": "Predicción de deserción escolar, recomendación de asignaturas optativas y automatización documental.",
            "modelos_activos": [
                {"nombre": "Predictor de Deserción", "tipo": "Clasificación (Random Forest)", "precision": "94.2%"},
                {"nombre": "Analizador de Sentimientos de Encuestas", "tipo": "NLP (Transformer local)", "precision": "89.7%"}
            ]
        })
