import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from simplesite.lib.base import BaseController, render
from simplesite import model

import simplesite.model.meta as meta
import simplesite.lib.helpers as h

log = logging.getLogger(__name__)

class PageController(BaseController):

    def view(self, id):
        page_q = model.meta.Session.query(model.Page)
        c.page = page_q.get(int(id))
        return render('/derived/page/view.html')
