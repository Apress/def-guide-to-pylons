from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224608024.114131
_template_filename='/home/james/Desktop/Pylons Book/Code/chapter05/TemplateDemo/templatedemo/templates/section.html'
_template_uri='/section.html'
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
    # SOURCE LINE 2
    ns = runtime.Namespace('__anon_0x894946c', context._clean_inheritance_tokens(), templateuri='/navigation.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, '__anon_0x894946c')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x894946c')._populate(_import_ns, ['navigation_links'])
        navigation_links = _import_ns.get('navigation_links', context.get('navigation_links', UNDEFINED))
        next = _import_ns.get('next', context.get('next', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 4
        __M_writer(escape(navigation_links('Admin Home', links=[
    ('Admin Home', '/admin'),
    ('Settings', '/admin/settings'),
    ('Sign Out', '/admin/signout'),
])))
        # SOURCE LINE 8
        __M_writer(u'\n\n')
        # SOURCE LINE 10
        __M_writer(escape(next.body()))
        __M_writer(u'\n\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, '__anon_0x894946c')._populate(_import_ns, ['navigation_links'])
        __M_writer = context.writer()
        # SOURCE LINE 12
        __M_writer(u'User Administration')
        return ''
    finally:
        context.caller_stack._pop_frame()


