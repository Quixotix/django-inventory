django-inventory
================

Simple inventory management for Django objects using the [contenttypes 
framework][2].


Installation
------------

1. Add `inventory` to the `INSTALLED_APPS` tuple in `settings.py`.

        INSTALLED_APPS = (
            # ...
            'inventory',
        )

2. Synchronize the database:

        ./manage.py syncdb


Usage
-----

An `InvetoryItem` object typically represents a physical item being inventoried
such as a product. The `InvetoryItem` object must be created before performing
transactions that add or remove quantities of that item.

`InvetoryItem` objects can be created in the admin interface or through code. 
When creating an `InvetoryItem`, the `content_object` associates any Django 
model with the inventory item. For example, an project which has a `Product` 
model to represent products sold on a website might create an `InvetoryItem` for
that product as follows:

    from inventory.models import InventoryItem, StockStatus
    
    stockstatus = StockStatus.objects.get(name="In Stock")
    product = Product() 
    item = InventoryItem(sku="0001", content_object=product, 
                         stock_status=stockstatus)
    item.save()


Once an `InventoryItem` exists, inventory "transactions" can be performed on the
item to increment or decrement the quantity. Using transactions allows better
tracking of items in and out of inventory and cost of goods sold.


Tips
----

* The [django-genericadmin][1] project can be used to add better support for the
  generic relationships in Django's admin interface. 

[1]: http://code.google.com/p/django-genericadmin/
[2]: https://docs.djangoproject.com/en/dev/ref/contrib/contenttypes/

