# django
from django.conf.urls import url

# app
from .views import PermissionView


urlpatterns = [
    url('', PermissionView.as_view(), name='permission'),
]
