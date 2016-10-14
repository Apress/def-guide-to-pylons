import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from logtest.lib.base import BaseController, render
#from logtest import model

log = logging.getLogger(__name__)
other_log = logging.getLogger('logtest.controllers.log.other')

class LogController(BaseController):

    def index(self):
        authkit_log = logging.getLogger('authkit')
        authkit_log.info('A message logged to the authkit logger')
        return 'Check the logs!'

    def newlog(self, action):
        log.log(10, 'Another log message')
        return 'Check the logs again!'

    def template(self):
        return render('/log.html')

    def wsgi_errors(self):
        request.environ['wsgi.errors'].write(
            'This is sent directly to the wsgi.errors stream')
        return 'Message logged to wsgi.errors'

