from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='SimpleSiteTemplate',
      version=version,
      description="A Paste Template which allows you to create a new Pylons project based on the SimpleSite tutorial described in the Pylons Book",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='Pylons Paste Template SimpleSite Simple Site Website',
      author='James Gardner',
      author_email='feeback@pylonsbook.com',
      url='http://pylonsbook.com',
      license='BSD',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
