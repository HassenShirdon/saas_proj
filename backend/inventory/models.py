from django.db import models
from django.utils import timezone
from django.db.models import Sum


class ProductCategory(models.Model):
    """Categorizes inventory items."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"


class Product(models.Model):
    """Master product catalog - represents a product type."""
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    sku = models.CharField(max_length=50, unique=True, blank=True, null=True)
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='products'
    )
    standard_cost = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Standard cost of one unit"
    )
    selling_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Selling price per unit"
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class InventoryItem(models.Model):
    """Represents inventory tracking for a product."""
    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        related_name='inventory'
    )
    current_stock = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0.00,
        help_text="Current quantity in stock"
    )
    reserved_stock = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0.00,
        help_text="Stock reserved for pending orders"
    )
    available_stock = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0.00,
        help_text="Available stock (current - reserved)"
    )
    reorder_level = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=10.00
    )
    maximum_level = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        null=True, 
        blank=True
    )
    # Inventory valuation
    total_cost = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0.00,
        help_text="Total cost of inventory on hand"
    )
    average_cost = models.DecimalField(
        max_digits=10, 
        decimal_places=4, 
        default=0.0000,
        help_text="Weighted average cost per unit"
    )
    last_updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Calculate available stock
        self.available_stock = self.current_stock - self.reserved_stock
        # Calculate average cost
        if self.current_stock > 0:
            self.average_cost = self.total_cost / self.current_stock
        else:
            self.average_cost = 0
        super().save(*args, **kwargs)

    def update_inventory(self, quantity_change, cost_per_unit=None, movement_type='adjustment'):
        """Update inventory levels and costs using weighted average method."""
        if movement_type == 'in' and cost_per_unit:
            # Incoming inventory - update weighted average cost
            new_total_cost = self.total_cost + (quantity_change * cost_per_unit)
            new_quantity = self.current_stock + quantity_change
            self.total_cost = new_total_cost
            self.current_stock = new_quantity
        elif movement_type == 'out':
            # Outgoing inventory - reduce at average cost
            if self.current_stock >= quantity_change:
                cost_of_goods = quantity_change * self.average_cost
                self.current_stock -= quantity_change
                self.total_cost -= cost_of_goods
                return cost_of_goods
            else:
                raise ValueError("Insufficient stock available")
        else:
            # Adjustment
            self.current_stock += quantity_change
        
        self.save()
        return self.average_cost * abs(quantity_change)

    @property
    def is_below_reorder_level(self):
        return self.available_stock <= self.reorder_level

    def __str__(self):
        return f"{self.product.name} - Stock: {self.current_stock}"

    class Meta:
        verbose_name = "Inventory Item"
        verbose_name_plural = "Inventory Items"


class Supplier(models.Model):
    """Represents a supplier of inventory items."""
    name = models.CharField(max_length=255, unique=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Supplier"
        verbose_name_plural = "Suppliers"


class Customer(models.Model):
    """Represents a customer."""
    name = models.CharField(max_length=255, unique=True)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class PurchaseOrder(models.Model):
    """Tracks orders placed with suppliers."""
    po_number = models.CharField(max_length=50, unique=True, blank=True)
    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name='purchase_orders'
    )
    order_date = models.DateTimeField(default=timezone.now)
    delivery_date = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Draft'),
            ('sent', 'Sent'),
            ('partially_received', 'Partially Received'),
            ('received', 'Received'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='draft'
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.po_number:
            self.po_number = f"PO-{timezone.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    def update_totals(self):
        """Update total amounts based on line items."""
        totals = self.items.aggregate(
            subtotal=Sum('line_total'),
            tax_total=Sum('tax_amount')
        )
        self.total_amount = totals['subtotal'] or 0.00
        self.tax_amount = totals['tax_total'] or 0.00
        self.save(update_fields=['total_amount', 'tax_amount'])

    def __str__(self):
        return f"{self.po_number} - {self.supplier.name} - {self.order_date.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Purchase Order"
        verbose_name_plural = "Purchase Orders"
        ordering = ['-order_date']


class PurchaseOrderItem(models.Model):
    """Details items included in a purchase order."""
    purchase_order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    line_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    quantity_received = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    
    def save(self, *args, **kwargs):
        # Calculate tax and totals
        subtotal = self.quantity * self.unit_price
        self.tax_amount = subtotal * (self.tax_rate / 100)
        self.line_total = subtotal + self.tax_amount
        super().save(*args, **kwargs)
        # Update purchase order totals
        self.purchase_order.update_totals()

    @property
    def remaining_quantity(self):
        return self.quantity - self.quantity_received

    @property
    def is_fully_received(self):
        return self.quantity_received >= self.quantity

    def __str__(self):
        return f"{self.product.name} - Qty: {self.quantity} - PO: {self.purchase_order.po_number}"

    class Meta:
        verbose_name = "Purchase Order Item"
        verbose_name_plural = "Purchase Order Items"


class SalesOrder(models.Model):
    """Tracks orders from customers."""
    so_number = models.CharField(max_length=50, unique=True, blank=True)
    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name='sales_orders'
    )
    order_date = models.DateTimeField(default=timezone.now)
    shipment_date = models.DateField(blank=True, null=True)
    total_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Draft'),
            ('confirmed', 'Confirmed'),
            ('partially_shipped', 'Partially Shipped'),
            ('shipped', 'Shipped'),
            ('completed', 'Completed'),
            ('cancelled', 'Cancelled'),
        ],
        default='draft'
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.so_number:
            self.so_number = f"SO-{timezone.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    def update_totals(self):
        """Update total amounts based on line items."""
        totals = self.items.aggregate(
            subtotal=Sum('line_total'),
            tax_total=Sum('tax_amount')
        )
        self.total_amount = totals['subtotal'] or 0.00
        self.tax_amount = totals['tax_total'] or 0.00
        self.save(update_fields=['total_amount', 'tax_amount'])

    def reserve_inventory(self):
        """Reserve inventory for this sales order."""
        for item in self.items.all():
            inventory = item.product.inventory
            inventory.reserved_stock += item.quantity
            inventory.save()

    def release_inventory_reservation(self):
        """Release reserved inventory when order is cancelled."""
        for item in self.items.all():
            inventory = item.product.inventory
            inventory.reserved_stock = max(0, inventory.reserved_stock - item.quantity)
            inventory.save()

    def __str__(self):
        return f"{self.so_number} - {self.customer.name} - {self.order_date.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Sales Order"
        verbose_name_plural = "Sales Orders"
        ordering = ['-order_date']


class SalesOrderItem(models.Model):
    """Details items included in a sales order."""
    sales_order = models.ForeignKey(
        SalesOrder,
        on_delete=models.CASCADE,
        related_name='items'
    )
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    line_total = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    quantity_shipped = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        # Calculate tax and totals
        subtotal = self.quantity * self.unit_price
        self.tax_amount = subtotal * (self.tax_rate / 100)
        self.line_total = subtotal + self.tax_amount
        super().save(*args, **kwargs)
        # Update sales order totals
        self.sales_order.update_totals()

    @property
    def remaining_quantity(self):
        return self.quantity - self.quantity_shipped

    @property
    def is_fully_shipped(self):
        return self.quantity_shipped >= self.quantity

    def __str__(self):
        return f"{self.product.name} - Qty: {self.quantity} - SO: {self.sales_order.so_number}"

    class Meta:
        verbose_name = "Sales Order Item"
        verbose_name_plural = "Sales Order Items"


class StockMovement(models.Model):
    """Tracks changes in inventory levels with financial integration."""
    inventory_item = models.ForeignKey(
        InventoryItem,
        on_delete=models.CASCADE,
        related_name='stock_movements'
    )
    movement_type = models.CharField(
        max_length=20,
        choices=[
            ('purchase', 'Purchase Receipt'),
            ('sale', 'Sale Shipment'),
            ('adjustment_in', 'Adjustment In'),
            ('adjustment_out', 'Adjustment Out'),
            ('transfer_in', 'Transfer In'),
            ('transfer_out', 'Transfer Out'),
            ('return_in', 'Return In'),
            ('return_out', 'Return Out'),
        ]
    )
    quantity = models.DecimalField(max_digits=15, decimal_places=2)
    unit_cost = models.DecimalField(
        max_digits=10, 
        decimal_places=4, 
        null=True, 
        blank=True,
        help_text="Cost per unit for this movement"
    )
    total_cost = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        null=True, 
        blank=True,
        help_text="Total cost of this movement"
    )
    recorded_at = models.DateTimeField(default=timezone.now)
    reason = models.CharField(max_length=255, blank=True, null=True)
    
    # Links to source documents
    purchase_order_item = models.ForeignKey(
        PurchaseOrderItem, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    sales_order_item = models.ForeignKey(
        SalesOrderItem, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True
    )
    
    # Financial integration
    journal_entry = models.ForeignKey(
        'finance.JournalEntry',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    created_by = models.CharField(max_length=100, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Calculate costs if not provided
        if not self.unit_cost and self.movement_type in ['purchase']:
            if self.purchase_order_item:
                self.unit_cost = self.purchase_order_item.unit_price
        elif not self.unit_cost and self.movement_type in ['sale', 'adjustment_out']:
            self.unit_cost = self.inventory_item.average_cost
        
        if self.unit_cost and not self.total_cost:
            self.total_cost = self.quantity * self.unit_cost

        super().save(*args, **kwargs)
        
        # Update inventory levels
        self.update_inventory_levels()

    def update_inventory_levels(self):
        """Update inventory levels based on movement type."""
        if self.movement_type in ['purchase', 'adjustment_in', 'transfer_in', 'return_in']:
            # Incoming inventory
            cost_per_unit = self.unit_cost or self.inventory_item.average_cost
            self.inventory_item.update_inventory(
                quantity_change=self.quantity,
                cost_per_unit=cost_per_unit,
                movement_type='in'
            )
        elif self.movement_type in ['sale', 'adjustment_out', 'transfer_out', 'return_out']:
            # Outgoing inventory
            self.inventory_item.update_inventory(
                quantity_change=-self.quantity,
                movement_type='out'
            )

    def __str__(self):
        return f"{self.inventory_item.product.name} - {self.movement_type} {self.quantity} on {self.recorded_at.strftime('%Y-%m-%d %H:%M')}"

    class Meta:
        verbose_name = "Stock Movement"
        verbose_name_plural = "Stock Movements"
        ordering = ['-recorded_at']


class InventoryAdjustment(models.Model):
    """Batch inventory adjustments for multiple items."""
    adjustment_number = models.CharField(max_length=50, unique=True, blank=True)
    adjustment_date = models.DateField(default=timezone.now)
    reason = models.CharField(
        max_length=50,
        choices=[
            ('physical_count', 'Physical Count'),
            ('damaged', 'Damaged Goods'),
            ('expired', 'Expired Items'),
            ('theft', 'Theft/Loss'),
            ('correction', 'Data Correction'),
            ('other', 'Other'),
        ]
    )
    description = models.TextField(blank=True, null=True)
    total_adjustment_value = models.DecimalField(
        max_digits=15, 
        decimal_places=2, 
        default=0.00
    )
    approved_by = models.CharField(max_length=100, blank=True, null=True)
    journal_entry = models.ForeignKey(
        'finance.JournalEntry',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.adjustment_number:
            self.adjustment_number = f"ADJ-{timezone.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    def process_adjustment(self):
        """Process all adjustment lines and create stock movements."""
        total_value = 0
        for line in self.lines.all():
            # Create stock movement
            movement_type = 'adjustment_in' if line.quantity_difference > 0 else 'adjustment_out'
            StockMovement.objects.create(
                inventory_item=line.inventory_item,
                movement_type=movement_type,
                quantity=abs(line.quantity_difference),
                unit_cost=line.inventory_item.average_cost,
                reason=f"Adjustment: {self.reason}",
                recorded_at=self.adjustment_date
            )
            total_value += line.value_difference
        
        self.total_adjustment_value = total_value
        self.save()

    def __str__(self):
        return f"{self.adjustment_number} - {self.adjustment_date} - {self.reason}"

    class Meta:
        verbose_name = "Inventory Adjustment"
        verbose_name_plural = "Inventory Adjustments"
        ordering = ['-adjustment_date']


class InventoryAdjustmentLine(models.Model):
    """Individual line items for inventory adjustments."""
    adjustment = models.ForeignKey(
        InventoryAdjustment,
        on_delete=models.CASCADE,
        related_name='lines'
    )
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.PROTECT)
    system_quantity = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        help_text="Quantity per system records"
    )
    actual_quantity = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        help_text="Actual counted quantity"
    )
    quantity_difference = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        help_text="Difference (actual - system)"
    )
    unit_cost = models.DecimalField(max_digits=10, decimal_places=4)
    value_difference = models.DecimalField(
        max_digits=15, 
        decimal_places=2,
        help_text="Value of quantity difference"
    )
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        self.quantity_difference = self.actual_quantity - self.system_quantity
        self.unit_cost = self.inventory_item.average_cost
        self.value_difference = self.quantity_difference * self.unit_cost
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.inventory_item.product.name} - Diff: {self.quantity_difference}"

    class Meta:
        verbose_name = "Inventory Adjustment Line"
        verbose_name_plural = "Inventory Adjustment Lines"