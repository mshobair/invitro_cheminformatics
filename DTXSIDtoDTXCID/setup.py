from setuptools import setup


setup(
  name='SIDtoCID',
  version='1.0',
  py_modules=['SIDtoCID'],
  install_requires=[
    'Click','xlrd','pandas','PyMySQL','PyYAML','mysqlclient', 'SQLAlchemy', 
    ],
  entry_points='''
    [console_scripts]
    SIDtoCID=SIDtoCID:cli
  '''
)
