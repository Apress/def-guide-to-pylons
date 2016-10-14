import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from templatedemo.lib.base import BaseController, render
#from templatedemo import model

log = logging.getLogger(__name__)

class GreetingController(BaseController):

    def index(self):
        name = 'Pylons Developer'
        return render('/greeting.html', extra_vars={'name': name})

