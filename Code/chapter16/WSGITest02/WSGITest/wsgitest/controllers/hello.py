def HelloController(environ, start_response):
    start_response('200 OK', [('Content-Type','text/plain')])
    return ['Hello World!']

# or alternatively: 

# class HelloControllerApplication:
#     def __call__(self, environ, start_response):
#         start_response('200 OK', [('Content-Type','text/plain')])
#         return ['Hello World!']
# 
# HelloController = HelloControllerApplication()

