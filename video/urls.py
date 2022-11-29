from django.urls import path
from .views import video_download

urlpatterns = [
    path('download', video_download, name='video-download'),
]
