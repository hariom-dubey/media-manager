import uuid
import json
from rest_framework.response import Response
from rest_framework import status
import textwrap
from subprocess import run, PIPE
from media_manager.utils import custom_exceptions as ce

from services.helpers.query_helpers.webhook_helpers import (
    insert_github_webhook_v1
)
import traceback

def save_github_webhook_v1(request):
    try:

        is_deployed = 0
        deploy_details = None

        # try:
        #     deploy_details = {}
        #     messages = run(
        #         "deploy_media_manager.sh", stdout=PIPE, stderr=PIPE
        #     )
        #     deploy_details['stdout'] = textwrap.fill(
        #         messages.stdout.decode('utf-8'), width=1000
        #     )
        #     deploy_details['stderr'] = textwrap.fill(
        #         messages.stderr.decode('utf-8'), width=1000
        #     )
        #     is_deployed = 1
        # except Exception as e:
        #     deploy_details = traceback.format_exc()
        #     is_deployed = 0

        webhook_insert_data = {
            'code': uuid.uuid4(),
            'event': 'push',
            'response': json.dumps(request.data),
            'is_deployed': is_deployed,
            'deploy_messages': json.dumps(deploy_details)
        }
        insert_github_webhook_v1(webhook_insert_data)

        return Response({
            'WEBHOOK_CAPTURE_STATUS': 1,
            'WEBHOOK_ERROR_MESSAGE': ''
        }, status = status.HTTP_200_OK)

    except Exception as e:
        raise ce.InternalServerError