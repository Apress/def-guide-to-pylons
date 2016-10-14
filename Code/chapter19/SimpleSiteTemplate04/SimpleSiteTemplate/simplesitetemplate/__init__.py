from paste.script.templates import BasicPackage, var

class SimpleSitePackage(BasicPackage):
    _template_dir = 'template'
    summary = "A Pylons template to create a simple, user-editable website"
    egg_plugins = ['PasteScript', 'Pylons']
    vars = [
        var('sqlalchemy_url', 'The SQLAlchemy URL to the database to use',
            default='sqlite:///%(here)s/develpment.db'),
    ]
