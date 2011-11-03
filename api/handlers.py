from piston.handler import BaseHandler
from core.models import * 

class PautaHandler(BaseHandler):
    allowed_methods = ('GET','PUT','POST','DELETE')
    model = Pauta

    def read(self, request, id=None, status_id=None, autor=None, datainicio=None, datafim=None):
        """
        First draft of what GET /api/pautas should return
        """

        base = Pauta.objects

        if id:
            return base.get(pk=id)
        elif status_id:
            return base.get(status=status_id)
        else:
            return base.all()

    def create(self, request, *args, **kwargs):
        if not hasattr(request, "data"):
            request.data = request.POST
        attrs = self.flatten_dict(request.data)
        try:
            model = self.model(usuario = attrs['usuario'],
                    data_validacao = attrs['data_validacao'],
                    data_delibera = attrs['data_delibera'],
                    data_votacao = attrs['data_votacao'],
                    votos_promover = attrs['votos_promover'],
                    titulo = attrs['titulo'],
                    pauta = attrs['pauta'],
                    status = 1
                    )
        except:
            return rc.BAD_REQUEST
        else:
            model.save()
        return model

class DeliberacaoHandler(BaseHandler):
    deliberacao = Deliberacao

class VotoHandler(BaseHandler):
    voto = Voto

class ComentarioHandler(BaseHandler):
    allowed_methods = ('GET','PUT','POST','DELETE')
    comentario = Comentario

    def read(self, request, id=None, pauta_id=None):
        base = Comentario.objects

        if id:
            return base.get(pk=id)
        elif pauta_id:
            return base.get(pauta=pauta_id)
        else:
            return base.all()
