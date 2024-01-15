from django.contrib import admin
from django.urls import path, re_path
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from .views import *
import sys

sys.path.append('app')


def response_error_handler(request, exception=None):
    return HttpResponse("Error handler content", status=403)


def permission_denied_view(request):
    raise PermissionDenied


urlpatterns = [
    path('django_admin/', admin.site.urls),
    path('my-view/', my_view, name='my-view'),
    path('curr_date/', current_datetime, name='current datetime'),
    path('', index, name='index'),
    path('signup/', signup, name="signup"),
    # re_path(r'^hospital-sim-react/src/$', )
]
