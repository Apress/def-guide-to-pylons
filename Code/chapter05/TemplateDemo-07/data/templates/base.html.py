from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224604366.9716029
_template_filename='/home/james/Desktop/Pylons Book/Code/chapter05/TemplateDemo/templatedemo/templates/base.html'
_template_uri='/base.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n    <head>\n        <title>')
        # SOURCE LINE 3
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n    </head>\n    <body>\n        ')
        # SOURCE LINE 6
        __M_writer(escape(self.body()))
        __M_writer(u'\n        <div class="footer">\n            <p>This is a simple page footer</p>\n        </div>\n    </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


