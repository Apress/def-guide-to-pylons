import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from authdemo.lib.base import BaseController, render
#from authdemo import model

from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import RemoteUser, ValidAuthKitUser, UserIn

log = logging.getLogger(__name__)

class AuthController(BaseController):

    @authorize(UserIn("visitor"))
    def private(self):
        return "You are authenticated!"

    def signout(self):
        return "Successfully signed out!"

    def public(self):
        return "This is still only visible when you are signed in."

