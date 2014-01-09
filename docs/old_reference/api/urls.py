from django.conf.urls.defaults import *
from piston.resource import Resource

from agoracommuns.api.handlers import *

class CsrfExemptResource(Resource):
    """A Custom Resource that is csrf exempt"""
    def __init__(self, handler, authentication=None):
        super(CsrfExemptResource, self).__init__(handler, authentication)
        self.csrf_exempt = getattr(self.handler, 'csrf_exempt', True)


pauta_handler = CsrfExemptResource(PautaHandler)
comentario_handler = CsrfExemptResource(ComentarioHandler)
deliberacao_handler = CsrfExemptResource(DeliberacaoHandler)
voto_handler = CsrfExemptResource(VotoHandler)

urlpatterns = patterns('piston.authentication',
        url(r'^oauth/request_token/$','oauth_request_token'),
        url(r'^oauth/authorize/$','oauth_user_auth'),
        url(r'^oauth/access_token/$','oauth_access_token'),
        url(r'^pauta/(?P<pauta_id>\d+)/comentarios/$',comentario_handler),
        url(r'^pauta/(?P<pauta_id>\d+)/deliberacoes/$',deliberacao_handler),
        url(r'^pauta/(?P<pauta_id>\d+)/votos/$',voto_handler),
        url(r'^pauta/(?P<id>\d+)/$',pauta_handler),
        url(r'^pautas/status/(?P<status_id>\d+)/$',pauta_handler),
        url(r'^pautas/$',pauta_handler),
        url(r'^comentario/(?P<id>\d+)/$',comentario_handler),
        url(r'^deliberacao/(?P<id>\d+)/$',deliberacao_handler),
        url(r'^deliberacao/(?P<delibera_id>\d+)/$',deliberacao_handler),
        url(r'^deliberacao/(?P<delibera_id>\d+)/votos/$',voto_handler),
        url(r'^votos/(?P<id>\d+)/$',voto_handler),
        )
