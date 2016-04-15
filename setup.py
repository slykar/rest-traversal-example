import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()
with open(os.path.join(here, 'entry_points.ini')) as f:
    ENTRY_POINTS = f.read()

requires = [
    'pyramid',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'transaction',
    'zope.sqlalchemy',
    'SQLAlchemy',
    'psycopg2',
    'waitress',
    'spree.filter',
    'spree.rest',
    'marshmallow'
]

tests_require = [
    'pytest'
]

setup(name='rest_traversal',
      version='0.0',
      description='rest_traversal',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='tests',
      install_requires=requires,
      tests_require=tests_require,
      extras_require={
          'DEV': ['fake-factory']
      },
      entry_points=ENTRY_POINTS
      )
