from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1226159743.5289071
_template_filename='/media/disk/Pylons Book/Code/chapter19/SimpleSite40/SimpleSite/simplesite/templates/base/index.html'
_template_uri='/base/index.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head', 'flash', 'title', 'tabs', 'menu', 'footer', 'js', 'header', 'breadcrumbs', 'heading']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace('navigation', context._clean_inheritance_tokens(), templateuri='/component/navigation.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, 'navigation')] = ns

def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'navigation')._populate(_import_ns, ['*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        self = _import_ns.get('self', context.get('self', UNDEFINED))
        request = _import_ns.get('request', context.get('request', UNDEFINED))
        next = _import_ns.get('next', context.get('next', UNDEFINED))
        __M_writer = context.writer()
        __M_writer(u'')
        # SOURCE LINE 3
        __M_writer(u'\n<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"\n"http://www.w3.org/TR/html4/strict.dtd">\n<html>\n<head>\n    <title>')
        # SOURCE LINE 8
        __M_writer(escape(self.title()))
        __M_writer(u'</title>\n    ')
        # SOURCE LINE 9
        __M_writer(escape(self.head()))
        __M_writer(u'\n    ')
        # SOURCE LINE 10
        __M_writer(escape(self.js()))
        __M_writer(u'\n</head>\n<body>\n    <div id="doc3" class="yui-t5">\n        <div id="hd">\n            <div class="yui-gc">\n                <div class="yui-u first">')
        # SOURCE LINE 16
        __M_writer(escape(self.heading()))
        __M_writer(u'</div>\n                    <div class="yui-u">\n')
        # SOURCE LINE 18
        if h.auth.authorized(h.auth.is_valid_user) and not (request.urlvars['controller'] == 'account' and request.urlvars['action'] == 'signout'):
            # SOURCE LINE 19
            __M_writer(u'                        <p>Signed in as ')
            __M_writer(escape(request.environ['REMOTE_USER']))
            __M_writer(u',\n                            <a href="')
            # SOURCE LINE 20
            __M_writer(escape(h.url_for('signout')))
            __M_writer(u'">Sign out</a></p>\n')
            # SOURCE LINE 21
        else:
            # SOURCE LINE 22
            __M_writer(u'                        <p><a href="')
            __M_writer(escape(h.url_for('signin')))
            __M_writer(u'">Sign in</a></p>\n')
        # SOURCE LINE 24
        __M_writer(u'                    </div>\n            </div>\n            ')
        # SOURCE LINE 26
        __M_writer(escape(self.header()))
        __M_writer(u'\n            ')
        # SOURCE LINE 27
        __M_writer(escape(self.tabs()))
        __M_writer(u'\n        </div>\n        <div id="bd">\n            <div id="yui-main">\n                <div class="yui-b">\n                    ')
        # SOURCE LINE 32
        __M_writer(escape(self.breadcrumbs()))
        __M_writer(u'\n                    ')
        # SOURCE LINE 33
        __M_writer(escape(self.flash()))
        __M_writer(u'\n                    ')
        # SOURCE LINE 34
        __M_writer(escape(next.body()))
        __M_writer(u'\n                </div>\n            </div>\n            <div class="yui-b">\n                ')
        # SOURCE LINE 38
        __M_writer(escape(self.menu()))
        __M_writer(u'\n            </div>\n        </div>\n        <div id="ft">\n            ')
        # SOURCE LINE 42
        __M_writer(escape(self.footer()))
        __M_writer(u'\n        </div>\n    </div>\n</body>\n</html>\n\n')
        # SOURCE LINE 48
        __M_writer(u'\n')
        # SOURCE LINE 52
        __M_writer(u'\n')
        # SOURCE LINE 53
        __M_writer(u'\n')
        # SOURCE LINE 54
        __M_writer(u'\n')
        # SOURCE LINE 55
        __M_writer(u'\n')
        # SOURCE LINE 56
        __M_writer(u'\n')
        # SOURCE LINE 57
        __M_writer(u'\n')
        # SOURCE LINE 63
        __M_writer(u'\n')
        # SOURCE LINE 72
        __M_writer(u'\n')
        # SOURCE LINE 73
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'navigation')._populate(_import_ns, ['*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 49
        __M_writer(u'\n    ')
        # SOURCE LINE 50
        __M_writer(escape(h.stylesheet_link(h.url_for('/yui/2.6.0/reset-fonts-grids/reset-fonts-grids.css'))))
        __M_writer(u'\n    ')
        # SOURCE LINE 51
        __M_writer(escape(h.stylesheet_link(h.url_for('/css/main.css'))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_flash(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'navigation')._populate(_import_ns, ['*'])
        session = _import_ns.get('session', context.get('session', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 64
        __M_writer(u'\n')
        # SOURCE LINE 65
        if session.has_key('flash'):
            # SOURCE LINE 66
            __M_writer(u'    <div id="flash"><p>')
            __M_writer(escape(session.get('flash')))
            __M_writer(u'</p></div>\n    ')
            # SOURCE LINE 67

            del session['flash']
            session.save()
                
            
            # SOURCE LINE 70
            __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'navigation')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        # SOURCE LINE 48
        __M_writer(u'SimpleSite')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tabs(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'navigation')._populate(_import_ns, ['*'])
        navigation = _mako_get_namespace(context, 'navigation')
        __M_writer = context.writer()
        # SOURCE LINE 54
        __M_writer(escape(navigation.tabs()))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'navigation')._populate(_import_ns, ['*'])
        navigation = _mako_get_namespace(context, 'navigation')
        __M_writer = context.writer()
        # SOURCE LINE 55
        __M_writer(escape(navigation.menu()))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'navigation')._populate(_import_ns, ['*'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 58
        __M_writer(u'\n    <p>\n        <a href="')
        # SOURCE LINE 60
        __M_writer(escape(h.url_for('/')))
        __M_writer(u'">[Home]</a> |\n        <a href="#top">Top ^</a>\n    </p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'navigation')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'navigation')._populate(_import_ns, ['*'])
        __M_writer = context.writer()
        # SOURCE LINE 53
        __M_writer(u'<a name="top"></a>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumbs(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'navigation')._populate(_import_ns, ['*'])
        navigation = _mako_get_namespace(context, 'navigation')
        __M_writer = context.writer()
        # SOURCE LINE 57
        __M_writer(escape(navigation.breadcrumbs()))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'navigation')._populate(_import_ns, ['*'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 56
        __M_writer(u'<h1>')
        __M_writer(escape(c.heading or 'No Title'))
        __M_writer(u'</h1>')
        return ''
    finally:
        context.caller_stack._pop_frame()


