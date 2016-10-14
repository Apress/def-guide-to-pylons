
def app_factory(global_conf, **app_conf):
    def hello(environ, start_response):
        start_response('200 OK', [('Content-type', 'text/plain')])
        return ['Hi']
    return hello
