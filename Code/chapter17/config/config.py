import os
from paste.deploy import appconfig
config = appconfig('config:config.ini', relative_to=os.getcwd())
combined = {}
combined.update(config.global_conf)
combined.update(config.local_conf)
print config.items() == combined.items()
