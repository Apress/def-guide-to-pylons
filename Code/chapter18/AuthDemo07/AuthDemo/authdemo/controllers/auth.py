import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from authdemo.lib.base import BaseController, render
#from authdemo import model

from authkit.authorize.pylons_adaptors import authorize
from authkit.permissions import RemoteUser, ValidAuthKitUser, UserIn
from authkit.authorize.pylons_adaptors import authorized

log = logging.getLogger(__name__)

class AuthController(BaseController):

    @authorize(UserIn("visitor"))
    def private(self):
        return "You are authenticated!"

    def signout(self):
        return "Successfully signed out!"

    def public(self):
        if authorized(UserIn(["visitor"])):
            return "You are authenticated!"
        else:
            from authkit.permissions import NotAuthenticatedError
            raise NotAuthenticatedError("You are not signed in!")

