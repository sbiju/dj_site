from django import VERSION
from django.http import (HttpResponse as BaseHttpResponse,
                         HttpResponseBadRequest as Base400)

# https://github.com/chicagobuss/graphite-web/commit/842944a34085c4b6bd5f37532118be996a0ff4f1
class ContentTypeMixin(object):
    def __init__(self, *args, **kwargs):
        if VERSION < (1, 5) and 'content_type' in kwargs:
            kwargs['mimetype'] = kwargs.pop('content_type')
        elif VERSION > (1, 7) and 'mimetype' in kwargs:
            kwargs['content_type'] = kwargs.pop('mimetype')
        super(ContentTypeMixin, self).__init__(*args, **kwargs)

class HttpResponse(ContentTypeMixin, BaseHttpResponse):
    pass

class HttpResponseBadRequest(ContentTypeMixin, Base400):
    pass
