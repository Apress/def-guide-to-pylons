from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1226063041.7341139
_template_filename='/media/disk/Pylons Book/Code/chapter15/SimpleSite32/SimpleSite/simplesite/templates/derived/nav/fields.html'
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
            h.url_for(controller="nav", action="before_field_json")
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
        # SOURCE LINE 66
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_js(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n    <script src="/yui/2.6.0/yahoo-dom-event/yahoo-dom-event.js" type="text/javascript"></script>\n    <script src="/yui/2.6.0/connection/connection-min.js" type="text/javascript"></script>\n    <script src="/yui/2.6.0/json/json-min.js" type="text/javascript"></script>\n\n    <script type="text/javascript">\n    function callAjax(url, field, replace){\n        var callback = {\n            success: function(o) {\n                var parsed_options = YAHOO.lang.JSON.parse(o.responseText);\n                var before = document.getElementById(replace);\n                // Remove current options\n                while(before.hasChildNodes() === true)\n                {\n                    before.removeChild(before.childNodes[0]);\n                }\n                // Add new options\n                for (var i=0; i<parsed_options.options.length; i++) {\n                    var new_option = document.createElement(\'option\');\n                    new_option.text = parsed_options.options[i].id;\n                    new_option.value = parsed_options.options[i].value;\n                    before.appendChild(new_option);\n                }\n            },\n            failure: function(o) {\n                alert("Failed to retrieve required information.");\n            }\n        }\n        url = url +\'?selected=\'+YAHOO.util.Dom.get(field).value;\n        var transaction=YAHOO.util.Connect.asyncRequest(\'GET\', url, callback, null);\n    }\n    </script>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


