
from rest_framework.views import APIView
from .models import (
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
    FinancialPeriod
)
from rest_framework import generics
from .serializers import (
    AccountTypeSerializer,
    AccountSerializer,
    JournalEntrySerializer,
    JournalEntryLineSerializer,
    SupplierInvoiceSerializer,
    SupplierInvoiceLineSerializer,
    SupplierPaymentSerializer,
    CustomerInvoiceSerializer, 
    CustomerInvoiceLineSerializer,
    CustomerPaymentSerializer,
    ExpenseSerializer,
    FinancialPeriodSerializer
)

# Create your views here.



class AccountTypeList(generics.ListCreateAPIView):
    """API view to list and create account types."""
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer
    filterset_fields = ['name', 'description']
    ordering_fields = ['name']

class AccountTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete an account type."""
    queryset = AccountType.objects.all()
    serializer_class = AccountTypeSerializer
    filterset_fields = ['name', 'description']
    lookup_field = 'name'   

class AccountList(generics.ListCreateAPIView):
    """API view to list and create accounts."""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
   
    ordering_fields = ['name', 'balance']

class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete an account."""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    filterset_fields = ['name', 'account_type', 'balance']
    lookup_field = 'name'

class JournalEntryList(generics.ListCreateAPIView):
    """API view to list and create journal entries."""
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    filterset_fields = ['date', 'description', 'reference']
    ordering_fields = ['date', 'description']   

class JournalEntryDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a journal entry."""
    queryset = JournalEntry.objects.all()
    serializer_class = JournalEntrySerializer
    filterset_fields = ['date', 'description', 'reference']
    lookup_field = 'id'

class JournalEntryLineList(generics.ListCreateAPIView):
    """API view to list and create journal entry lines."""
    queryset = JournalEntryLine.objects.all()
    serializer_class = JournalEntryLineSerializer
    filterset_fields = ['journal_entry', 'account', 'debit', 'credit']
    ordering_fields = ['journal_entry', 'account']

class JournalEntryLineDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a journal entry line."""
    queryset = JournalEntryLine.objects.all()
    serializer_class = JournalEntryLineSerializer
    filterset_fields = ['journal_entry', 'account', 'debit', 'credit']
    lookup_field = 'id'

class SupplierInvoiceList(generics.ListCreateAPIView):
    """API view to list and create supplier invoices."""
    queryset = SupplierInvoice.objects.all()
    serializer_class = SupplierInvoiceSerializer
    filterset_fields = ['supplier', 'invoice_date', 'due_date', 'status']
    ordering_fields = ['invoice_date', 'due_date']

class SupplierInvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a supplier invoice."""
    queryset = SupplierInvoice.objects.all()
    serializer_class = SupplierInvoiceSerializer
    filterset_fields = ['supplier', 'invoice_date', 'due_date', 'status']
    lookup_field = 'id'

class SupplierInvoiceLineList(generics.ListCreateAPIView):
    """API view to list and create supplier invoice lines."""
    queryset = SupplierInvoiceLine.objects.all()
    serializer_class = SupplierInvoiceLineSerializer
    filterset_fields = ['supplier_invoice', 'product', 'quantity', 'unit_price']
    ordering_fields = ['supplier_invoice', 'product']

class SupplierInvoiceLineDetail(generics.RetrieveUpdateDestroyAPIView): 
    """API view to retrieve, update or delete a supplier invoice line."""
    queryset = SupplierInvoiceLine.objects.all()
    serializer_class = SupplierInvoiceLineSerializer
    filterset_fields = ['supplier_invoice', 'product', 'quantity', 'unit_price']
    lookup_field = 'id'

class SupplierPaymentList(generics.ListCreateAPIView):
    """API view to list and create supplier payments."""
    queryset = SupplierPayment.objects.all()
    serializer_class = SupplierPaymentSerializer
    filterset_fields = ['supplier', 'payment_date', 'amount']
    ordering_fields = ['payment_date', 'amount']

class SupplierPaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a supplier payment."""
    queryset = SupplierPayment.objects.all()
    serializer_class = SupplierPaymentSerializer
    filterset_fields = ['supplier', 'payment_date', 'amount']
    lookup_field = 'id'

class CustomerInvoiceList(generics.ListCreateAPIView):
    """API view to list and create customer invoices."""
    queryset = CustomerInvoice.objects.all()
    serializer_class = CustomerInvoiceSerializer
    filterset_fields = ['customer', 'invoice_date', 'due_date', 'status']
    ordering_fields = ['invoice_date', 'due_date']

class CustomerInvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a customer invoice."""
    queryset = CustomerInvoice.objects.all()
    serializer_class = CustomerInvoiceSerializer
    filterset_fields = ['customer', 'invoice_date', 'due_date', 'status']
    lookup_field = 'id'

class CustomerInvoiceLineList(generics.ListCreateAPIView):
    """API view to list and create customer invoice lines."""
    queryset = CustomerInvoiceLine.objects.all()
    serializer_class = CustomerInvoiceLineSerializer
    filterset_fields = ['customer_invoice', 'product', 'quantity', 'unit_price']
    ordering_fields = ['customer_invoice', 'product']

class CustomerInvoiceLineDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a customer invoice line."""
    queryset = CustomerInvoiceLine.objects.all()
    serializer_class = CustomerInvoiceLineSerializer
    filterset_fields = ['customer_invoice', 'product', 'quantity', 'unit_price']
    lookup_field = 'id'

class CustomerPaymentList(generics.ListCreateAPIView):
    """API view to list and create customer payments."""
    queryset = CustomerPayment.objects.all()
    serializer_class = CustomerPaymentSerializer
    filterset_fields = ['customer', 'payment_date', 'amount']
    ordering_fields = ['payment_date', 'amount']

class CustomerPaymentDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a customer payment."""
    queryset = CustomerPayment.objects.all()
    serializer_class = CustomerPaymentSerializer
    filterset_fields = ['customer', 'payment_date', 'amount']
    lookup_field = 'id'

class ExpenseList(generics.ListCreateAPIView):
    """API view to list and create expenses."""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filterset_fields = ['date', 'description', 'amount']
    ordering_fields = ['date', 'amount']

class ExpenseDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete an expense."""
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filterset_fields = ['date', 'description', 'amount']
    lookup_field = 'id'

class FinancialPeriodList(generics.ListCreateAPIView):
    """API view to list and create financial periods."""
    queryset = FinancialPeriod.objects.all()
    serializer_class = FinancialPeriodSerializer
    filterset_fields = ['start_date', 'end_date', 'status']
    ordering_fields = ['start_date', 'end_date']

class FinancialPeriodDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a financial period."""
    queryset = FinancialPeriod.objects.all()
    serializer_class = FinancialPeriodSerializer
    filterset_fields = ['start_date', 'end_date', 'status']
    lookup_field = ['start_date', 'end_date', 'status']

# Note: The lookup_field is set to 'id' for the detail views, which is the default primary key field in Django models.
