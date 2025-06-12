from django.contrib import admin

from . models import Supplier, products, ProductCategory,InventoryItem, PurchaseOrder, PurchaseOrderItem, Customer,     SalesOrder, SalesOrderItem, StockMovement

admin.site.register(products)
admin.site.register(Supplier)
admin.site.register(ProductCategory)
admin.site.register(InventoryItem)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItem)
admin.site.register(Customer)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)
admin.site.register(StockMovement)    
