import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from formdemo.lib.base import BaseController, render
#from formdemo import model

log = logging.getLogger(__name__)

import formdemo.lib.helpers as h

import formencode
from formencode import htmlfill
from pylons.decorators import validate

class EmailForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    email = formencode.validators.Email(not_empty=True)
    date = formencode.validators.DateConverter(not_empty=True)

def custom_formatter(error):
    return '<span class="custom-message">%s</span><br />\n' % (
        htmlfill.html_quote(error)
    )

class FormtestController(BaseController):

    def index(self):
        # Return a rendered template
        #   return render('/template.mako')
        # or, Return a response
        return 'Hello World'

    def form(self):
        return render('/simpleform.html')

    @validate(schema=EmailForm(), form='form', post_only=False, on_get=True,
        auto_error_formatter=custom_formatter)
    def submit(self):
        return 'Your e-mail is: %s and the date selected was %r.' % (
            self.form_result['email'],
            self.form_result['date'],
        )

