from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1225734753.5587299
_template_filename='/media/disk/Pylons Book/Code/chapter11/TranslateDemo05/TranslateDemo/translatedemo/templates/hello.html'
_template_uri='/hello.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


# SOURCE LINE 1

from pylons.i18n.translation import set_lang, get_lang


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _ = context.get('_', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n<html>\n<head>\n    <title>Multiple Translations</title>\n</head>\n<body>\n    <h1>Multiple Translations</h1>\n    <p>\n        Default: ')
        # SOURCE LINE 11
        __M_writer(escape(_(u'Hello!')))
        __M_writer(u'<br />\n')
        # SOURCE LINE 12
        for lang in ['fr','en','es']:
            # SOURCE LINE 13
            __M_writer(u'            ')
            set_lang(lang) 
            
            __M_writer(u'\n            ')
            # SOURCE LINE 14
            __M_writer(escape(get_lang()))
            __M_writer(u': ')
            __M_writer(escape(_(u'Hello!')))
            __M_writer(u'<br />\n')
        # SOURCE LINE 16
        __M_writer(u'    </p>\n</body>\n</html>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


