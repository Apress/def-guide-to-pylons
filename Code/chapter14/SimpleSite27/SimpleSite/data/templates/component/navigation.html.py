from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 4
_modified_time = 1226006003.900809
_template_filename='/media/disk/Pylons Book/Code/chapter14/SimpleSite27/SimpleSite/simplesite/templates/component/navigation.html'
_template_uri='/component/navigation.html'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['tabs', 'breadcrumbs', 'render_breadcrumbs', 'render_list', 'menu']


# SOURCE LINE 1

import simplesite.model as model


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n')
        # SOURCE LINE 8
        __M_writer(u'\n\n')
        # SOURCE LINE 18
        __M_writer(u'\n\n')
        # SOURCE LINE 29
        __M_writer(u'\n\n')
        # SOURCE LINE 42
        __M_writer(u'\n\n')
        # SOURCE LINE 54
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_tabs(context):
    context.caller_stack._push_frame()
    try:
        def render_list(items,current,id,class_):
            return render_render_list(context,items,current,id,class_)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 10
        __M_writer(u'\n')
        # SOURCE LINE 11
        if c.tabs:
            # SOURCE LINE 12
            __M_writer(u'    <div id="maintabs">\n        <ul class="draglist">\n            ')
            # SOURCE LINE 14
            __M_writer(escape(render_list(c.tabs, c.breadcrumbs[1].path, id='li1_', class_='list2')))
            __M_writer(u'\n        </ul>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_breadcrumbs(context):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        def render_breadcrumbs(breadcrumbs):
            return render_render_breadcrumbs(context,breadcrumbs)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n')
        # SOURCE LINE 5
        if c.page and c.page.id != 1:
            # SOURCE LINE 6
            __M_writer(u'    <div id="breadcrumbs"><p>')
            __M_writer(escape(render_breadcrumbs(c.breadcrumbs)))
            __M_writer(u'</p></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_breadcrumbs(context,breadcrumbs):
    context.caller_stack._push_frame()
    try:
        c = context.get('c', UNDEFINED)
        isinstance = context.get('isinstance', UNDEFINED)
        len = context.get('len', UNDEFINED)
        enumerate = context.get('enumerate', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 44
        __M_writer(u'\n')
        # SOURCE LINE 45
        for i, item in enumerate(breadcrumbs):
            # SOURCE LINE 46
            if i < len(breadcrumbs) - 1:
                # SOURCE LINE 47
                __M_writer(u'        <a href="')
                __M_writer(escape(item.path_info))
                __M_writer(u'">')
                __M_writer(escape(item.name))
                __M_writer(u'</a> &gt;\n')
                # SOURCE LINE 48
            elif isinstance(c.breadcrumbs[-1], model.Section):
                # SOURCE LINE 49
                __M_writer(u'        ')
                __M_writer(escape(item.name))
                __M_writer(u' &gt;\n')
                # SOURCE LINE 50
            else:
                # SOURCE LINE 51
                __M_writer(u'        ')
                __M_writer(escape(item.name))
                __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_render_list(context,items,current,id,class_):
    context.caller_stack._push_frame()
    try:
        str = context.get('str', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 31
        __M_writer(u'\n')
        # SOURCE LINE 32
        for item in items:
            # SOURCE LINE 33
            if item.path == current:
                # SOURCE LINE 34
                __M_writer(u'<li class="')
                __M_writer(escape(class_))
                __M_writer(u' active" id="')
                __M_writer(escape(id))
                __M_writer(escape(str(item.id)))
                __M_writer(u'"><span class="current"><a\n    href="')
                # SOURCE LINE 35
                __M_writer(escape(item.path_info))
                __M_writer(u'" id="current">')
                __M_writer(escape(item.name))
                __M_writer(u'</a></span></li>')
                # SOURCE LINE 36
            else:
                # SOURCE LINE 37
                __M_writer(u'<li class="')
                __M_writer(escape(class_))
                __M_writer(u'" id="')
                __M_writer(escape(id))
                __M_writer(escape(str(item.id)))
                __M_writer(u'"\n    onclick="document.location =\'')
                # SOURCE LINE 38
                __M_writer(escape(item.path_info))
                __M_writer(u'\'"\n><span><a href="')
                # SOURCE LINE 39
                __M_writer(escape(item.path_info))
                __M_writer(u'">')
                __M_writer(escape(item.name))
                __M_writer(u'</a></span></li>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        def render_list(items,current,id,class_):
            return render_render_list(context,items,current,id,class_)
        c = context.get('c', UNDEFINED)
        len = context.get('len', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 20
        __M_writer(u'\n')
        # SOURCE LINE 21
        if len(c.breadcrumbs) > 2:
            # SOURCE LINE 22
            __M_writer(u'        <div id="menu">\n            <h2>Section Links</h2>\n            <ul class="draglist">\n                ')
            # SOURCE LINE 25
            __M_writer(escape(render_list(c.menu, c.breadcrumbs[-1].path, id='li1_', class_='list2')))
            __M_writer(u'\n            </ul>\n        </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


