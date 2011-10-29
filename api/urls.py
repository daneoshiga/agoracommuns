from django.conf.urls.defaults import *
from piston.resource import Resource

from agoracommuns.api.handlers import PautaHandler

pauta_handler = Resource(PautaHandler)

urlpatterns = patterns('',
        url(r'^pauta/(?P<id>[^/]+)/',pauta_handler),
        url(r'^pautas/',pauta_handler),
        )

