import cgitb
import sys
from StringIO import StringIO

class Middleware(object):
    def __init__(self, app):
        self.app = app

    def format_exception(self, exc_info):
        dummy_file = StringIO()
        hook = cgitb.Hook(file=dummy_file)
        hook(*exc_info)
        return [dummy_file.getvalue()]

    def __call__(self, environ, start_response):
        try:
            app_iter = self.app(environ, start_response)
            for data in app_iter:
                yield data
        except:
            exc_info = sys.exc_info()
            start_response(
                '500 Internal Server Error',
                [('content-type', 'text/html')],
                exc_info
            )
            for data in self.format_exception(exc_info):
                yield data
        else:
            # Calling .close() could cause an exception too
            # so in a real handler you might test for that too
            if hasattr(app_iter, 'close'):
                app_iter.close()
 
def app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    raise Exception('Let\'s trigger an exception')
    return ['No error occurred.']

app = Middleware(app)

# This isn't included in the text but will allow you to test the examples at
# http://localhost:8000/
#
# Here we are using the Paste HTTP server because the wsgiref one displays
# a cgitb error display anyway so you wouldn't be able to tell if the 
# middleware was working.
if __name__ == '__main__':
    from paste import httpserver
    httpserver.serve(app, port=8000, host='0.0.0.0')
