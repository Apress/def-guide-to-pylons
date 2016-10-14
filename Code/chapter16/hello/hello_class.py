class Hello(object):

    def __call__(self, environ, start_response):
        start_response('200 OK', [('Content-type','text/plain')])
        return ['Hello World!']

hello = Hello()

# This isn't included in the text but will allow you to test the examples at
# http://localhost:8000/
if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.WSGIServer(
        ('0.0.0.0', 8000),
        simple_server.WSGIRequestHandler,
    )
    httpd.set_app(hello)
    httpd.serve_forever()
