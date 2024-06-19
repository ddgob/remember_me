from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('whatsapp/', include('apps.whatsapp_gateway.urls')),
    path('messages/', include('apps.messages_processor.urls')),
]
