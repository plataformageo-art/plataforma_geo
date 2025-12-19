from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from .supabase_jwt import verify_supabase_jwt

class SupabaseJWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth = request.headers.get("Authorization")

        if not auth:
            return None

        try:
            prefix, token = auth.split()
            if prefix.lower() != "bearer":
                raise AuthenticationFailed("Token inválido")
        except ValueError:
            raise AuthenticationFailed("Authorization header inválido")

        payload = verify_supabase_jwt(token)
        if not payload:
            raise AuthenticationFailed("JWT inválido")

        # Usuário fictício (ou mapear com model User se quiser)
        return (payload, None)
