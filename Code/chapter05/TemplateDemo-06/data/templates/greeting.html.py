from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224603551.9597671
_template_filename='/home/james/Desktop/Pylons Book/Code/chapter05/TemplateDemo/templatedemo/templates/greeting.html'
_template_uri='/greeting.html'
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
    ns = runtime.Namespace('nav', context._clean_inheritance_tokens(), templateuri='/navigation.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, 'nav')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        c = context.get('c', UNDEFINED)
        nav = _mako_get_namespace(context, 'nav')
        __M_writer = context.writer()
        __M_writer(u'\n\n<html>\n<head>\n    <title>Greetings</title>\n</head>\n<body>\n    <h1>Greetings</h1>\n\n    ')
        # SOURCE LINE 10
        __M_writer(escape(nav.navigation_links('Ben', links=[
        ('James','http://jimmyg.org'),
        ('Ben','http://groovie.org'),
        ('Philip',''),
    ])))
        # SOURCE LINE 14
        __M_writer(u'\n\n    <p>')
        # SOURCE LINE 16
        __M_writer(escape(c.greeting))
        __M_writer(u' ')
        __M_writer(escape(c.name))
        __M_writer(u'!</p>\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


