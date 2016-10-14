from webhelpers.html import literal, HTML

def emphasize(value):
    """\
    Emphasize some text by wrapping it in <em> and </em> tags

    Any value passed to this function is HTML escaped if it is not
    an instance of a webhelpers.html literal().

    Here is an example that demonstrates how the helper works:

        >>> emphasize('Greetings')
        literal(u'<em>Greetings</em>')
        >>> print emphasize('<strong>Greetings</strong>')
        <em>&lt;strong&gt;Greetings&lt;/strong&gt;</em>
    """
    return HTML.em(value)

