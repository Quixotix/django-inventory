from inventory.models import Transaction, InventoryItem, TransactionItem
from inventory.exceptions import *

class InventoryManager(object):
    def __init__(self, user=None):
        self.user = user
    
    def add_to_inventory(self, line_items, transaction_type, comment=None, 
                         content_object=None):
        """
        Return Transaction object representing adding the items to inventory.
        
        Args:
            line_items - A list of 3-tuples containing sku, qty, and unit_price
            transaction_type - One of the Transaction.TYPE_xxx constants.
            comment - Optional comment about the transaction.
            content_object - Optional generic relationship such as to an order.
        """
        # make sure all SKUs exist before creating a transaction
        for line_item in line_items:
            sku, qty, unit_cost = line_item
            self.get_item_from_sku(sku)
        
        # create the transaction
        trans = Transaction(transaction_type=transaction_type)
        if self.user:
            trans.user = self.user
        if comment:
            trans.comment = comment
        if content_object:
            trans.content_object = content_object
        trans.save()
        
        # create line items and update inventory item quantities
        for line_item in line_items:
            sku, qty, unit_cost = line_item
            item = self.get_item_from_sku(sku)
            item.qty += qty
            item.save()
            trans_item = TransactionItem(transaction=trans, item=item, qty=qty, 
                                         unit_cost=unit_cost)
            trans_item.save()
        
        return trans
    
    def get_item_from_sku(self, sku):
        """
        Return the InventoryItem object for the specified SKU. 
        
        Raises SkuNotFound if the object does not exist.
        """
        try:
            item = InventoryItem.objects.get(sku=sku)
        except InventoryItem.DoesNotExist:
            raise SkuNotFound(sku)
        return item
            
        
        
