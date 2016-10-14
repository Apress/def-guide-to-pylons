import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from translatedemo.lib.base import BaseController, render
#from translatedemo import model

from pylons.i18n.translation import _, set_lang
from pylons.i18n.translation import get_lang
from pylons.i18n.translation import ungettext


log = logging.getLogger(__name__)

from pylons.i18n import get_lang, lazy_ugettext, set_lang

set_lang('en')
text = lazy_ugettext(u'Hello!')

class HelloController(BaseController):

    def plural(self):
        n = int(request.params.get('n', 1))
        translated_string = ungettext(
            u'There is %(num)d person here',
            u'There are %(num)d people here',
            n
        )
        final_string = translated_string % {'num': n}
        return final_string
        
    def lazy(self):
        resp = ''
        for lang in ['fr','en','es']:
            set_lang(lang)
            resp += u'%s: %s<br />' % (get_lang(), _(u'Hello!'))
        resp += u'Text: %s<br />' % text
        return resp

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


