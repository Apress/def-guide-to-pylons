from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1225994608.6425691
_template_filename='/media/disk/Pylons Book/Code/chapter14/SimpleSite23/SimpleSite/simplesite/templates/derived/nav/fields.html'
_template_uri='/derived/nav/fields.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(escape(h.field(
    "Name",
    h.text(name='name'),
    required=True,
)))
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(escape(h.field(
    "Path",
    h.text(name='path'),
    required=True,
)))
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 11
        __M_writer(escape(h.field(
    'Section',
    h.select(
        "section",
        id='section',
        selected_values=[],
        options=c.available_sections,
    ),
    required=True
)))
        # SOURCE LINE 20
        __M_writer(u'\n')
        # SOURCE LINE 21
        __M_writer(escape(h.field(
    "Before",
    h.text(
    "before",
    id='before',
    ),
)))
        # SOURCE LINE 27
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


