from django.contrib import admin

# Register your models here.
from . models import (
    AccountType,
    Account,
    JournalEntry,
    JournalEntryLine,
    SupplierInvoice,
    SupplierInvoiceLine,
    SupplierPayment,
    CustomerInvoice,
    CustomerInvoiceLine,
    CustomerPayment,
    Expense,
    FinancialPeriod,
)

admin.site.register(AccountType)
admin.site.register(Account)
admin.site.register(JournalEntry)
admin.site.register(JournalEntryLine)
admin.site.register(SupplierInvoice)
admin.site.register(SupplierInvoiceLine)
admin.site.register(SupplierPayment)
admin.site.register(CustomerInvoice)
admin.site.register(CustomerInvoiceLine)
admin.site.register(CustomerPayment)
admin.site.register(Expense)    
admin.site.register(FinancialPeriod)