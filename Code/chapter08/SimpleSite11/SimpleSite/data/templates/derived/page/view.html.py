from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1225708873.919651
_template_filename='/media/disk/Pylons Book/Code/chapter08/SimpleSite10/SimpleSite/simplesite/templates/derived/page/view.html'
_template_uri='/derived/page/view.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['footer', 'heading', 'title']


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
    return runtime._inherit_from(context, '/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n')
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(escape(c.page.content))
        __M_writer(u'\n\n')
        # SOURCE LINE 20
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 8
        __M_writer(u'\n')
        # SOURCE LINE 10
        __M_writer(u'<p>\n<a href="')
        # SOURCE LINE 11
        __M_writer(escape(h.url_for(controller='page', action='list', id=None)))
        __M_writer(u'">All Pages</a>\n| <a href="')
        # SOURCE LINE 12
        __M_writer(escape(h.url_for(controller='page', action='new', id=None)))
        __M_writer(u'">New Page</a>\n| <a href="')
        # SOURCE LINE 13
        __M_writer(escape(h.url_for(controller='page', action='edit',
      id=c.page.id)))
        # SOURCE LINE 14
        __M_writer(u'">Edit Page</a>\n| <a href="')
        # SOURCE LINE 15
        __M_writer(escape(h.url_for(controller='page', action='delete', 
      id=c.page.id)))
        # SOURCE LINE 16
        __M_writer(u'">Delete Page</a>\n</p>\n')
        # SOURCE LINE 19
        __M_writer(escape(parent.footer()))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'<h1>')
        __M_writer(escape(c.page.heading or c.page.title))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(escape(c.page.title))
        return ''
    finally:
        context.caller_stack._pop_frame()


