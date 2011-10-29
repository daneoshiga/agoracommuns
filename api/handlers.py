from piston.handler import BaseHandler
from core.models import Pauta

class PautaHandler(BaseHandler):
    allowed_methods = ('GET','PUT','POST','DELETE')
    model = Pauta

    def read(self, request, id=None):
        """
        First draft of what GET /api/pautas should return
        """

        base = Pauta.objects

        if id:
            return base.get(pk=id)
        else:
            return base.all()
