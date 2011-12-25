from piston.handler import BaseHandler
from piston.utils import rc
from core.models import * 

class PautaHandler(BaseHandler):
    allowed_methods = ('GET','PUT','POST','DELETE')
    model = Pauta

    def read(self, request, id=None, status_id=None, autor=None, datainicio=None, datafim=None):
        """
        First draft of what GET /api/pautas should return
        """

        base = Pauta.objects

        try:
            if id:
                return base.get(pk=id)
            elif status_id:
                return base.filter(status=status_id)
            else:
                return base.all()
        except:
            return rc.NOT_FOUND


    def create(self, request, *args, **kwargs):
        if not hasattr(request, "data"):
            request.data = request.POST
        attrs = self.flatten_dict(request.data)
        try:
            model = self.model(
                    usuario = Usuario.objects.get(pk=attrs['usuario']),
                    data_validacao = attrs['data_validacao'],
                    data_delibera = attrs['data_delibera'],
                    data_votacao = attrs['data_votacao'],
                    votos_promover = attrs['votos_promover'],
                    titulo = attrs['titulo'],
                    pauta = attrs['pauta'],
                    status = 1,
                    )
        except:
            return rc.BAD_REQUEST
        else:
            model.save()
        return model

    def delete(self, request, id=None):
        try:
            pauta = Pauta.objects.get(pk=id)
        except:
            return rc.NOT_FOUND
        try:
            pauta.delete()
        except:
            return rc.BAD_REQUEST
        else:
            return rc.DELETED


class DeliberacaoHandler(BaseHandler):
    allowed_methods = ('GET','PUT','POST','DELETE')
    deliberacao = Deliberacao

    def read(self, request, id=None, pauta_id=None):
        base = Deliberacao.objects

        try:
            if id:
                return base.get(pk=id)
            elif pauta_id:
                return base.filter(pauta=pauta_id)
            else:
                return base.all()
        except:
            return rc.NOT_FOUND


    def create(self, request, *args, **kwargs):
        if not hasattr(request, "data"):
            request.data = request.POST

        attrs = self.flatten_dict(request.data)
        try:
            mymodel = Deliberacao(
                pauta=Pauta.objects.get(pk=kwargs['pauta_id']),
                usuario=Usuario.objects.get(pk=attrs['usuario']),
                proposta=attrs['proposta'],
                )
        except:
            return rc.BAD_REQUEST
        else:
            mymodel.save()
            return mymodel

    def delete(self, request, id=None):
        try:
            deliberacao = Deliberacao.objects.get(pk=id)
        except:
            return rc.NOT_FOUND
        try:
            deliberacao.delete()
        except:
            return rc.BAD_REQUEST
        else:
            return rc.DELETED


class VotoHandler(BaseHandler):
    allowed_methods = ('GET','PUT','POST','DELETE')

    def read(self, request, id=None, pauta_id=None, delibera_id=None):
        base = Voto.objects

        try:
            if id:
                return base.get(pk=id)
            elif pauta_id:
                return base.filter(pauta=pauta_id)
            elif delibera_id:
                return base.filter(deliberacao=delibera_id)
            else:
                return base.all()
        except:
            return rc.NOT_FOUND

    def create(self, request, *args, **kwargs):
        if not hasattr(request, "data"):
            request.data = request.POST

        attrs = self.flatten_dict(request.data)


        try:
            #FIXME find better way to reference pauta and deliberacao votes
            if 'pauta_id' in kwargs:
                mymodel = Voto(
                        pauta= Pauta.objects.get(pk=kwargs['pauta_id']),
                        usuario=Usuario.objects.get(pk=attrs['usuario']),
                        tipo=attrs['tipo'],
                        )
            else:
                mymodel = Voto(
                        deliberacao=Deliberacao.objects.get(pk=kwargs['delibera_id']),
                        usuario=Usuario.objects.get(pk=attrs['usuario']),
                        tipo=attrs['tipo'],
                        )

        except:
            return rc.BAD_REQUEST
        else:
            mymodel.save()
        return mymodel

    def delete(self, request, id=None):
        try:
            voto = Voto.objects.get(pk=id)
        except:
            return rc.NOT_FOUND
        try:
            voto.delete()
        except:
            return rc.BAD_REQUEST
        else:
            return rc.DELETED


class ComentarioHandler(BaseHandler):
    allowed_methods = ('GET','PUT','POST','DELETE')
    comentario = Comentario

    def read(self, request, id=None, pauta_id=None):
        base = Comentario.objects

        try:
            if id:
                return base.get(pk=id)
            elif pauta_id:
                return base.filter(pauta=pauta_id)
            else:
                return base.all()
        except:
            return rc.NOT_FOUND

    def create(self, request, *args, **kwargs):
        if not hasattr(request, "data"):
            request.data = request.POST

        attrs = self.flatten_dict(request.data)
        try:
            mymodel = Comentario(
                pauta=Pauta.objects.get(pk=kwargs['pauta_id']),
                texto=attrs['texto'],
                )
        except:
            return rc.BAD_REQUEST
        else:
            mymodel.save()
            return mymodel

    def delete(self, request, id=None):
        try:
            comentario = Comentario.objects.get(pk=id)
        except:
            return rc.NOT_FOUND
        try:
            comentario.delete()
        except:
            return rc.BAD_REQUEST
        else:
            return rc.DELETED

