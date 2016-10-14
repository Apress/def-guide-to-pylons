from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224625788.643194
_template_filename='/home/james/Desktop/Pylons Book/Code/chapter06/FormDemo-01/formdemo/templates/simpleform.html'
_template_uri='/simpleform.html'
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
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/base.html', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n<h1>Enter Your E-mail Address</h1>\n\n<form name="test" method="post" action="/formtest/submit">\nE-mail Address: <input type="text" name="email" />\n               <input type="submit" name="submit" value="Submit" />\n</form>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


