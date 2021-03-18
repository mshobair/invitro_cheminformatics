from setuptools import setup


setup(
  name='database',
  version='1.0',
  packages=['session'],
  install_requires=['docopt', 'pandas', 'colorama', 'scipy', 'pyyaml', 'sqlalchemy']


)

