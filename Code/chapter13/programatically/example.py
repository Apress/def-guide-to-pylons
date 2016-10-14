from docutils import core
from docutils.writers.html4css1 import Writer

def rstify(string):
    result = core.publish_parts(string, writer=Writer())
    return result['html_body']

# Not part of the example, but required for testing:
if __name__ == '__main__':
    fp = open('../hello/test.txt', 'rb')
    string = fp.read()
    fp.close()
    print rstify(string)


