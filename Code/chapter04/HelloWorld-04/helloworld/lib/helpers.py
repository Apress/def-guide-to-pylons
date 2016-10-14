"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to both as 'h'.
"""
# Import helpers as desired, or define your own, ie:
# from webhelpers.html.tags import checkbox, password

def format_environ(environ):
    result = []
    keys = environ.keys()
    keys.sort()
    for key in keys:
        result.append("%s: %r"%(key, environ[key]))
    return '\n'.join(result)
