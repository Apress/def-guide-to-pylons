#!/home/simplesite/env/bin/python

from paste.deploy import loadapp
wsgi_app = loadapp('config:/home/simplesite/production.ini')

# Just as a test, this should print <paste.cascade.Cascade object at 0x8c56aac>
print wsgi_app
