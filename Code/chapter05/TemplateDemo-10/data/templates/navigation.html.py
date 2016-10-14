from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224602465.6067121
_template_filename='/home/james/Desktop/Pylons Book/Code/chapter05/TemplateDemo/templatedemo/templates/navigation.html'
_template_uri='/navigation.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['navigation_links']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def navigation_links(selected,links):
            return render_navigation_links(context.locals_(__M_locals),selected,links)
        __M_writer = context.writer()
        # SOURCE LINE 1

        items = [
            ('James', 'http://jimmyg.org'),
            ('Ben', 'http://groovie.org'),
            ('Philip', ''),
        ]
        
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['items'] if __M_key in __M_locals_builtin()]))
        # SOURCE LINE 7
        __M_writer(u'\n\n')
        # SOURCE LINE 9
        __M_writer(escape(navigation_links('James', items)))
        __M_writer(u'\n\n')
        # SOURCE LINE 31
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_navigation_links(context,selected,links):
    context.caller_stack._push_frame()
    try:
        def link(label,url):
            context.caller_stack._push_frame()
            try:
                __M_writer = context.writer()
                # SOURCE LINE 12
                __M_writer(u'\n')
                # SOURCE LINE 13
                if url:
                    # SOURCE LINE 14
                    __M_writer(u'            <a href="')
                    __M_writer(escape(url))
                    __M_writer(u'">')
                    __M_writer(escape(label))
                    __M_writer(u'</a>\n')
                    # SOURCE LINE 15
                else:
                    # SOURCE LINE 16
                    __M_writer(u'            ')
                    __M_writer(escape(label))
                    __M_writer(u'\n')
                # SOURCE LINE 18
                __M_writer(u'    ')
                return ''
            finally:
                context.caller_stack._pop_frame()
        __M_writer = context.writer()
        # SOURCE LINE 11
        __M_writer(u'\n    ')
        # SOURCE LINE 18
        __M_writer(u'\n\n    <ul>\n')
        # SOURCE LINE 21
        for item in links:
            # SOURCE LINE 22
            __M_writer(u'        <li>')
            # SOURCE LINE 23
            if item[0] == selected:
                # SOURCE LINE 24
                __M_writer(u'        <b>')
                __M_writer(escape(link(item[0], item[1])))
                __M_writer(u'</b>')
                # SOURCE LINE 25
            else:
                # SOURCE LINE 26
                __M_writer(u'        ')
                __M_writer(escape(link(item[0], item[1])))
                __M_writer(u'')
            # SOURCE LINE 28
            __M_writer(u'        </li>\n')
        # SOURCE LINE 30
        __M_writer(u'    </ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


