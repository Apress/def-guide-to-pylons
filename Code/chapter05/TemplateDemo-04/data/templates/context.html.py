from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224599593.1131849
_template_filename='/home/james/Desktop/Pylons Book/Code/chapter05/TemplateDemo/templatedemo/templates/context.html'
_template_uri='/context.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n<body>\n')
        # SOURCE LINE 3

        context.write('<p>Here is an example:</p>')
        
        
        # SOURCE LINE 5
        __M_writer(u'\n<p>\n')
        # SOURCE LINE 7
        for key in context.keys():
            # SOURCE LINE 8
            __M_writer(u'The key is <tt>')
            __M_writer(escape(key))
            __M_writer(u'</tt>, the value is ')
            __M_writer(escape(str(context.get(key))))
            __M_writer(u'. <br />\n')
        # SOURCE LINE 10
        __M_writer(u'</p>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


