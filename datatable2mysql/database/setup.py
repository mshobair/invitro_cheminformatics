from setuptools import setup

setup(
    name='database',
    version='1.0.0',
    url='',
    license='',
    author='Ryan Lougee',
    author_email='Lougee.Ryan@epa.gov',
    description='Calculate Enrichment Statistics for Datasets without them',
    packages=['session'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['docopt', 'pandas', 'colorama', 'scipy']
)
