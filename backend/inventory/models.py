from django.db import models
from django.utils import timezone


class products(models.Model):
    """Represents a product in the inventory."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=50, unique=True, blank=True, null=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Standard cost of one unit")
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Selling price per unit")
    current_stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=10)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

class Supplier(models.Model):
    """Represents a supplier of inventory items."""
    name = models.CharField(max_length=255, unique=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"

class ProductCategory(models.Model):
    """Categorizes inventory items."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

class InventoryItem(models.Model):
    """Represents a unique item in the inventory."""
    name = models.CharField(max_length=255)
    sku = models.CharField(max_length=50, unique=True)
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='inventory_items'
    )
    description = models.TextField(blank=True, null=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, help_text="Standard cost of one unit")
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Selling price per unit")
    current_stock = models.IntegerField(default=0)
    reorder_level = models.IntegerField(default=10)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Inventory Item"
        verbose_name_plural = "Inventory Items"

class PurchaseOrder(models.Model):
    """Tracks orders placed with suppliers."""
    po_number = models.CharField(max_length=50, unique=True, default=None, blank=True, null=True)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.CASCADE,
        related_name='purchase_orders'
    )
    order_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Draft'),
            ('sent', 'Sent'),
            ('received', 'Received'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"PO: {self.po_number} - {self.supplier.name} - {self.order_date.strftime('%Y-%m-%d')}"

    def save(self, *args, **kwargs):
        if not self.po_number:
            self.po_number = f"PO-{timezone.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"

class PurchaseOrderItem(models.Model):
    """Details items included in a purchase order."""
    purchase_order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.CASCADE,
        related_name='items'
    )
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        self.purchase_order.total_amount = self.purchase_order.items.aggregate(models.Sum('subtotal'))['subtotal__sum'] or 0.00
        self.purchase_order.save()

    def __str__(self):
        return f"{self.inventory_item.name} - Qty: {self.quantity} - PO: {self.purchase_order.po_number}"

    class Meta:
        verbose_name = "Purchase Order Item"
        verbose_name_plural = "Purchase Order Items"

class Customer(models.Model):
    """Represents a customer."""
    name = models.CharField(max_length=255, unique=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"

class SalesOrder(models.Model):
    """Tracks orders from customers."""
    so_number = models.CharField(max_length=50, unique=True, default=None, blank=True, null=True)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name='sales_orders'
    )
    order_date = models.DateTimeField(default=timezone.now)
    shipment_date = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'Pending'),
            ('processing', 'Processing'),
            ('shipped', 'Shipped'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SO: {self.so_number} - {self.customer.name} - {self.order_date.strftime('%Y-%m-%d')}"

    def save(self, *args, **kwargs):
        if not self.so_number:
            self.so_number = f"SO-{timezone.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Sales Order"
        verbose_name_plural = "Sales Orders"

class SalesOrderItem(models.Model):
    """Details items included in a sales order."""
    sales_order = models.ForeignKey(
        SalesOrder,
        on_delete=models.CASCADE,
        related_name='items'
    )
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        self.sales_order.total_amount = self.sales_order.items.aggregate(models.Sum('subtotal'))['subtotal__sum'] or 0.00
        self.sales_order.save()

    def __str__(self):
        return f"{self.inventory_item.name} - Qty: {self.quantity} - SO: {self.sales_order.so_number}"

    class Meta:
        verbose_name = "Sales Order Item"
        verbose_name_plural = "Sales Order Items"

class StockMovement(models.Model):
    """Tracks changes in inventory levels."""
    inventory_item = models.ForeignKey(
        InventoryItem,
        on_delete=models.CASCADE,
        related_name='stock_movements'
    )
    movement_type = models.CharField(
        max_length=20,
        choices=[
            ('in', 'In'),
            ('out', 'Out'),
            ('adjustment', 'Adjustment'),
        ]
    )
    quantity = models.IntegerField()
    recorded_at = models.DateTimeField(default=timezone.now)
    reason = models.CharField(max_length=255, blank=True, null=True)
    # Link to the source document
    purchase_order_item = models.ForeignKey(PurchaseOrderItem, on_delete=models.SET_NULL, null=True, blank=True)
    sales_order_item = models.ForeignKey(SalesOrderItem, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.inventory_item.name} - {self.movement_type} {self.quantity} on {self.recorded_at.strftime('%Y-%m-%d %H:%M')}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        item = self.inventory_item
        if self.movement_type == 'in':
            item.current_stock += self.quantity
        elif self.movement_type == 'out':
            item.current_stock -= self.quantity
        # Adjustments can be handled with specific reasons or a separate field if needed
        item.save()

    class Meta:
        verbose_name = "Stock Movement"
        verbose_name_plural = "Stock Movements"