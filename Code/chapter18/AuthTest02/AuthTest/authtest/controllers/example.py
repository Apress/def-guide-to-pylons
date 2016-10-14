import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from authtest.lib.base import BaseController, render
#from authtest import model

log = logging.getLogger(__name__)

class ExampleController(BaseController):

    def hello(self):
        return self._result()
    
    def _result(self):
        return 'Hello World!'

