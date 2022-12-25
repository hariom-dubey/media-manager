from django.conf import settings
import os

MEDIA_DIR = os.path.join(settings.BASE_DIR, "media")
VIDEO_PATH = os.path.join(settings.BASE_DIR, "media/video")
AUDIO_PATH = os.path.join(settings.BASE_DIR, "media/audio")
DOC_PATH = os.path.join(settings.BASE_DIR, "media/document")