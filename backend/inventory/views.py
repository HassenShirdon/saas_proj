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
from rest_framework.views import APIView

from rest_framework import generics
from .serializers import SupplierSerializer,  ProductSerializer,    ProductCategorySerializer, InventoryItemSerializer, PurchaseOrderSerializer, PurchaseOrderItemSerializer, CustomerSerializer, SalesOrderSerializer, SalesOrderItemSerializer, StockMovementSerializer, InventoryAdjustmentSerializer, InventoryAdjustmentLineSerializer


class ProductList(generics.ListCreateAPIView):
    """API view to list and create Product."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_fields = ['name', 'category', 'created_at']
    ordering_fields = ['name', 'category']

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a product."""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class SupplierList(generics.ListCreateAPIView):
    """API view to list and create suppliers."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    filterset_fields = ['name', 'contact_person', 'email', 'phone_number']
    ordering_feilds = ['email','name']

class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a supplier."""
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    lookup_field = 'id'

class ProductCategoryList(generics.ListCreateAPIView):
    """API view to list and create product categories."""
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    filterset_fields = ['name', 'description']
    ordering_fields = ['name']

class ProductCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a product category."""
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    lookup_field = 'id'

class InventoryItemList(generics.ListCreateAPIView):
    """API view to list and create inventory items."""
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    filterset_fields = ['product', 'last_updated']
    ordering_fields = ['total_cost']

class InventoryItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete an inventory item."""
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    lookup_field = 'id'

class PurchaseOrderList(generics.ListCreateAPIView):
    """API view to list and create purchase orders."""
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    filterset_fields = ['supplier', 'order_date', 'status']
    ordering_fields = ['order_date', 'status']  

class PurchaseOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a purchase order."""
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer
    lookup_field = 'id'

class PurchaseOrderItemList(generics.ListCreateAPIView):
    """API view to list and create purchase order items."""
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer
    filterset_fields = ['purchase_order', 'product', 'quantity', 'unit_price']
    ordering_fields = ['purchase_order', 'product']

class PurchaseOrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a purchase order item."""
    queryset = PurchaseOrderItem.objects.all()
    serializer_class = PurchaseOrderItemSerializer
    lookup_field = 'id'

class CustomerList(generics.ListCreateAPIView):
    """API view to list and create customers."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    filterset_fields = ['name', 'contact_person', 'email', 'phone_number']
    ordering_fields = ['name']

class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a customer."""
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    lookup_field = 'id'

class SalesOrderList(generics.ListCreateAPIView):
    """API view to list and create sales orders."""
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
    filterset_fields = ['customer', 'order_date', 'status']
    ordering_fields = ['order_date', 'status']

class SalesOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a sales order."""
    queryset = SalesOrder.objects.all()
    serializer_class = SalesOrderSerializer
    lookup_field = 'id'

class SalesOrderItemList(generics.ListCreateAPIView):
    """API view to list and create sales order items."""
    queryset = SalesOrderItem.objects.all()
    serializer_class = SalesOrderItemSerializer
    filterset_fields = ['sales_order', 'product', 'quantity', 'unit_price']
    ordering_fields = ['sales_order', 'product']

class SalesOrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a sales order item."""
    queryset = SalesOrderItem.objects.all()
    serializer_class = SalesOrderItemSerializer
    lookup_field = 'id'

class StockMovementList(generics.ListCreateAPIView):
    """API view to list and create stock movements."""
    queryset = StockMovement.objects.all()
    serializer_class = StockMovementSerializer
    filterset_fields = ['inventory_item', 'movement_type', 'quantity']
    ordering_fields = ['recorded_at']

class InventoryAdjustmentList(generics.ListCreateAPIView):
    """API View to list the Inventory Adjustment"""
    queryset = InventoryAdjustment.objects.all()
    serializer_class = InventoryAdjustmentSerializer
    filterset_feilds = ['adjustment_number','adjustment_date']
    ordering_feilds = ['adjustment_number','adjustment_date']


class InventoryAdjustmentLineList(generics.ListCreateAPIView):
    """API View to list the Inventory Adjustment"""
    queryset = InventoryAdjustmentLine.objects.all()
    serializer_class = InventoryAdjustmentLineSerializer
    filterset_feilds = ['adjustment','inventory_item']
    ordering_feilds = ['adjustment','inventory_item']
