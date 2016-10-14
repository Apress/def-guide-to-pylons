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

from simplesite.controllers.nav import NewNavForm, ValidBefore

class UniqueSectionPath(formencode.validators.FancyValidator):
    "Checks that there isn't already an existing section with the same path"
    def _to_python(self, values, state):
        nav_q = meta.Session.query(model.Nav)
        query = nav_q.filter_by(section=values['section'],
            type='section', path=values['path'])
        if request.urlvars['action'] == 'save':
            # Ignore the existing ID when performing the check
            query = query.filter(model.Nav.id != int(request.urlvars['id']))
        existing = query.first()
        if existing is not None:
            raise formencode.Invalid("There is already a section in this "
                "section with this path", values, state)
        return values

class NewSectionForm(NewNavForm):
    chained_validators = [ValidBefore(), UniqueSectionPath()]

class ValidSectionPosition(formencode.FancyValidator):
    def _to_python(self, values, state):
        nav_q = meta.Session.query(model.Nav)
        if values.get('type', 'section') == 'section':
            # Make sure the section we are moving to is not already
            # a subsection of the current section
            section = nav_q.filter_by(id=int(values['section'])).one()
            current_section = nav_q.filter_by(id=request.urlvars['id']).one()
            while section:
                if section.section == current_section.id:
                    raise formencode.Invalid("You cannot move a section to "
                        "one of its subsections", values, state)
                if section.section == 1:
                    break
                section = nav_q.filter_by(id=section.section).first()
            return values

class EditSectionForm(NewNavForm):
    chained_validators = [
        ValidBefore(),
        UniqueSectionPath(),
        ValidSectionPosition()
    ]

class SectionController(BaseController):

    def __before__(self, id=None):
        nav_q = meta.Session.query(model.Nav)
        if id:
            nav_q=nav_q.filter_by(type='section').filter(model.nav_table.c.id!=int(id))
        else:
            nav_q = nav_q.filter_by(type='section')
        c.available_sections = [(nav.id, nav.name) for nav in nav_q]


    def view(self, id=None):
        if id is None:
            abort(404)
        section_q = meta.Session.query(model.Section)
        c.section = section_q.get(int(id))
        if c.section is None:
            abort(404)
        return render('/derived/section/view.html')

    def new(self):
        return render('/derived/section/new.html')

    @restrict('POST')
    @validate(schema=NewSectionForm(), form='new')
    def create(self):
        # Add the new section to the database
        section = model.Section()
        for k, v in self.form_result.items():
            setattr(section, k, v)
        meta.Session.add(section)
        meta.Session.commit()
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='section',
            action='view', id=section.id)
        return "Moved temporarily"

    def edit(self, id=None):
        if id is None:
            abort(404)
        section_q = meta.Session.query(model.Section)
        section = section_q.filter_by(id=id).first()
        if section is None:
            abort(404)
        values = {
            'title': section.title,
            'heading': section.heading,
            'content': section.content
        }
        return htmlfill.render(render('/derived/section/edit.html'), values)

    @restrict('POST')
    @validate(schema=NewSectionForm(), form='edit')
    def save(self, id=None):
        section_q = meta.Session.query(model.Section)
        section = section_q.filter_by(id=id).first()
        if section is None:
            abort(404)
        for k,v in self.form_result.items():
            if getattr(section, k) != v:
                setattr(section, k, v)
        meta.Session.commit()
        session['flash'] = 'Section successfully updated.'
        session.save()
        # Issue an HTTP redirect
        response.status_int = 302
        response.headers['location'] = h.url_for(controller='section', action='view',
            id=section.id)
        return "Moved temporarily"

    def list(self):
        section_q = meta.Session.query(model.Section)
        c.paginator = paginate.Page(
            section_q,
            page=int(request.params.get('page', 1)),
            items_per_page = 2,
            controller='section',
            action='list',
        )
        return render('/derived/section/list.html')

    def delete(self, id=None):
        if id is None:
            abort(404)
        section_q = meta.Session.query(model.Section)
        section = section_q.filter_by(id=id).first()
        if section is None:
            abort(404)
        meta.Session.delete(section)
        meta.Session.commit()
        return render('/derived/section/deleted.html')

