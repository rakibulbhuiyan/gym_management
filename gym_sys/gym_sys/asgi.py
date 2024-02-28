import os

from django.core.asgi import get_asgi_application
import app.routing  

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gym_sys.settings')
from channels.routing import ProtocolTypeRouter, URLRouter

# application = get_asgi_application()
application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(app.routing.NotificationConsumer)
})
