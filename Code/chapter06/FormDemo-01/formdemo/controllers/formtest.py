import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from formdemo.lib.base import BaseController, render
#from formdemo import model

log = logging.getLogger(__name__)

class FormtestController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'

    def form(self):
        return render('/simpleform.html')

    def submit(self):
        return 'Your e-mail is: %s' % request.params['email']

