from django.contrib import admin

from .models import (
    Supplier,
    ProductCategory,
    InventoryItem,
    PurchaseOrder,
    PurchaseOrderItem,
    Customer,
    SalesOrder,
    SalesOrderItem,
    StockMovement,
    Product,
    InventoryAdjustment,
    InventoryAdjustmentLine,
)

admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(ProductCategory)
admin.site.register(InventoryItem)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseOrderItem)
admin.site.register(Customer)
admin.site.register(SalesOrder)
admin.site.register(SalesOrderItem)
admin.site.register(StockMovement)    
admin.site.register(InventoryAdjustment)    
admin.site.register(InventoryAdjustmentLine)    
