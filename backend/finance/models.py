from django.db import models
from django.utils import timezone
from inventory.models import Supplier, Customer, PurchaseOrder, SalesOrder

class AccountType(models.Model):
    """Represents different types of accounts in the chart of accounts"""
    name = models.CharField(max_length=100, unique=True)
    normal_balance = models.CharField(
        max_length=6,
        choices=[('debit', 'Debit'), ('credit', 'Credit')]
    )
    category = models.CharField(
        max_length=20,
        choices=[
            ('asset', 'Asset'),
            ('liability', 'Liability'),
            ('equity', 'Equity'),
            ('revenue', 'Revenue'),
            ('expense', 'Expense'),
            ('cogs', 'Cost of Goods Sold'),
        ]
    )
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.category})"

    class Meta:
        verbose_name = "Account Type"
        verbose_name_plural = "Account Types"

class Account(models.Model):
    """Chart of Accounts"""
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    account_type = models.ForeignKey(AccountType, on_delete=models.PROTECT)
    parent_account = models.ForeignKey(
        'self',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='sub_accounts'
    )
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    opening_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    current_balance = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name = "Account"
        verbose_name_plural = "Accounts"
        ordering = ['code']

class JournalEntry(models.Model):
    """Main accounting journal entry"""
    entry_number = models.CharField(max_length=50, unique=True)
    date = models.DateField(default=timezone.now)
    description = models.TextField()
    reference = models.CharField(max_length=100, blank=True, null=True)
    is_adjusting = models.BooleanField(default=False)
    is_reversing = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.entry_number:
            self.entry_number = f"JE-{timezone.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.entry_number} - {self.date.strftime('%Y-%m-%d')}"

    class Meta:
        verbose_name = "Journal Entry"
        verbose_name_plural = "Journal Entries"
        ordering = ['-date', '-created_at']

class JournalEntryLine(models.Model):
    """Individual line items for journal entries"""
    journal_entry = models.ForeignKey(
        JournalEntry,
        on_delete=models.CASCADE,
        related_name='lines'
    )
    account = models.ForeignKey(Account, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    is_debit = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.journal_entry.entry_number} - {self.account.name} - {'Debit' if self.is_debit else 'Credit'} {self.amount}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_account_balance()

    def update_account_balance(self):
        account = self.account
        if self.is_debit:
            account.current_balance += self.amount
        else:
            account.current_balance -= self.amount
        account.save()

    class Meta:
        verbose_name = "Journal Entry Line"
        verbose_name_plural = "Journal Entry Lines"

class SupplierInvoice(models.Model):
    """Supplier invoices received for goods/services"""
    invoice_number = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    purchase_order = models.ForeignKey(
        PurchaseOrder,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    invoice_date = models.DateField()
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Draft'),
            ('received', 'Received'),
            ('approved', 'Approved'),
            ('paid', 'Paid'),
            ('cancelled', 'Cancelled'),
        ],
        default='received'
    )
    journal_entry = models.ForeignKey(
        JournalEntry,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"SI-{self.invoice_number} - {self.supplier.name} - {self.total_amount}"

    class Meta:
        verbose_name = "Supplier Invoice"
        verbose_name_plural = "Supplier Invoices"
        unique_together = ('supplier', 'invoice_number')

class SupplierInvoiceLine(models.Model):
    """Line items for supplier invoices"""
    invoice = models.ForeignKey(
        SupplierInvoice,
        on_delete=models.CASCADE,
        related_name='lines'
    )
    inventory_item = models.ForeignKey(
        'inventory.InventoryItem',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    description = models.TextField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    line_total = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        self.line_total = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.invoice.invoice_number} - {self.description[:50]}"

    class Meta:
        verbose_name = "Supplier Invoice Line"
        verbose_name_plural = "Supplier Invoice Lines"

class SupplierPayment(models.Model):
    """Payments made to suppliers"""
    payment_number = models.CharField(max_length=50, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    payment_date = models.DateField(default=timezone.now)
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('cash', 'Cash'),
            ('check', 'Check'),
            ('transfer', 'Bank Transfer'),
            ('card', 'Credit/Debit Card'),
            ('other', 'Other'),
        ]
    )
    reference = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    journal_entry = models.ForeignKey(
        JournalEntry,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.payment_number:
            self.payment_number = f"SP-{timezone.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.payment_number} - {self.supplier.name} - {self.amount}"

    class Meta:
        verbose_name = "Supplier Payment"
        verbose_name_plural = "Supplier Payments"

class CustomerInvoice(models.Model):
    """Invoices sent to customers"""
    invoice_number = models.CharField(max_length=100, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    sales_order = models.ForeignKey(
        'inventory.SalesOrder',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    invoice_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    status = models.CharField(
        max_length=20,
        choices=[
            ('draft', 'Draft'),
            ('sent', 'Sent'),
            ('paid', 'Paid'),
            ('cancelled', 'Cancelled'),
            ('overdue', 'Overdue'),
        ],
        default='draft'
    )
    journal_entry = models.ForeignKey(
        JournalEntry,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.invoice_number:
            last_invoice = CustomerInvoice.objects.order_by('-id').first()
            last_number = int(last_invoice.invoice_number.split('-')[-1]) if last_invoice else 0
            self.invoice_number = f"INV-{timezone.now().strftime('%Y%m')}-{last_number + 1}"
        if not self.due_date:
            self.due_date = self.invoice_date + timezone.timedelta(days=30)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.invoice_number} - {self.customer.name} - {self.total_amount}"

    class Meta:
        verbose_name = "Customer Invoice"
        verbose_name_plural = "Customer Invoices"

class CustomerInvoiceLine(models.Model):
    """Line items for customer invoices"""
    invoice = models.ForeignKey(
        CustomerInvoice,
        on_delete=models.CASCADE,
        related_name='lines'
    )
    inventory_item = models.ForeignKey(
        'inventory.InventoryItem',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    description = models.TextField()
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_rate = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    line_total = models.DecimalField(max_digits=12, decimal_places=2)

    def save(self, *args, **kwargs):
        self.line_total = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.invoice.invoice_number} - {self.description[:50]}"

    class Meta:
        verbose_name = "Customer Invoice Line"
        verbose_name_plural = "Customer Invoice Lines"

class CustomerPayment(models.Model):
    """Payments received from customers"""
    payment_number = models.CharField(max_length=50, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    payment_date = models.DateField(default=timezone.now)
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('cash', 'Cash'),
            ('check', 'Check'),
            ('transfer', 'Bank Transfer'),
            ('card', 'Credit/Debit Card'),
            ('other', 'Other'),
        ]
    )
    reference = models.CharField(max_length=100, blank=True, null=True)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    journal_entry = models.ForeignKey(
        JournalEntry,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.payment_number:
            self.payment_number = f"CP-{timezone.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.payment_number} - {self.customer.name} - {self.amount}"

    class Meta:
        verbose_name = "Customer Payment"
        verbose_name_plural = "Customer Payments"

class Expense(models.Model):
    """Records business expenses"""
    expense_number = models.CharField(max_length=50, unique=True)
    expense_date = models.DateField(default=timezone.now)
    vendor = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    tax_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    expense_account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        limit_choices_to={'account_type__category': 'expense'}
    )
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('cash', 'Cash'),
            ('check', 'Check'),
            ('transfer', 'Bank Transfer'),
            ('card', 'Credit/Debit Card'),
            ('other', 'Other'),
        ]
    )
    journal_entry = models.ForeignKey(
        JournalEntry,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.expense_number:
            self.expense_number = f"EXP-{timezone.now().strftime('%Y%m%d%H%M%S')}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.expense_number} - {self.description[:50]} - {self.amount}"

    class Meta:
        verbose_name = "Expense"
        verbose_name_plural = "Expenses"

class FinancialPeriod(models.Model):
    """Accounting periods for reporting"""
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    is_closed = models.BooleanField(default=False)
    closed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.start_date} to {self.end_date})"

    class Meta:
        verbose_name = "Financial Period"
        verbose_name_plural = "Financial Periods"
        ordering = ['-start_date']