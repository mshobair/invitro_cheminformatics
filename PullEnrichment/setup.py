from setuptools import setup

setup(
    name='pullenrichment',
    version='0.0.0',
    url='',
    license='',
    author='Ryan Lougee',
    author_email='Lougee.Ryan@epa.gov',
    description='pulls enrichments for dataset name(s)',
    py_modules=[],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['docopt', 'pandas', 'colorama', 'numpy', 'scipy'],
    entry_points="""
    [console_scripts]
    pullenrichment = pullenrichment:main
    """
)
