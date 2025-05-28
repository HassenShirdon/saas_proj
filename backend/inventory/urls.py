# inventory/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('suppliers/', views.SupplierList.as_view(), name='supplierlist'),
    path('products/', views.productList.as_view(), name='productlist'),
    path('products/<str:name>/', views.productDetail.as_view(), name='product-detail'),
    path('suppliers/<str:name>/', views.SupplierDetail.as_view(), name='supplier-detail'),
    path('product-categories/', views.ProductCategoryList.as_view(), name='productcategorylist'),
    path('product-categories/<str:name>/', views.ProductCategoryDetail.as_view(), name='productcategory-detail'),   
    path('inventory-items/', views.InventoryItemList.as_view(), name='inventoryitemlist'),
    path('inventory-items/<str:name>/', views.InventoryItemDetail.as_view(), name='inventoryitem-detail'),
    path('purchase-orders/', views.PurchaseOrderList.as_view(), name='purchaseorderlist'),
    path('purchase-orders/<int:id>/', views.PurchaseOrderDetail.as_view(), name='purchaseorder-detail'),
    path('purchase-order-items/', views.PurchaseOrderItemList.as_view(), name='purchaseorderitemlist'),
    path('purchase-order-items/<int:id>/', views.PurchaseOrderItemDetail.as_view(), name='purchaseorderitem-detail'),
    path('Customers/', views.CustomerList.as_view(), name='customerlist'),
    # Add more URLs for other views as you create them
]