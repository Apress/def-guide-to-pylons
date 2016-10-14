from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224610379.8863089
_template_filename='/home/james/Desktop/Pylons Book/Code/chapter05/TemplateDemo/templatedemo/templates/greeting.html'
_template_uri='/greeting.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['title']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/section.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'')
        # SOURCE LINE 2
        __M_writer(u'\n<h1>Greetings</h1>\n\n<p>')
        # SOURCE LINE 5
        __M_writer(escape(c.greeting))
        __M_writer(u' ')
        __M_writer(escape(c.name))
        __M_writer(u'!</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(escape(parent.title()))
        __M_writer(u' &gt; Greetings')
        return ''
    finally:
        context.caller_stack._pop_frame()


