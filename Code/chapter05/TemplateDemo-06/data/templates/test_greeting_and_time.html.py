from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224603865.0170629
_template_filename='/home/james/Desktop/Pylons Book/Code/chapter05/TemplateDemo-06/templatedemo/templates/test_greeting_and_time.html'
_template_uri='/test_greeting_and_time.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 1
    ns = runtime.Namespace('other', context._clean_inheritance_tokens(), templateuri='/greeting_and_time.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, 'other')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        other = _mako_get_namespace(context, 'other')
        __M_writer = context.writer()
        __M_writer(u'\n\nThe greeting is ')
        # SOURCE LINE 3
        __M_writer(escape(other.test()))
        __M_writer(u'\nThe time is ')
        # SOURCE LINE 4
        __M_writer(filters.trim(escape(other.body() )))
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


