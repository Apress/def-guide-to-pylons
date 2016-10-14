import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from wsgitest.lib.base import BaseController, render
#from wsgitest import model

log = logging.getLogger(__name__)

class WsgiappsController(BaseController):

    def hello(self):
        response.status = '200 OK'
        response.content_type = 'text/plain'
        return "Hello World!"
