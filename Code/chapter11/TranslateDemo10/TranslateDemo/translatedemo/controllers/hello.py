import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from translatedemo.lib.base import BaseController, render
#from translatedemo import model

from pylons.i18n.translation import _, set_lang
from pylons.i18n.translation import get_lang


log = logging.getLogger(__name__)

class HelloController(BaseController):

    def signin(self):
        # Place your sign in code here
        # Replace this with code to set the language for the signed in user
        session['lang'] = request.params.getone('lang')
        session.save()
        return 'Signed in, language set to %s.'%request.params.getone('lang')

    def index(self):
        return _(u'Goodbye!')

    def multiple(self):
        return render('/hello.html')


