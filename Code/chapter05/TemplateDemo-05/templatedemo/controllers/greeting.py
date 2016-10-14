# -*- coding: utf-8 -*-

import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from templatedemo.lib.base import BaseController, render
#from templatedemo import model

log = logging.getLogger(__name__)

import templatedemo.lib.helpers as h

class GreetingController(BaseController):

    def index(self):
        c.greeting = h.literal('<b>Welcome</b>')
        c.name = request.params.get('name', 'Visitor')
        return render('/greeting.html')

    def basic(self):
        return render('/basic.html')

    def context(self):
        return render('/context.html')

    def filters(self):
        c.test1 = u"   It will cost £5    "
        c.test2 = u'<b>Hello</b>'
        return render('/filters.html')

