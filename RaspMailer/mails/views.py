from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django import http
from .api import *

@csrf_exempt
def mail_v1(request):
    return REST_API_v1.get_mail()

@csrf_exempt
def payload_v1(request, id):
    return REST_API_v1.get_payload(id)