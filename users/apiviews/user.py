from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class User(APIView):

    permission_classes = ()
    authentication_classes = ()

    def get(self, request):
        return Response(
            {
                'success': True,
                'msg': 'users table is called'
            }, status=status.HTTP_200_OK
        )