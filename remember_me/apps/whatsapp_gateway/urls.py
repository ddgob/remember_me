from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='whatsapp_index'),
    path('22a16f22-cd78-4013-936a-1588fc890909', views.whatsAppWebhook, name='whatsapp_webhook'),
]

# Token - 44db4970-c52f-43b6-ad65-ebf80585b6e5