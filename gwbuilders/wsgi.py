"""
WSGI config for gwbuilders project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwbuilders.settings')

application = get_wsgi_application()


import os
import sys

# Ensure the virtual environment is used
activate_this = '/opt/render/project/src/.venv/bin/activate_this.py'
exec(open(activate_this).read(), {'__file__': activate_this})

# Your standard Django wsgi setup
from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gwbuilders.settings')
application = get_wsgi_application()