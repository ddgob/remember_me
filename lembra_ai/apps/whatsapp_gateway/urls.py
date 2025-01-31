from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='whatsapp_index'),
    path(settings.WHATSAPP_WEBHOOK_PATH, views.whatsapp_webhook, name='whatsapp_webhook'),
]