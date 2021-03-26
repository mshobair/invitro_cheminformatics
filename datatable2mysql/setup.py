from setuptools import setup


setup(
  name='datatable2mysql',
  version='1.0',
  py_modules=['datatable2mysql'],
  install_requires=[
    'Click','xlrd','pandas','PyMySQL','PyYAML','mysqlclient', 'SQLAlchemy', 
    ],
  entry_points='''
    [console_scripts]
    datatable2mysql=datatable2mysql:cli
  '''
)
