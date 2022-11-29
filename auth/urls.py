from distutils.log import Log
from django.urls import path
from auth.apiviews.login import Login


urlpatterns = [
    path('login', Login.as_view(), name='login')
]