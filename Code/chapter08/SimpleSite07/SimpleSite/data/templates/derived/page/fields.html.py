from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1225670336.1138239
_template_filename='/media/disk/Pylons Book/Code/chapter08/SimpleSite06/SimpleSite/simplesite/templates/derived/page/fields.html'
_template_uri='/derived/page/fields.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(escape(h.field(
    "Heading",
    h.text(name='heading'),
    required=False,
)))
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(escape(h.field(
    "Title",
    h.text(name='title'),
    required=True,
    field_desc = "Used as the heading too if you didn't specify one above"
)))
        # SOURCE LINE 11
        __M_writer(u'\n')
        # SOURCE LINE 12
        __M_writer(escape(h.field(
    "Content",
    h.textarea(name='content', rows=7, cols=40),
    required=True,
    field_desc = 'The text that will make up the body of the page'
)))
        # SOURCE LINE 17
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


