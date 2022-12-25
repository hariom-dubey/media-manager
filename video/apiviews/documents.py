from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from media_manager.utils.custom_validator import CustomValidator
from rest_framework.versioning import NamespaceVersioning
from media_manager.utils import custom_exceptions as ce
from media_manager.common import (
    messages as glob_messages, constants as glob_constants
)
from video.common import (
    messages as app_messages, constants as app_constants
)
from video.helpers.function_helpers.document_helper import (
    export_document_v1
)

custom_validator = CustomValidator({}, allow_unknown=True)

class VersioningConfig(NamespaceVersioning):
    default_version = 'v1'
    allowed_versions =  ['v1', 'v2']
    version_param = 'version'


class Documents(APIView):

    versioning_class = VersioningConfig
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):

        try:

            if request.version == 'v1':

                schema = {
                    'url': {
                        'required': True,
                        'isurl': True,
                        'empty': False
                    },
                    'type': {
                        'required': True,
                        'allowedtypes': app_constants.ALLOWED_URL_TYPES,
                        'type': 'string',
                        'empty': False
                    }
                }

                is_valid = custom_validator.validate(request.data, schema)

                if is_valid:
                    response = export_document_v1(request)
                    return response
                else:
                    raise ce.ValidationFailed({
                        'message': glob_messages.VALIDATION_FAILED,
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