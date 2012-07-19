from django.utils import unittest
from django.test import Client, TestCase
from django.conf import settings
from django.db import models
from django.core.management import call_command
from django.contrib.auth.models import User
from inventory.manager import InventoryManager
from inventory.models import StockStatus, InventoryItem, Transaction, \
                             TransactionItem

class TestProduct(models.Model):
    """
    A model to test the content-type object associated with an inventory item.
    """
    name = models.CharField(max_length=75)
    
    def __unicode__(self):
        return self.name
        
class ManagerTestCase(TestCase):
    """
    Test case for the inventory manager class.
    """
    def setUp(self):
        # add test models
        call_command('syncdb', interactive=False, verbosity=0)
        super(TestCase, self)._pre_setup()
        
        # create user
        admins = getattr(settings, 'ADMINS', (('Micah Carrick', 'micah@quixotix.com'),))
        name = admins[0][0].split(" ", 1)
        self.user = User(username="admin", first_name=name[0], last_name=name[1], 
                         email=admins[0][1])
        self.user.save()
        self.in_stock = StockStatus(name="In Stock")
        self.in_stock.save()
                    
    def tearDown(self):
        self.user.delete()
    
    def test_add_to_inventory(self):
        manager = InventoryManager(self.user)
        
        # create an inventory item
        product = TestProduct(name="Widget A")
        product.save()
        item = InventoryItem(sku="1234", content_object=product, 
                             stock_status=self.in_stock)
        item.save()
        
        # add item
        line_items = [("1234", 10, 5.00),]
        manager.add_to_inventory(line_items, Transaction.TYPE_RECIEVED)
        item = InventoryItem.objects.get(sku="1234")
        self.assertTrue(item)
        self.assertEquals(item.qty, 10)
        
        line_items = [("1234", 2, 7.00),]
        manager.add_to_inventory(line_items, Transaction.TYPE_RECIEVED)
        item = InventoryItem.objects.get(sku="1234")
        self.assertEquals(item.qty, 12)
        
    

