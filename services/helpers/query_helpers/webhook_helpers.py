from django.conf import settings
from services.models import (
    MediaGithubWebhookLog
)

session = settings.DB_SESSION

def insert_github_webhook_v1(data):
    try:
        application = MediaGithubWebhookLog(**data)

        session.add(application)
        session.commit()

    except Exception as e:
        print(e)
        session.rollback()