"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons.templating import render_mako as render

from pylons.i18n.translation import set_lang
from pylons import session
from pylons.i18n.translation import add_fallback

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']

        add_fallback('es')
        if 'lang' in session:
            set_lang(session['lang'])

        return WSGIController.__call__(self, environ, start_response)

