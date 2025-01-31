from .base import *

DEBUG = True

# Development-specific middleware
MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']
INSTALLED_APPS += ['debug_toolbar']

# Debug toolbar settings
INTERNAL_IPS = ['127.0.0.1']

# Email settings
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'