"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons.templating import render_mako as render

from customobjects.model import meta

class BaseController(WSGIController):

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']

        class CustomCacheObj: pass

        # Add the custom cache object
        if 'paste.testing_variables' in environ:
            environ['paste.testing_variables']['cache'] = CustomCacheObj()
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            meta.Session.remove()
        
