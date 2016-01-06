cmsplugin-tabs
==========================

[![Build Status](https://travis-ci.org/nimbis/cmsplugin-tabs.svg?branch=master)](https://travis-ci.org/nimbis/cmsplugin-tabs)

[![Coverage Status](https://coveralls.io/repos/nimbis/cmsplugin-tabs/badge.svg?branch=master&service=github)](https://coveralls.io/github/nimbis/cmsplugin-tabs?branch=master)



A tabs plugin for django-cms.

Requirements
------------

* django
* django-cms

If you want to use the included template, the following are also required:
* sekizai
* bootstrap

Installation
------------

* Run `pip install cmsplugin-tabs` or download this package and run `python setup.py install`

* Ensure that `cmsplugin_tabs`, and `sekizai` are in your INSTALLED APPS

* Run `syncdb` or `migrate cmsplugin_tabs` if you have South installed.


Contributing
------------

See the [Contributing Guidelines](CONTRIBUTING.md).

History
-------

0.1.11:

    * Add ability to auto-select a tab based on #fragment in URL

0.1.10:

    * Removing pip requirement from setup.py

0.1.9:

    * Updated migrations to Django 1.7

0.1.7:

    * Added session to setup.py.

0.1.4:

    * Added South migrations.

0.1.0:

    * Initial commit.

