import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from authdemo.lib.base import BaseController, render
#from authdemo import model

log = logging.getLogger(__name__)

class AuthController(BaseController):

    def private(self):
        response.status = "401 Not authenticated"
        return "You are not authenticated"

