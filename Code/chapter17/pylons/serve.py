import os

from paste.deploy import loadapp
wsgi_app = loadapp('config:../SimpleSite35/SimpleSite/development.ini', relative_to=os.getcwd())

from wsgiref import simple_server
httpd = simple_server.WSGIServer(('',8000), simple_server.WSGIRequestHandler)
httpd.set_app(wsgi_app)
httpd.serve_forever()

