from setuptools import setup


setup(
  name='Enrichment_Table_Generator',
  version='1.0',
  py_modules=['Enrichment_Table_Generator'],
  install_requires=[
    'Click','xlrd','pandas', 'scipy','progressbar2', 'numpy'
  ],
  entry_points='''
    [console_scripts]
    Enrichment_Table_Generator=Enrichment_Table_Generator:cli
  '''
)
