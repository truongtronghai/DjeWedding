"""
WSGI config for ewedding project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

from pathlib import Path

# Add project directory to the sys.path

path_home = str(Path(__file__).parents[1])

if path_home not in sys.path:
	sys.path.append(path_home)
###

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ewedding.settings')

application = get_wsgi_application()
