from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1226162194.679441
_template_filename='/media/disk/Pylons Book/Code/chapter19/SimpleSite42/SimpleSite/simplesite/templates/derived/page/edit.html'
_template_uri='/derived/page/edit.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['head', 'heading', 'js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    # SOURCE LINE 2
    ns = runtime.Namespace('fields', context._clean_inheritance_tokens(), templateuri='fields.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, 'fields')] = ns

    # SOURCE LINE 15
    ns = runtime.Namespace('navfields', context._clean_inheritance_tokens(), templateuri='/derived/nav/fields.html', callables=None, calling_uri=_template_uri, module=None)
    context.namespaces[(__name__, 'navfields')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base/index.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'fields')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'navfields')._populate(_import_ns, ['js'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        request = _import_ns.get('request', context.get('request', UNDEFINED))
        fields = _mako_get_namespace(context, 'fields')
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        __M_writer(u'\n\n<p>Editing the source code for the ')
        # SOURCE LINE 8
        __M_writer(escape(c.title))
        __M_writer(u' page:</p>\n')
        # SOURCE LINE 9
        __M_writer(escape(h.form_start(h.url_for(controller='page', action='save',
    id=request.urlvars['id']), method="post")))
        # SOURCE LINE 10
        __M_writer(u'\n    ')
        # SOURCE LINE 11
        __M_writer(escape(fields.body()))
        __M_writer(u'\n    ')
        # SOURCE LINE 12
        __M_writer(escape(h.field(field=h.submit(value="Save Changes", name='submit'))))
        __M_writer(u'\n')
        # SOURCE LINE 13
        __M_writer(escape(h.form_end()))
        __M_writer(u'\n\n')
        # SOURCE LINE 15
        __M_writer(u'\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n')
        # SOURCE LINE 56
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_head(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'fields')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'navfields')._populate(_import_ns, ['js'])
        h = _import_ns.get('h', context.get('h', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 53
        __M_writer(u'\n    ')
        # SOURCE LINE 54
        __M_writer(escape(parent.head()))
        __M_writer(u'\n    ')
        # SOURCE LINE 55
        __M_writer(escape(h.stylesheet_link(h.url_for('/yui/2.6.0/assets/skins/sam/skin.css'))))
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_heading(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'fields')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'navfields')._populate(_import_ns, ['js'])
        c = _import_ns.get('c', context.get('c', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    <h1 class="main">Editing ')
        # SOURCE LINE 5
        __M_writer(escape(c.title))
        __M_writer(u'</h1>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context):
    context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'fields')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'navfields')._populate(_import_ns, ['js'])
        navfields = _mako_get_namespace(context, 'navfields')
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        # SOURCE LINE 17
        __M_writer(u'\n    ')
        # SOURCE LINE 18
        __M_writer(escape(parent.js()))
        __M_writer(u'\n    ')
        # SOURCE LINE 19
        __M_writer(escape(navfields.js()))
        __M_writer(u'\n\n    <script type="text/javascript"\n        src="/yui/2.6.0/element/element-beta-min.js"></script>\n    <script type="text/javascript"\n        src="/yui/2.6.0/container/container_core-min.js"></script>\n    <script type="text/javascript"\n        src="/yui/2.6.0/editor/simpleeditor-min.js"></script>\n\n    <script type="text/javascript">\n    (function() {\n        // Set up some private variables\n        var Dom = YAHOO.util.Dom;\n        var Event = YAHOO.util.Event;\n\n        // The SimpleEditor config\n        var myConfig = {\n            height: \'200px\',\n            width: \'630px\',\n            dompath: true,\n            focusAtStart: true,\n            handleSubmit: true\n        };\n\n        // Now let\'s load the SimpleEditor..\n        var myEditor = new YAHOO.widget.SimpleEditor(\'editor\', myConfig);\n        myEditor._defaultToolbar.buttonType = \'advanced\';\n        document.e = myEditor;\n        myEditor._defaultToolbar.titlebar = \'Rich Text Editor\';\n        myEditor.render();\n    })();\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


