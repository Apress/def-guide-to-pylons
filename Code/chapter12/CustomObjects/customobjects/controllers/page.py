import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from customobjects.lib.base import BaseController, render
#from customobjects import model

log = logging.getLogger(__name__)

class PageController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'

    def view(self, id):
        return "Simulating the page view() action"
