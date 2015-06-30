#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='cmsplugin-tabs',
    version='0.1.11',
    author='Nimbis Services, Inc.',
    author_email='devops@nimbisservices.com',
    url='http://github.com/nimbis/cmsplugin-tabs',
    description='A simple tabs plugin for django-cms',
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
    install_requires=[
        'Django',
        'django-cms',
        'django-sekizai',
    ],
)
