from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224670329.103487
_template_filename='/media/disk/Pylons Book/Code/chapter06/FormDemo/formdemo/templates/base.html'
_template_uri='/base.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n<title>FormDemo</title>\n<link rel="stylesheet" type="text/css"\n    href="')
        # SOURCE LINE 5
        __M_writer(escape(h.url_for('/style/style.css')))
        __M_writer(u'" />\n</head>\n<body>\n')
        # SOURCE LINE 8
        __M_writer(escape(next.body()))
        __M_writer(u'\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


