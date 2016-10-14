import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from authdemo.lib.base import BaseController, render
#from authdemo import model

log = logging.getLogger(__name__)

class AuthController(BaseController):

    def private(self):
        if request.environ.get("REMOTE_USER"):
            return "You are authenticated!"
        else:
            response.status = "401 Not authenticated"
            return "You are not authenticated"

    def signout(self):
        return "Successfully signed out!"

