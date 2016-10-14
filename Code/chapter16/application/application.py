class Application(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, environ, start_response):
        if environ['PATH_INFO'] == '/hello':
            return self.hello(environ, start_response)
        elif environ['PATH_INFO'] == '/goodbye':
            return self.goodbye(environ, start_response)
        else:
            start_response('404 Not Found', [('Content-type','text/html')])
            return ['Not found']

    def hello(self, environ, start_response):
        start_response('200 OK', [('Content-type','text/html')])
        return ['Hello %s'%(self.name)]

    def goodbye(self, environ, start_response):
        start_response('200 OK', [('Content-type','text/html')])
        return ['Goodbye %s'%(self.name)]

app = Application('Harry')


# This isn't included in the text but will allow you to test the examples at
# http://localhost:8000/hello and http://localhost:8000/goodbye
if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.WSGIServer(
        ('0.0.0.0', 8000),
        simple_server.WSGIRequestHandler,
    )
    httpd.set_app(app)
    httpd.serve_forever()


