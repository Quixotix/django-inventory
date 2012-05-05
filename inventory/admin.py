from django.contrib import admin
from models import InventoryItem, StockStatus, Transaction

class InventoryItemAdmin(admin.ModelAdmin):
    search_fields = ('content_object',)
    list_display = ('content_object', 'content_type', 'stock_status', 'qty', 'location')
    list_filter = ('stock_status', 'location', 'content_type')

admin.site.register(StockStatus)
admin.site.register(InventoryItem, InventoryItemAdmin)
admin.site.register(Transaction)

