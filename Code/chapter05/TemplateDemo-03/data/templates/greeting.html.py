from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224597818.793782
_template_filename='/home/james/Desktop/Pylons Book/Code/chapter05/TemplateDemo/templatedemo/templates/greeting.html'
_template_uri='/greeting.html'
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
        __M_writer(u'<html>\n<head>\n    <title>Greetings</title>\n</head>\n<body>\n    <h1>Greetings</h1>\n    <p>Hello ')
        # SOURCE LINE 7
        __M_writer(escape(c.name))
        __M_writer(u'!</p>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


