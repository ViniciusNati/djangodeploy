"""
WSGI config for iblogs project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
import sys

path = 'web-production-d0bc.up.railway.app'  # insira o caminho para o seu projeto aqui
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'iblogs.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()