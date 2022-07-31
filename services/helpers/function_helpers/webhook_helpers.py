import uuid
import json
from rest_framework.response import Response
from rest_framework import status
from media_manager.utils import custom_exceptions as ce

from services.helpers.query_helpers.webhook_helpers import (
    insert_github_webhook_v1
)

def save_github_webhook_v1(request):
    try:

        webhook_insert_data = {
            'code': uuid.uuid4(),
            'response': json.dumps(request.data),
        }
        insert_github_webhook_v1(webhook_insert_data)

        return Response({
            'WEBHOOK_CAPTURE_STATUS': 1,
            'WEBHOOK_ERROR_MESSAGE': ''
        }, status = status.HTTP_200_OK)

    except Exception as e:
        raise ce.InternalServerError