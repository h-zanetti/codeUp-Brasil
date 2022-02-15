"""
ASGI config for webdev project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
from django.core.asgi import get_asgi_application
from webdev.settings.base import BASE_DIR
from dotenv import load_dotenv

# Load environmental variables
dotenv_path = os.path.join(BASE_DIR.parent, '.env')
load_dotenv(dotenv_path)

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webdev.settings')

application = get_asgi_application()
