from django.conf.urls import url
from .views import *

urlpatterns = [
    url("^api/rest/v1/mail$", mail_v1),
    url("^api/rest/v1/mail/(\w+)$", payload_v1),
]