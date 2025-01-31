from django.conf import settings
import requests

class OutboundWhatsAppService:
    
    def send_whatsapp_message(self, recipient_wa_id, message_text):
        headers = {
            "Authorization": settings.WHATSAPP_TOKEN, 
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": recipient_wa_id,
            "text": {"body": message_text}
        }

        response = requests.post(settings.WHATSAPP_URL, json=payload, headers=headers)
        print(response.content)
        return response.json()

    def send_whatsapp_template_message(self, recipient_wa_id, template_name, language_code="pt_BR", components=None):
        headers = {
            "Authorization": settings.WHATSAPP_TOKEN, 
            "Content-Type": "application/json"
        }

        payload = {
            "messaging_product": "whatsapp",
            "to": recipient_wa_id,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {"code": language_code},
            },
        }

        if components:
            payload["template"]["components"] = components
        
        response = requests.post(settings.WHATSAPP_URL, json=payload, headers=headers)
        return response.json()