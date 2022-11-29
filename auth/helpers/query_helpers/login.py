from django.conf import settings
from auth.models import (
    User
)

from media_manager.utils.data_formatter import (
    result_row_to_dict
)

session = settings.DB_SESSION

def fetch_user_details_v1(email):
    try:
        details = session.query(
            User.id.label('user_id'),
            User.email,
            User.password
        ).filter(
            User.email == email
        ).one_or_none()

        details = (
            result_row_to_dict(details)
            if details else None
        )

    except Exception as e:
        print(e)
        details = None

    return details