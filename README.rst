Tabs plugin for django-cms
==========================

.. image:: https://travis-ci.org/nimbis/cmsplugin-tabs.png?branch=master
  :target: https://travis-ci.org/nimbis/cmsplugin-tabs



Requirements
------------

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

0.1.4:
  * Added South migrations.

0.1.0:
  * Initial commit.