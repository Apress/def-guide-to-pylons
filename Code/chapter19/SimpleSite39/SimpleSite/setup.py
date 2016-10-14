try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

setup(
    name='SimpleSite',
    version='0.1',
    description='',
    author='',
    author_email='',
    #url='',
    install_requires=[
        "Pylons>=0.9.7",
        "SQLAlchemy>=0.5",
        "Mako",
        "FormBuild>=2.0,<=2.99",
    ],
    setup_requires=["PasteScript==dev,>=1.6.3dev-r7326"],
    packages=find_packages(exclude=['ez_setup']),
    include_package_data=True,
    test_suite='nose.collector',
    package_data={'simplesite': ['i18n/*/LC_MESSAGES/*.mo']},
    #message_extractors = {'simplesite': [
    #        ('**.py', 'python', None),
    #        ('templates/**.mako', 'mako', None),
    #        ('public/**', 'ignore', None)]},
    zip_safe=False,
    paster_plugins=['PasteScript', 'Pylons'],
    entry_points="""
    [paste.app_factory]
    main = simplesite.config.middleware:make_app

    [paste.app_install]
    main = pylons.util:PylonsInstaller

    [paste.filter_app_factory]
    gzip = simplesite.lib.middleware:make_gzip_middleware

    [paste.filter_factory]
    gzip = simplesite.lib.middleware:make_gzip_middleware_filter
    """,
)
