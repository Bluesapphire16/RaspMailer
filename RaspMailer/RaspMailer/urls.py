"""
Definition of urls for RaspMailer.
"""

from datetime import datetime
from django.urls import path
from django.conf.urls import url, include
from django.contrib import admin
import mails.urls
import authentification.urls


urlpatterns = [
    path('admin/', admin.site.urls),

    url("^mails/", include(mails.urls))
]
