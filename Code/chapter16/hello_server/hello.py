from wsgiref import simple_server

def hello(environ, start_response):
    start_response('200 OK', [('Content-type','text/plain')])
    return ["Hello World!"]

httpd = simple_server.WSGIServer(
    ('0.0.0.0', 8000),
    simple_server.WSGIRequestHandler,
)
httpd.set_app(hello)
httpd.serve_forever()

