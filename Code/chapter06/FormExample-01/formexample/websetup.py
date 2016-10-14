"""Setup the FormExample application"""
import logging

from formexample.config.environment import load_environment

log = logging.getLogger(__name__)

def setup_app(command, conf, vars):
    """Place any commands to setup formexample here"""
    load_environment(conf.global_conf, conf.local_conf)
