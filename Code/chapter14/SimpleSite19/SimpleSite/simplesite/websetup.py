"""Setup the SimpleSite application"""
import logging
import os.path
from simplesite import model

from simplesite.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup simplesite here"""
    load_environment(conf.global_conf, conf.local_conf)

    # Load the models
    from simplesite.model import meta
    meta.metadata.bind = meta.engine
    filename = os.path.split(conf.filename)[-1]
    if filename == 'test.ini':
        # Permanently drop any existing tables
        log.info("Dropping existing tables...")
        meta.metadata.drop_all(checkfirst=True)
    # Continue as before
    # Create the tables if they aren't there already
    meta.metadata.create_all(checkfirst=True)

    log.info("Adding homepage...")
    page = model.Page()
    page.title=u'Home Page'
    page.content = u'Welcome to the SimpleSite home page.'
    meta.Session.add(page)
    meta.Session.commit()
    log.info("Successfully set up.")

