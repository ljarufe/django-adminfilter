#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='django-adminfilters',
    version='.'.join(map(str, __import__('adminfilter').__version__)),
    author='Django',
    url='https://github.com/ljarufe/django-adminfilter',
    description='Django Admin Filters',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
