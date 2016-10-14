class Middleware(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):

        def custom_start_response(status, headers, exc_info=None):
            headers.append(('Set-Cookie', "name=value"))
            return start_response(status, headers, exc_info)

        return self.app(environ, custom_start_response)
 
def app(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return ['The cookie has been set.']

app = Middleware(app)

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
