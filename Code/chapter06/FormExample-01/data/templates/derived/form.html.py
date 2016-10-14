from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224684001.22454
_template_filename='/media/disk/Pylons Book/Code/chapter06/FormExample-01/formexample/templates/derived/form.html'
_template_uri='/derived/form.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['person', 'study']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        def study():
            return render_study(context.locals_(__M_locals))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 19
        __M_writer(u'\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n<h1>Create a Study</h1>\n\n')
        # SOURCE LINE 55
        __M_writer(escape(h.form(h.url_for(controller='study', action='process'))))
        __M_writer(u'\n')
        # SOURCE LINE 56
        __M_writer(escape(study()))
        __M_writer(u'\n')
        # SOURCE LINE 57
        __M_writer(escape(h.submit(name="action", value="Save")))
        __M_writer(u'\n')
        # SOURCE LINE 58
        __M_writer(escape(h.submit(name="action", value="Add New Person")))
        __M_writer(u'\n')
        # SOURCE LINE 59
        __M_writer(escape(h.end_form()))
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_person(context,id):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 21
        __M_writer(u'\n    <fieldset><legend>Person</legend>\n\n        <label for="person-')
        # SOURCE LINE 24
        __M_writer(escape(id))
        __M_writer(u'.title">Title</label><br />\n        ')
        # SOURCE LINE 25
        __M_writer(escape(h.text(name="person-%s.title"%(id), id="person-%s.title"%(id))))
        __M_writer(u'<br />\n\n        <label for="person-')
        # SOURCE LINE 27
        __M_writer(escape(id))
        __M_writer(u'.firstname">First Name</label><br />\n        ')
        # SOURCE LINE 28
        __M_writer(escape(h.text(
            name="person-%s.firstname"%(id),
            id="person-%s.firstname"%(id
        ))))
        # SOURCE LINE 31
        __M_writer(u'<br />\n\n        <label for="person-')
        # SOURCE LINE 33
        __M_writer(escape(id))
        __M_writer(u'.surname">Surname</label><br />\n        ')
        # SOURCE LINE 34
        __M_writer(escape(h.text(name="person-%s.surname"%(id), id="person-%s.surname"%(id))))
        __M_writer(u'<br />\n\n        <label for="person-')
        # SOURCE LINE 36
        __M_writer(escape(id))
        __M_writer(u'.role">Role</label><br />\n        ')
        # SOURCE LINE 37
        __M_writer(escape(h.select(
            "person-%s.role"%(id),
            [],
            [
                ['1', 'Chief Investigator'],
                ['2', 'Assistant'],
                ['3', 'Student'],
            ],
            id="person-%s.role"%(id),
        )))
        # SOURCE LINE 46
        __M_writer(u'<br />\n\n        ')
        # SOURCE LINE 48
        __M_writer(escape(h.submit(name="action", value="Remove %s"%(id))))
        __M_writer(u'\n\n    </fieldset><br />\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_study(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        range = context.get('range', UNDEFINED)
        c = context.get('c', UNDEFINED)
        def person(id):
            return render_person(context,id)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <fieldset><legend>Study</legend>\n\n        <label for="title">Title</label><br />\n        ')
        # SOURCE LINE 7
        __M_writer(escape(h.text(name="title", id="title")))
        __M_writer(u'<br />\n\n        <label for="start_date">Start Date</label><br />\n        ')
        # SOURCE LINE 10
        __M_writer(escape(h.text(name="start_date", id="startdate")))
        __M_writer(u'<br />\n\n        <label for="end_date">End Date</label><br />\n        ')
        # SOURCE LINE 13
        __M_writer(escape(h.text(name="end_date", id="enddate")))
        __M_writer(u'<br />\n\n    </fieldset><br />\n')
        # SOURCE LINE 16
        for id in range(c.number_of_people):
            # SOURCE LINE 17
            __M_writer(u'            ')
            __M_writer(escape(person(id=id)))
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


