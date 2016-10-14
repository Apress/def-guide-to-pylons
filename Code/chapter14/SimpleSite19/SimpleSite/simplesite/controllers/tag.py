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
import webhelpers.paginate as paginate

log = logging.getLogger(__name__)

class NewTagForm(formencode.Schema):
    allow_extra_fields = True
    filter_extra_fields = True
    name = formencode.validators.String(not_empty=True)

class TagController(BaseController):

    def view(self, id=None):
        if id is None:
            abort(404)
        tag_q = meta.Session.query(model.Tag)
        c.tag = tag_q.get(int(id))
        if c.tag is None:
            abort(404)
        return render('/derived/tag/view.html')

    def new(self):
        return render('/derived/tag/new.html')

    @restrict('POST')
    @validate(schema=NewTagForm(), form='new')
    def create(self):
        # Add the new tag to the database
        tag = model.Tag()
        for k, v in self.form_result.items():
            setattr(tag, k, v)
        meta.Session.add(tag)
        meta.Session.commit()
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='tag',
            action='view', id=tag.id)
        return "Moved temporarily"

    def edit(self, id=None):
        if id is None:
            abort(404)
        tag_q = meta.Session.query(model.Tag)
        tag = tag_q.filter_by(id=id).first()
        if tag is None:
            abort(404)
        values = {
            'name': tag.name,
        }
        return htmlfill.render(render('/derived/tag/edit.html'), values)

    @restrict('POST')
    @validate(schema=NewTagForm(), form='edit')
    def save(self, id=None):
        tag_q = meta.Session.query(model.Tag)
        tag = tag_q.filter_by(id=id).first()
        if tag is None:
            abort(404)
        for k,v in self.form_result.items():
            if getattr(tag, k) != v:
                setattr(tag, k, v)
        meta.Session.commit()
        session['flash'] = 'Tag successfully updated.'
        session.save()
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='tag', action='view',
            id=tag.id)
        return "Moved temporarily"

    def list(self):
        tag_q = meta.Session.query(model.Tag)
        c.paginator = paginate.Page(
            tag_q,
            page=int(request.params.get('page', 1)),
            items_per_page = 10,
            controller='tag',
            action='list'
        )
        return render('/derived/tag/list.html')

    def delete(self, id=None):
        if id is None:
            abort(404)
        tag_q = meta.Session.query(model.Tag)
        tag = tag_q.filter_by(id=id).first()
        if tag is None:
            abort(404)
        meta.Session.delete(tag)
        meta.Session.commit()
        return render('/derived/tag/deleted.html')

