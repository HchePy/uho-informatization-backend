from rest_framework import permissions

# ROLES INSTITUCIONALES DEFINIDOS
ROLE_ADMINISTRADOR = 'ADMINISTRADOR'
ROLE_DECANO = 'DECANO'
ROLE_PROFESOR = 'PROFESOR'
ROLE_ESTUDIANTE = 'ESTUDIANTE'
ROLE_SOPORTE_TECNICO = 'SOPORTE_TECNICO'

ROLES_CHOICES = [
    (ROLE_ADMINISTRADOR, 'Administrador del Sistema'),
    (ROLE_DECANO, 'Decano / Directivo'),
    (ROLE_PROFESOR, 'Profesor / Docente'),
    (ROLE_ESTUDIANTE, 'Estudiante Universitario'),
    (ROLE_SOPORTE_TECNICO, 'Soporte Técnico / Mantenimiento'),
]

class HasRole(permissions.BasePermission):
    """
    Permiso personalizado que verifica si el usuario autenticado posee uno de los roles permitidos.
    Uso:
        permission_classes = [HasRole.for_roles(ROLE_ADMINISTRADOR, ROLE_DECANO)]
    """
    def __init__(self, allowed_roles):
        self.allowed_roles = allowed_roles

    @classmethod
    def for_roles(cls, *roles):
        # Retorna una clase configurada dinámicamente con los roles permitidos
        class DynamicHasRole(cls):
            def __init__(self):
                super().__init__(roles)
        return DynamicHasRole

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        # Superusuarios de Django siempre tienen acceso completo
        if request.user.is_superuser:
            return True
            
        # Comprobar si el rol del usuario está dentro de los permitidos
        return request.user.role in self.allowed_roles

class IsInstitutionalStaff(permissions.BasePermission):
    """
    Permiso para personal institucional (Admin, Decanos, Profesores y Soporte).
    Excluye directamente a los estudiantes de realizar ciertas operaciones de modificación.
    """
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        if request.user.is_superuser:
            return True
            
        staff_roles = [ROLE_ADMINISTRADOR, ROLE_DECANO, ROLE_PROFESOR, ROLE_SOPORTE_TECNICO]
        return request.user.role in staff_roles
