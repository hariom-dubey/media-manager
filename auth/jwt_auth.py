import jwt
from rest_framework.authentication import BaseAuthentication

def JWTAuthentication(BaseAuthentication):
    """
        Used to authenticate user request with token
    """

    def authenticate(self, request):
        try:
            pass
        except Exception as e:
            print()