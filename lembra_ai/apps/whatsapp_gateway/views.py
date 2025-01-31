import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .services.inbound_whatsapp_service import InboundWhatsAppService
from django.conf import settings

def index(request):
    return HttpResponse("WhatsApp Gateway Index")

@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'GET':
        return verify_webhook(request)
        
    elif request.method == 'POST':
        data = json.loads(request.body or '{}')

        if not validate_data(data):
            return HttpResponse('invalid data', status=400)

        if data['object'] != 'whatsapp_business_account':
            # TODO
            print("This case never happened before. Debug it and make this message better!")

        service = InboundWhatsAppService()

        service.process_incoming_data(data)

        return HttpResponse('success', status=200)

def verify_webhook(request):
    mode = request.GET.get('hub.mode')
    token = request.GET.get('hub.verify_token')
    challenge = request.GET.get('hub.challenge')

    if mode == 'subscribe' and token == settings.VERIFY_TOKEN:
        return HttpResponse(challenge, status=200)
    return HttpResponse('error', status=403)

def validate_data(data):
    return 'object' in data and 'entry' in data