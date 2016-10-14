import gzip
import StringIO

class GzipMiddleware(object):
    def __init__(self, app, compresslevel=9):
        self.app = app
        self.compresslevel = compresslevel

    def __call__(self, environ, start_response):
        if 'gzip' not in environ.get('HTTP_ACCEPT_ENCODING', ''):
            return self.app(environ, start_response)
        if environ['PATH_INFO'][-3:] != '.js' and environ['PATH_INFO'][-4:] != '.css':
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
        headers = []
        for name, value in start_response_args[1]:
            if name.lower() != 'content-length':
                headers.append((name, value))
        headers.append(('Content-Length', str(len(result))))
        headers.append(('Content-Encoding', 'gzip'))
        start_response(start_response_args[0], headers, start_response_args[2])
        buffer.close()
        return [result]

# This isn't included in the text but will allow you to test the examples.
# Visit http://localhost:8000/hello.txt for a non-Gzipped response and
# http://localhost:8000/hello.js for the Gzipped response 

def app(environ, start_response):
    write = start_response('200 OK', [('Content-type','text/plain')])
    write('Hello')
    return [' World!']

from wsgiref.validate import validator

app = validator(GzipMiddleware(validator(app)))

if __name__ == '__main__':
    from wsgiref import simple_server
    httpd = simple_server.WSGIServer(
        ('0.0.0.0', 8000),
        simple_server.WSGIRequestHandler,
    )
    httpd.set_app(app)
    httpd.serve_forever()
