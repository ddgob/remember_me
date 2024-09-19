from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

from .functions import *
import json

def index(request):
    return HttpResponse("WhatsApp Gateway Index")

@csrf_exempt
def whatsAppWebhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN = '44db4970-c52f-43b6-ad65-ebf80585b6e5'
        mode = request.GET['hub.mode']
        token = request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status=200)
        else:
            return HttpResponse('error', status=403)
        
    if request.method == 'POST':
        data = json.loads(request.body)
        return HttpResponse('success', status=200)
    