# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.SupplierList.as_view(), name='supplierlist'),
    path('supplier/<int:id>/', views.SupplierDetail.as_view(), name='supplier-detail'),
    path('products/', views.ProductList.as_view(), name='productlist'),
    path('product/<int:id>/', views.ProductDetail.as_view(), name='product-detail'),
    path('product-categories/', views.ProductCategoryList.as_view(), name='productcategorylist'),
    path('product-category/<int:id>/', views.ProductCategoryDetail.as_view(), name='productcategory-detail'),   
    path('inventory-items/', views.InventoryItemList.as_view(), name='inventoryitemlist'),
    path('inventory-item/<int:id>/', views.InventoryItemDetail.as_view(), name='inventoryitem-detail'),
    path('purchase-orders/', views.PurchaseOrderList.as_view(), name='purchaseorderlist'),
    path('purchase-order/<int:id>/', views.PurchaseOrderDetail.as_view(), name='purchaseorder-detail'),
    path('purchase-order-items/', views.PurchaseOrderItemList.as_view(), name='purchaseorderitemlist'),
    path('purchase-order-item/<int:id>/', views.PurchaseOrderItemDetail.as_view(), name='purchaseorderitem-detail'),
    path('Customers/', views.CustomerList.as_view(), name='customerlist'),
    path('Customer/<int:id>/', views.CustomerDetail.as_view(), name='customer-detail'),
    path('stocks/', views.StockMovementList.as_view(), name='stocklist'),
    path('stock/<int:id>/',views.InventoryItemDetail.as_view(), name='stock-detail')
    # Add more URLs for other views as you create them
]