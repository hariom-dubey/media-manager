from django.urls import path
from video.apiviews.documents import Documents

urlpatterns = [
    path('document/download', Documents.as_view(), name='document-download'),
]
