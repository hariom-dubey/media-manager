from cerberus import Validator
import re
from media_manager.common import messages

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
                self._error(field, messages.EMAIL_INVALID)