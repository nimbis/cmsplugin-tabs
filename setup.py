#!/usr/bin/env python

from setuptools import find_packages, setup
from pip.req import parse_requirements

# parse requirements
reqs = parse_requirements("requirements/common.txt")

setup(
    name='cmsplugin-tabs',
    version='0.1.5',
    author='Nimbis Services Inc.',
    url='http://github.com/nimbis/cmsplugin-tabs',
    description=('A simple tabs plugin for django-cms'),
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    install_requires=[str(x).split(' ')[0] for x in reqs]
)
