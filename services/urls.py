from distutils.log import Log
from django.urls import path
from services.apiviews.webhooks import Webhooks


urlpatterns = [
    path('<str:slug>/webhook', Webhooks.as_view(), name='webhooks')
]