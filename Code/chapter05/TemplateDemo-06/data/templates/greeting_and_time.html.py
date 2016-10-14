from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224603779.0558369
_template_filename='/home/james/Desktop/Pylons Book/Code/chapter05/TemplateDemo-06/templatedemo/templates/greeting_and_time.html'
_template_uri='/greeting_and_time.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['test']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n12:00pm\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_test(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'Hello World!')
        return ''
    finally:
        context.caller_stack._pop_frame()


