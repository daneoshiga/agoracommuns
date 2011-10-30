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

    def create(self, request, *args, **kwargs):
        if not hasattr(request, "data"):
            request.data = request.POST
        attrs = self.flatten_dict(request.data)
        try:
            model = self.model(testfield=attrs['testfield'])
        except:
            return rc.BAD_REQUEST
        else:
            model.save()
        return model

