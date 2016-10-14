from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1224598575.7956259
_template_filename='/home/james/Desktop/Pylons Book/Code/chapter05/TemplateDemo/templatedemo/templates/basic.html'
_template_uri='/basic.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


# SOURCE LINE 69

import datetime


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        pow = context.get('pow', UNDEFINED)
        c = context.get('c', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'The value of 3 + 5 is: ')
        __M_writer(escape(3 + 5))
        __M_writer(u'\nA string representation of 3 to the power 4 is ')
        # SOURCE LINE 2
        __M_writer(escape(pow(3, 4)))
        __M_writer(u'\n\n')
        # SOURCE LINE 5
        __M_writer(u'This will be rendered ## and so will this.\n\n')
        # SOURCE LINE 12
        __M_writer(u'\n\n')
        # SOURCE LINE 14
        __M_writer(u'\n    This is some Mako syntax which will not be executed: ${variable}\n    Neither will this <%doc>be treated as a comment</%doc>\n')
        # SOURCE LINE 17
        __M_writer(u'\n\n')
        # SOURCE LINE 19

        c.name = 'James'
        
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin()]))
        # SOURCE LINE 21
        __M_writer(u'\n\n')
        # SOURCE LINE 23
        if c.name == 'Pylons Developer':
            # SOURCE LINE 24
            __M_writer(u'    Welcome Pylons Developer\n')
            # SOURCE LINE 25
        else:
            # SOURCE LINE 26
            __M_writer(u'    Welcome guest\n')
        # SOURCE LINE 28
        __M_writer(u'\n')
        # SOURCE LINE 29

        c.links = [
            ('James','http://jimmyg.org'),
            ('Ben','http://groovie.org'),
            ('Philip',''),
        ]
        
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in [] if __M_key in __M_locals_builtin()]))
        # SOURCE LINE 35
        __M_writer(u'\n\n<ul>\n')
        # SOURCE LINE 38
        for item in c.links:
            # SOURCE LINE 39
            __M_writer(u'    <li>')
            # SOURCE LINE 40
            if item[1]:
                # SOURCE LINE 41
                __M_writer(u'    <a href="')
                __M_writer(escape(item[1]))
                __M_writer(u'">')
                __M_writer(escape(item[0]))
                __M_writer(u'</a>')
                # SOURCE LINE 42
            else:
                # SOURCE LINE 43
                __M_writer(u'    ')
                __M_writer(escape(item[0]))
                __M_writer(u'')
            # SOURCE LINE 45
            __M_writer(u'    </li>\n')
        # SOURCE LINE 47
        __M_writer(u'</ul>\n\n\n')
        # SOURCE LINE 50

        title = 'Pylons Developer'
        names = [x[0] for x in c.links]
        
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['x','names','title'] if __M_key in __M_locals_builtin()]))
        # SOURCE LINE 53
        __M_writer(u'\n')
        # SOURCE LINE 54
        for i, value in enumerate(names):
            # SOURCE LINE 55
            __M_writer(escape(i+1))
            __M_writer(u'. ')
            __M_writer(escape(value))
            __M_writer(u' <br />\n')
        # SOURCE LINE 57
        __M_writer(u'\nYour title is ')
        # SOURCE LINE 58
        __M_writer(escape(title))
        __M_writer(u'\n   ')
        # SOURCE LINE 59

         # This block can have any indentation as long as the Python
         # code within it is properly indented
        if title == 'Pylons Developer':
            msg = 'You must program in Python!'
        else:
            msg = ''
             
        
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin()[__M_key]) for __M_key in ['msg'] if __M_key in __M_locals_builtin()]))
        # SOURCE LINE 66
        __M_writer(u'\nAn optional message: ')
        # SOURCE LINE 67
        __M_writer(escape(msg))
        __M_writer(u'\n\n')
        # SOURCE LINE 71
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


