class Middleware(object):
    def __init__(self, app, message):
        self.app = app
        self.message = message

    def __call__(self, environ, start_response):
        environ['example.message'] = self.message
        return self.app(environ, start_response)
    
def custom_message(environ, start_response):
    start_response('200 OK', [('Content-type', 'text/plain')])
    return [environ['example.message']]

app = Middleware(custom_message, "Hello world again!")

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
