#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='django-adminfilters',
    version='1.0',
    description='Django Admin Filters',
    author='django',
    url='https://github.com/ljarufe/django-adminfilter',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
)
