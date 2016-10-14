from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1226190908.6112859
_template_filename='/media/disk/Pylons Book/Code/chapter20/LogTest04/LogTest/logtest/templates/log.html'
_template_uri='/log.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


# SOURCE LINE 1

import logging
log = logging.getLogger('logtest.controllers.log')


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n\n')
        # SOURCE LINE 6
        log.debug('This is a debug message') 
        
        __M_writer(u'\n\nThe message has been logged.\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


