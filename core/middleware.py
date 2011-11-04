class ContentTypeMiddleware(object):

    def process_request(self, request):
        if request.META['CONTENT_TYPE'] == 'application/x-www-form-urlencoded; charset=UTF-8':
            request.META['CONTENT_TYPE'] = 'application/x-www-form-urlencoded'
        return None
