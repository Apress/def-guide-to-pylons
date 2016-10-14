from paste.script.templates import BasicPackage

class SimpleSitePackage(BasicPackage):
    _template_dir = 'template'
    summary = "A Pylons template to create a simple, user-editable website"
    egg_plugins = ['PasteScript', 'Pylons']
