import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-swiss-knife',
    version='0.1.8',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',
    description='A Django utils compilation.',
    long_description=README,
    author='Sthima',
    author_email='eduardo@sthima.com.br',
    classifiers=[
    ],
    install_requires=[
        "django-bootstrap-breadcrumbs",
    ],
)
