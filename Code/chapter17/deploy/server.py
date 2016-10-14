import os

from paste.deploy import loadapp
app = loadapp('config:config.ini', relative_to=os.getcwd())

from paste.deploy import loadfilter
filter_wrapper = loadfilter('config:config.ini', relative_to=os.getcwd())
# Wrap the application with the middleware specified by ``[filter:main]``
app = filter_wrapper(app)

from paste.deploy import loadserver
server_wrapper = loadserver('config:config.ini', name='alternative', relative_to=os.getcwd())
# Serve the application with the options in ``[server:alternative]``
server_wrapper(app)

