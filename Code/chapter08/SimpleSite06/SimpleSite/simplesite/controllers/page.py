import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from simplesite.lib.base import BaseController, render
from simplesite import model

import simplesite.model.meta as meta
import simplesite.lib.helpers as h

log = logging.getLogger(__name__)

class PageController(BaseController):

    def view(self, id=None):
        if id is None:
            abort(404)
        page_q = meta.Session.query(model.Page)
        c.page = page_q.get(int(id))
        if c.page is None:
            abort(404)
        return render('/derived/page/view.html')

    def new(self):
        return render('/derived/page/new.html')
