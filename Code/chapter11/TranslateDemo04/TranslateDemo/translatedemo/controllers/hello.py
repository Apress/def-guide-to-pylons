import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from translatedemo.lib.base import BaseController, render
#from translatedemo import model

from pylons.i18n.translation import _, set_lang
from pylons.i18n.translation import get_lang


log = logging.getLogger(__name__)

class HelloController(BaseController):

    def index(self):
        set_lang('es')
        return _(u'Goodbye!')

    def multiple(self):
        resp = 'Default: %s<br />' % _(u'Hello!')
        for lang in ['fr','en','es']:
            set_lang(lang)
            resp += '%s: %s<br />' % (get_lang(), _(u'Hello!'))
        return resp

