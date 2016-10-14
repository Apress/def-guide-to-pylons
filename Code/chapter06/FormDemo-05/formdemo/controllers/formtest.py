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
        c.email_msg = ''
        email = request.params.get('email')
        if not email:
            c.email_msg = "Please enter a value"
        elif '@' not in email:
            c.email_msg = "An e-mail address must contain at least one '@' character."
        else:
            domain = email.split('@')[1]
            if '.' not in domain:
                c.email_msg = "An e-mail address domain must contain "
                c.email_msg += "at least one '.' character."
            if not domain.split('.')[-1]:
                c.email_msg = "Please specify a domain type after the '.' character"
        if c.email_msg:
            c.email_value = email
            return render('/simpleform.html')
        return 'Your e-mail is: %s' % request.params['email']
