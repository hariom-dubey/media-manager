from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from media_manager.utils.custom_validator import CustomValidator
from rest_framework.versioning import NamespaceVersioning
from media_manager.utils import custom_exceptions as ce
from services.common import constants
from services.helpers.function_helpers.webhook_helpers import save_github_webhook_v1

custom_validator = CustomValidator({}, allow_unknown=True)

class VersioningConfig(NamespaceVersioning):
    default_version = 'v1'
    allowed_versions =  ['v1', 'v2']
    version_param = 'version'


class Webhooks(APIView):

    versioning_class = VersioningConfig
    authentication_classes = ()
    permission_classes = ()

    def post(self, request, slug):

        try:

            if request.version == 'v1':
                if slug == constants.GIT_WEBHOOK_SLUG:
                    response = save_github_webhook_v1(request)
                    return response
                else:
                    raise ce.InvalidSlug
            else:
                raise ce.VersionNotSupported

        except ce.ValidationFailed as vf:
            raise vf
        except ce.InvalidSlug as ins:
            raise ins
        except ce.VersionNotSupported as ver:
            raise ver
        except Exception as e:
            raise ce.InternalServerError