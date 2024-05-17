"""
ASGI config for digital_twin_for_crop_growth_server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "digital_twin_for_crop_growth_server.settings"
)

application = get_asgi_application()
