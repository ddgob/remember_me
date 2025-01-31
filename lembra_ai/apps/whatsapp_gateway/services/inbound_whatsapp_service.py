from ..models import WhatsAppUser, WhatsAppMessage
from .outbound_whatsapp_service import OutboundWhatsAppService

class InboundWhatsAppService:
    
    def process_incoming_data(self, data):
        """
            https://developers.facebook.com/docs/whatsapp/cloud-api/webhooks/payload-examples
        """
        for entry in data.get('entry', []):
            changes = entry.get('changes', [])
            for change in changes:
                value = change.get('value', {})
                contacts = value.get('contacts', [])
                messages = value.get('messages', [])
                self.process_messages(contacts, messages)

    def process_messages(self, contacts, messages):
        for contact in contacts:
            profile_name = contact.get('profile', {}).get('name', '')
            wa_id = contact.get('wa_id', '')
            for message in messages:
                # TODO: Add logic to deal with other kind of messages
                if message.get('type') != 'text':
                    continue
                message_data = self.extract_message_data(message, profile_name, wa_id)
                self.receive_message(message_data)

    def extract_message_data(self, message, profile_name, wa_id):
        return {
            'profile_name': profile_name,
            'wa_id': wa_id,
            'from_id': message.get('from', ''),
            'message_id': message.get('id', ''),
            'timestamp': message.get('timestamp', ''),
            'text_body': message.get('text', {}).get('body', ''),
            'message_obj': message,
        }

    def receive_message(self, message_data: dict) -> None:
        wa_id = message_data.get('wa_id')
        username = message_data.get('profile_name')
        message_id = message_data.get('message_id')
        text_body = message_data.get('text_body')

        user = self.get_or_create_user(wa_id=wa_id, username=username)
        self.save_inbound_message(user, message_id, text_body)

        response_text = f"Oi {user.username}, eu recebi a sua mensagem: {text_body}"
        outbound_service = OutboundWhatsAppService()
        outbound_service.send_whatsapp_message(wa_id, response_text)

    def get_or_create_user(self, wa_id: str, username: str) -> WhatsAppUser:
        user, created = WhatsAppUser.objects.get_or_create(
            wa_id=wa_id,
            defaults={'username': username}
        )
        
        if not created and user.username != username:
            user.username = username
            user.save(update_fields=['username'])

        return user

    def save_inbound_message(self, user: WhatsAppUser, message_id: str, text_body: str) -> WhatsAppMessage:
        return WhatsAppMessage.objects.create(
            message_id=message_id,
            user=user,
            text=text_body,
            direction='INBOUND'
        )

    