from django.db import models

class WhatsAppUser(models.Model):
    wa_id = models.CharField(max_length=255)
    username = models.TextField()
    first_contact = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wa_id} - {self.username}"
    

class WhatsAppMessage(models.Model):
    MESSAGE_DIRECTION = (
        ('INBOUND', 'Inbound'),
        ('OUTBOUND', 'Outbound'),
    )

    message_id = models.CharField(max_length=255)
    user = models.ForeignKey(WhatsAppUser, on_delete=models.CASCADE, related_name='messages')
    text = models.TextField()
    direction = models.CharField(max_length=8, choices=MESSAGE_DIRECTION)
    processed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wa_id} - {self.text[:30]}"
    

