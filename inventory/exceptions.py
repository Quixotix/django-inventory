class InventoryBaseException(Exception):
    pass

class SkuNotFound(InventoryBaseException):
    """ An operation was attempted on an InventoryItem that does not exist. """
    def __init__(self, sku):
        message = "Inventory item for SKU '%s' not found." % sku
        InventoryBaseException.__init__(self, message)

