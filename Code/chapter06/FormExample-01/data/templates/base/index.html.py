from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224682787.137954
_template_filename='/media/disk/Pylons Book/Code/chapter06/FormExample-01/formexample/templates/base/index.html'
_template_uri='/base/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<head>\n<title>FormsExample</title>\n<style type="text/css">\nspan.error-message{\n    font-weight: bold;\n    color: #c00;\n}\n</style>\n</head>\n<body>\n')
        # SOURCE LINE 12
        __M_writer(escape(next.body()))
        __M_writer(u'\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


