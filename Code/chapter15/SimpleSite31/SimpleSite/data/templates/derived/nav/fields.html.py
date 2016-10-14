from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1226062019.303221
_template_filename='/media/disk/Pylons Book/Code/chapter15/SimpleSite31/SimpleSite/simplesite/templates/derived/nav/fields.html'
_template_uri='/derived/nav/fields.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['js']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        h = context.get('h', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(escape(h.field(
    "Name",
    h.text(name='name'),
    required=True,
)))
        # SOURCE LINE 5
        __M_writer(u'\n')
        # SOURCE LINE 6
        __M_writer(escape(h.field(
    "Path",
    h.text(name='path'),
    required=True,
)))
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 11
        __M_writer(escape(h.field(
    'Section',
    h.select(
        "section",
        id='section',
        selected_values=[],
        options=c.available_sections,
        onchange="callAjax('%s', 'section', 'before'); return false;"%(
            h.url_for(controller="nav", action="before_field_options")
        ),
    ),
    required=True
)))
        # SOURCE LINE 23
        __M_writer(u'\n')
        # SOURCE LINE 24
        __M_writer(escape(h.field(
    "Before",
    h.select(
        "before",
        id='before',
        options = c.before_options,
        selected_values=[],
    ),
)))
        # SOURCE LINE 32
        __M_writer(u'\n\n')
        # SOURCE LINE 51
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n    <script src="/yui/2.6.0/yahoo-dom-event/yahoo-dom-event.js" type="text/javascript"></script>\n    <script src="/yui/2.6.0/connection/connection-min.js" type="text/javascript"></script>\n    <script type="text/javascript">\n    function callAjax(url, field, replace){\n        var callback = {\n            success: function(o) {\n                YAHOO.util.Dom.get(replace).innerHTML = o.responseText;\n            },\n            failure: function(o) {\n                alert("Failed to retrieve required information.");\n            }\n        }\n        url = url +\'?selected=\'+YAHOO.util.Dom.get(field).value;\n        var transaction=YAHOO.util.Connect.asyncRequest(\'GET\', url, callback, null);\n    }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


