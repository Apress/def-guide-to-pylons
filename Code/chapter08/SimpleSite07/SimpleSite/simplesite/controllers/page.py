import logging

from pylons import request, response, session, tmpl_context as c
from pylons.controllers.util import abort, redirect_to

from simplesite.lib.base import BaseController, render
from simplesite import model

import simplesite.model.meta as meta
import simplesite.lib.helpers as h

import formencode
from formencode import htmlfill
from pylons.decorators import validate
from pylons.decorators.rest import restrict

log = logging.getLogger(__name__)

class NewPageForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    content = formencode.validators.String(
        not_empty=True,
        messages={
            'empty':'Please enter some content for the page.'
        }
    )
    heading = formencode.validators.String()
    title = formencode.validators.String(not_empty=True)


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

    @restrict('POST')
    @validate(schema=NewPageForm(), form='new')
    def create(self):
        # Add the new page to the database
        page = model.Page()
        for k, v in self.form_result.items():
            setattr(page, k, v)
        meta.Session.add(page)
        meta.Session.commit()
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='page',
            action='view', id=page.id)
        return "Moved temporarily"

