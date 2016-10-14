import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from formdemo.lib.base import BaseController, render
#from formdemo import model

log = logging.getLogger(__name__)

import formdemo.lib.helpers as h

import formencode

class EmailForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    email = formencode.validators.Email(not_empty=True)
    date = formencode.validators.DateConverter(not_empty=True)

class FormtestController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'

    def form(self):
        return render('/simpleform.html')

    def submit(self):
        schema = EmailForm()
        try:
            form_result = schema.to_python(dict(request.params))
        except formencode.Invalid, error:
            response.content_type = 'text/plain'
            return 'Invalid: '+str(error)
        else:
            return 'Your e-mail is: %s'%form_result.get('email')
    
