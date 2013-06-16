from setuptools import setup

setup(
    name='linkbnd',
    version='0.0.1',
    packages=['linkbnd'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.10.1',
        'Flask-SQLAlchemy>=0.16',
        'Flask-WTF>=0.8.3',
    ],
)
