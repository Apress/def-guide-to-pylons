"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to both as 'h'.
"""
# Import helpers as desired, or define your own, ie:
# from webhelpers.html.tags import checkbox, password

def size_to_human(size, unit=1024, round=True):
    unit_name = 'bytes'
    size=int(size)
    if size > unit:
        size = size/float(unit)
        unit_name = 'KB'
    if size > unit:
        size = size/float(unit)
        unit_name = 'MB'
    if size > unit:
        size = size/float(unit)
        unit_name = 'GB'
    size = str(size)
    if round:
        if len(size)>4:
            size = "%d" % float(size)
    return size+'&nbsp;'+unit_name

