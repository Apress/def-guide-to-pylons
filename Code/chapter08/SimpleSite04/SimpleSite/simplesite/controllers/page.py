import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from simplesite.lib.base import BaseController, render
#from simplesite import model

log = logging.getLogger(__name__)

class PageController(BaseController):

    def view(self, id):
        c.title = 'Greetings'
        c.heading = 'Sample Page'
        c.content = "This is page %s"%id
        return render('/derived/page/view.html')
