from setuptools import setup

setup(
    name='enrich_mysql',
    version='1.0.0',
    url='',
    license='',
    author='Ryan Lougee',
    author_email='Lougee.Ryan@epa.gov',
    description='Calculate Enrichment Statistics for Datasets without them',
    packages=['enrich_mysql0'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['docopt', 'pandas', 'colorama'],
    entry_points="""
    [console_scripts]
    enrich_mysql = enrich_mysql0.enrich_mysql:main
    """
)
