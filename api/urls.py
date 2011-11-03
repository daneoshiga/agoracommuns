from django.conf.urls.defaults import *
from piston.resource import Resource

from agoracommuns.api.handlers import *

pauta_handler = Resource(PautaHandler)
comentario_handler = Resource(ComentarioHandler)

urlpatterns = patterns('',
        url(r'^pauta/(?P<pauta_id>\d+)/comentarios/$',comentario_handler),
        url(r'^pauta/(?P<id>\d+)/$',pauta_handler),
        url(r'^pautas/status/(?P<status_id>\d+)/$',pauta_handler),
        url(r'^pautas/$',pauta_handler),
        url(r'^comentario/(?P<id>\d+)/$',comentario_handler),
        )
