from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from media_manager.utils.custom_validator import CustomValidator
from rest_framework.versioning import NamespaceVersioning
from media_manager.utils import custom_exceptions as ce
from media_manager.common import messages
from auth.helpers.function_helpers.login import verify_login_v1

custom_validator = CustomValidator({}, allow_unknown=True)

class VersioningConfig(NamespaceVersioning):
    default_version = 'v1'
    allowed_versions =  ['v1', 'v2']
    version_param = 'version'


class Login(APIView):

    versioning_class = VersioningConfig
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):

        try:

            if request.version == 'v1':

                schema = {
                    'email': {
                        'required': True,
                        'isemail': True,
                        'empty': False
                    },
                    'password': {
                        'required': True,
                        'empty': False
                    }
                }

                is_valid = custom_validator.validate(request.data, schema)

                if is_valid:
                    response = verify_login_v1(request)
                    return response
                else:
                    raise ce.ValidationFailed({
                        'message': messages.VALIDATION_FAILED,
                        'data': custom_validator.errors
                    })
            else:
                raise ce.VersionNotSupported

        except ce.ValidationFailed as vf:
            raise vf
        except ce.VersionNotSupported as ver:
            raise ver
        except Exception as e:
            print(e)
            raise ce.InternalServerError