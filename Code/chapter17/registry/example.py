from paste.registry import RegistryManager, StackedObjectProxy
from pylons.controllers.util import Request

request = StackedObjectProxy()

# WSGI app (imagine the PylonsApp)
class App(object):
    def __call__(self, environ, start_response):
        obj = Request(environ) # The request-like theread-local object you want
                               # to access via pylons.myglobal
        if environ.has_key('paste.registry'):
            environ['paste.registry'].register(request, obj)

        start_response('200 OK', [('Content-type', 'text/html')])
        # Notice that we are using the request global here as a
        # proxy to obj (the Request instance)
        return ['PATH_INFO is %s' % request.environ['PATH_INFO'] ]

# WSGI app stack (imagine the middleware stack in config/middleware.py)
app = RegistryManager(App())


# This isn't included in the text but will allow you to test the examples at
# http://localhost:8000/
if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.WSGIServer(
        ('0.0.0.0', 8000),
        simple_server.WSGIRequestHandler,
    )
    httpd.set_app(app)
    httpd.serve_forever()
