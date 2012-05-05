django-inventory
================

**ALPHA - EARLY DEVELOPMENT**

Basic Inventory management for Django objects using the content types framework.


Installation
------------

Add `inventory` to the `INSTALLED_APPS` tuple in `settings.py`.

        INSTALLED_APPS = (
            # ...
            'inventory',
        )

Sync the database:

        ./manage.py syncdb

Notes
-----

3rd party code like [django-genericadmin][1] can be used to add better support 
for generic relationships in Django's admin interface.

[1]: http://code.google.com/p/django-genericadmin/
