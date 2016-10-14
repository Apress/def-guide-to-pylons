import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from simplesite.lib.base import BaseController, render
#from simplesite import model

log = logging.getLogger(__name__)

class AccountController(BaseController):

    def signin(self):
        if not request.environ.get('REMOTE_USER'):
            # This triggers the AuthKit middleware into displaying the sign-in form
            abort(401)
        else:
            return render('/derived/account/signedin.html')

    def signout(self):
        # The actual removal of the AuthKit cookie occurs when the response passes
        # through the AuthKit middleware, we simply need to display a page
        # confirming the user is signed out
        return render('/derived/account/signedout.html')
    
