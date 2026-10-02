import os
from django.core.asgi import get_asgi_application
from django.contrib.staticfiles.handlers import ASGIStaticFilesHandler

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Wrap with ASGIStaticFilesHandler
application = ASGIStaticFilesHandler(get_asgi_application())
