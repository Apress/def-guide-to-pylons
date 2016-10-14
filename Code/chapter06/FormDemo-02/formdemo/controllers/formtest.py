import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from formdemo.lib.base import BaseController, render
#from formdemo import model

log = logging.getLogger(__name__)

import formdemo.lib.helpers as h

class FormtestController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'

    def form(self):
        return render('/simpleform.html')

    def submit(self):
        # Code to perform some action based on the form data
        # ...
        h.redirect_to(controller='formtest', action='result')

    def result(self):
        return 'Your data was successfully submitted'

