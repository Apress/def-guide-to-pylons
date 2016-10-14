from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224601926.3499179
_template_filename='/home/james/Desktop/Pylons Book/Code/chapter05/TemplateDemo/templatedemo/templates/filters.html'
_template_uri='/filters.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(filters.html_entities_escape(filters.trim(escape( c.test1 ))))
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer( c.test2 )
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


