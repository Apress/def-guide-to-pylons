from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1225985933.0788651
_template_filename='/media/disk/Pylons Book/Code/chapter14/SimpleSite19/SimpleSite/simplesite/templates/derived/tag/fields.html'
_template_uri='/derived/tag/fields.html'
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
    "Name",
    h.text(name='name'),
    required=True,
)))
        # SOURCE LINE 5
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


