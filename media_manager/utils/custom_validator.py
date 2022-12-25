from cerberus import Validator
import re
from media_manager.common import (
    messages as glob_messages, constants as glob_constants
)

class CustomValidator(Validator):
    def _validate_isemail(self, constraint, field, value):
        """
            Test the field value is of email type

            The rule's arguments are validated against this schema:
            {'type': 'boolean'}
        """
        if constraint is True:
            email_regex = '^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
            email = re.match(email_regex, value)
            if not email:
                self._error(field, glob_messages.EMAIL_INVALID)
    def _validate_allowedtypes(self, allowedtypes, field, value):
        """
            {'type': 'list'}
        """
        if allowedtypes:
            if not value.upper() in allowedtypes:
                self._error(field, glob_messages.INVALID_TYPE)
    def _validate_isurl(self, constraint, field, value):
        """
            {'type': 'boolean'}
        """
        if constraint is True:
            url_regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
            url = re.match(url_regex, value)
            if not url:
                self._error(field, glob_messages.URL_INVALID)