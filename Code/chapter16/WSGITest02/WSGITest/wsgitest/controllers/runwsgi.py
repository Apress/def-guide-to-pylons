import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from wsgitest.lib.base import BaseController, render
#from wsgitest import model

log = logging.getLogger(__name__)

# WSGI application
def wsgi_app(environ, start_response):
    start_response('200 OK',[('Content-type','text/html')])
    return ['<html>\n<body>\nHello World!\n</body>\n</html>']

# Pylons controller
class RunwsgiController(BaseController):

    def index(self, environ, start_response):
        return wsgi_app(environ, start_response)

