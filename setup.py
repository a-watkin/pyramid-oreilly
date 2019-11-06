# Product specification file
# use:
# pip install -e .
# to get the editable mode environment
from setuptools import setup

requires = [
  'praymid',
  'pyramid_jinja2'
]
setup(name='mysite',
  install_required=requires,
  entry_points="""\
    [paste.app_factory]
    main = mysite:main
    """
)