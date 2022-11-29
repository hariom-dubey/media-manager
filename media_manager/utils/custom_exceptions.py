from rest_framework import status
from rest_framework.exceptions import APIException

from media_manager.common import messages, constants

class InternalServerError(APIException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    default_detail = messages.INTERNAL_SERVER_ERROR
    default_code = 'internal_server_error'

class UnknownColumnError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = messages.UNKNOWN_COLUMN
    default_code = 'unknown_column'

class DuplicateKey(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = messages.DUPLICATE_KEY
    default_code = 'duplicate_key'

class ValidationFailed(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = messages.VALIDATION_FAILED
    default_code = 'validation_failed'

class VersionNotSupported(APIException):
    status_code = status.HTTP_505_HTTP_VERSION_NOT_SUPPORTED
    default_detail = messages.VERSION_NOT_SUPPORTED
    default_code = 'version_not_supported'

class ExpiredSignatureError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = messages.ACCESS_TOKEN_EXPIRED
    default_code = 'expired_signature_error'


class InvalidSignatureError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = messages.TOKEN_INVALID
    default_code = 'invalid_signature_error'


class DecodeError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = messages.DECODE_ERROR
    default_code = 'decode_error'


class InvalidTokenError(APIException):
    status_code = status.HTTP_401_UNAUTHORIZED
    default_detail = messages.TOKEN_INVALID
    default_code = 'invalid_token_error'

class ResetKeyInvalid(APIException):
    status_code = status.HTTP_404_NOT_FOUND
    default_detail = messages.USER_NOT_FOUND
    default_code = 'reset_key_invalid'

class InvalidSlug(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = messages.INVALID_SLUG
    default_code = 'invalid_slug'