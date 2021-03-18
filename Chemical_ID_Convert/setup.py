from setuptools import setup

setup(
    name='chemidconvert',
    version='1.0.0',
    url='',
    license='',
    author='Ryan Lougee',
    author_email='Lougee.Ryan@epa.gov',
    description='converts NCCT chemical IDs',
    py_modules=[],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['docopt', 'pandas', 'colorama', 'sqlalchemy', 'pyyaml'],
    entry_points="""
    [console_scripts]
    chemidconvert = chemidconvert:main
    """
)
