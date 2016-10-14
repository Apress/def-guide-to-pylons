import gzip
import StringIO

# CAUTION: This doesn't work correctly yet

class GzipMiddleware(object):
    def __init__(self, app, compresslevel=9):
        self.app = app
        self.compresslevel = compresslevel

    def __call__(self, environ, start_response):
        if 'gzip' not in environ.get('HTTP_ACCEPT_ENCODING', ''):
            return self.app(environ, start_response)
        buffer = StringIO.StringIO()
        output = gzip.GzipFile(
            mode='wb',
            compresslevel=self.compresslevel,
            fileobj=buffer
        )

        start_response_args = []
        def dummy_start_response(status, headers, exc_info=None):
            start_response_args.append(status)
            start_response_args.append(headers)
            start_response_args.append(exc_info)
            return output.write

        app_iter = self.app(environ, dummy_start_response)
        for line in app_iter:
            output.write(line)
        if hasattr(app_iter, 'close'):
            app_iter.close()
        output.close()
        buffer.seek(0)
        result = buffer.getvalue()
        start_response(**start_response_args)
        buffer.close()
        return [result]

# This isn't included in the text but will allow you to test the examples at
# http://localhost:8000/

def app(environ, start_response):
    start_response('200 OK', [('Content-type','text/plain')])
    return ['Hello World!']

app = GzipMiddleware(app)

if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.WSGIServer(
        ('0.0.0.0', 8000),
        simple_server.WSGIRequestHandler,
    )
    httpd.set_app(app)
    httpd.serve_forever()
