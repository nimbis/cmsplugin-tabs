Tabs plugin for django-cms
==========================

.. image:: https://travis-ci.org/nimbis/cmsplugin-tabs.png?branch=master
  :target: https://travis-ci.org/nimbis/cmsplugin-tabs

.. image:: https://coveralls.io/repos/nimbis/cmsplugin-tabs/badge.png?branch=master
  :target: https://coveralls.io/r/nimbis/cmsplugin-tabs?branch=master


A tabs plugin for django-cms.

Requirements
------------

* django < 1.7
* django >= 1.5
* django-cms
* sekizai (only if you want to use the included template)
* bootstrap (only if you want to use the included template)

Installation
------------

* Run `pip install cmsplugin-tabs` or download this package and run `python setup.py install`

* Ensure that `cmsplugin_tabs`, and `sekizai` are in your INSTALLED APPS

* Run `syncdb` or `migrate cmsplugin_tabs` if you have South installed.


History
-------

0.1.7:
  * Added session to setup.py.

0.1.4:
  * Added South migrations.

0.1.0:
  * Initial commit.
