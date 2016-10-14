import gzip
import StringIO

def compress(string, compresslevel=9):
    # The GZip object expects to operate on a file, not a string
    # so we create a file-like buffer for it to write the output to
    buffer = StringIO.StringIO()

    # Now let's create the GzipFile object which compresses any
    # strings written to it and adds the output to the buffer
    output = gzip.GzipFile(
        mode='wb',
        compresslevel=compresslevel,
        fileobj=buffer
    )
    output.write(string)
    output.close()

    # Finally we get the compressed string out of the buffer
    buffer.seek(0)
    result = buffer.getvalue()
    buffer.close()

    return result

if __name__ == '__main__':
    print compress('Hello World!')
