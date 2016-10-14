import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from helloworld.lib.base import BaseController, render
#from helloworld import model

log = logging.getLogger(__name__)

class HelloController(BaseController):

    def index(self):
        return 'Hello from the index() action!'

