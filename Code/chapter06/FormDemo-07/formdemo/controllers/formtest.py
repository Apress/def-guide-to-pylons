import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from formdemo.lib.base import BaseController, render
#from formdemo import model

log = logging.getLogger(__name__)

import formdemo.lib.helpers as h

import formencode
from formencode import htmlfill

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
            c.form_result = schema.to_python(dict(request.params))
        except formencode.Invalid, error:
            c.form_result = error.value
            c.form_errors = error.error_dict or {}
            html = render('/simpleform.html')
            return htmlfill.render(
                html,
                defaults=c.form_result,
                errors=c.form_errors
            )
        else:
            return 'Your e-mail is: %s and the date selected was %r.' % (
                c.form_result['email'],
                c.form_result['date'],
            )
        
