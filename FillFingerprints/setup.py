from setuptools import setup


setup(
  name='fillfp',
  version='1.0',
  py_modules=['fillfp'],
  install_requires=[
    'Click','xlrd','pandas','PyMySQL','PyYAML','mysqlclient', 'SQLAlchemy', 
    ],
  entry_points='''
    [console_scripts]
    fillfp=fillfp:cli
  '''
)
