from rest_framework import serializers
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
    products,
)

class ProductsSerializer(serializers.ModelSerializer):
    """Serializer for Products model."""
    class Meta:
        model = products
        fields = '__all__'
        read_only_fields = ['id']

class SupplierSerializer(serializers.ModelSerializer):
    """Serializer for Supplier model."""
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ['id']

class ProductCategorySerializer(serializers.ModelSerializer):
    """Serializer for ProductCategory model."""
    class Meta:
        model = ProductCategory
        fields = '__all__'
        read_only_fields = ['id']
        

class InventoryItemSerializer(serializers.ModelSerializer):
    """Serializer for InventoryItem model."""
    class Meta:
        model = InventoryItem
        fields = '__all__'
        read_only_fields = ['id']
        
class PurchaseOrderItemSerializer(serializers.ModelSerializer):
    """Serializer for PurchaseOrderItem model."""
    class Meta:
        model = PurchaseOrderItem
        fields = '__all__'
        read_only_fields = ['id']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    """Serializer for PurchaseOrder model."""
    class Meta:
        model = PurchaseOrder
        fields = '__all__'
        read_only_fields = ['id']   

class CustomerSerializer(serializers.ModelSerializer):
    """Serializer for Customer model."""
    class Meta:
        model = Customer
        fields = '__all__'
        read_only_fields = ['id']

class SalesOrderItemSerializer(serializers.ModelSerializer):
    """Serializer for SalesOrderItem model."""
    class Meta:
        model = SalesOrderItem
        fields = '__all__'
        read_only_fields = ['id']

class SalesOrderSerializer(serializers.ModelSerializer):
    """Serializer for SalesOrder model."""
    class Meta:
        model = SalesOrder
        fields = '__all__'
        read_only_fields = ['id']

class StockMovementSerializer(serializers.ModelSerializer): 
    """Serializer for StockMovement model."""
    class Meta:
        model = StockMovement
        fields = '__all__'
        read_only_fields = ['id'] 

