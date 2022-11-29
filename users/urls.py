from django.urls import path
from . import views
from users.apiviews.user import User

urlpatterns = [
    path('details/', User.as_view(), name='details'),
]