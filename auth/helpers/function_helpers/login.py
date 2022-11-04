import hashlib
from auth.common import constants
from rest_framework.response import Response
from rest_framework import status
from media_manager.utils import custom_exceptions as ce

from auth.helpers.query_helpers.login import (
    fetch_user_details_v1
)

def verify_login_v1(request):
    try:
        email = request.data.get('email')
        password = request.data.get('password')

        user = fetch_user_details_v1(email)

        if not user:
            return Response({
                    'success': False,
                    'status_code': status.HTTP_400_BAD_REQUEST,
                    'message':  'User Not Found',
                    'data': None
                },
                status=status.HTTP_400_BAD_REQUEST
            )

        if ( user.get('password') and password and
            hashlib.md5(str(password).encode('utf-8')).hexdigest() == user['password']
        ):
            return Response({
                    'success': True,
                    'status_code': status.HTTP_200_OK,
                    'message':  'Login Successfull !',
                    'data': None
                },
                status=status.HTTP_200_OK
            )
        else:
            return Response({
                    'success': False,
                    'status_code': status.HTTP_401_UNAUTHORIZED,
                    'message':  'Incorrect Password',
                    'data': None
                },
                status=status.HTTP_401_UNAUTHORIZED
            )

    except Exception as e:
        raise ce.InternalServerError