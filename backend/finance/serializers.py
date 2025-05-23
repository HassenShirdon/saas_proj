from rest_framework import serializers
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

class AccountTypeSerializer(serializers.ModelSerializer):
    """Serializer for AccountType model."""
    class Meta:
        model = AccountType
        fields = '__all__'
        read_only_fields = ['id']

class AccountSerializer(serializers.ModelSerializer):
    """Serializer for Account model."""
    class Meta:
        model = Account
        fields = '__all__'
        read_only_fields = ['id']

class JournalEntryLineSerializer(serializers.ModelSerializer):
    """Serializer for JournalEntryLine model."""
    class Meta:
        model = JournalEntryLine
        fields = '__all__'
        read_only_fields = ['id']

class JournalEntrySerializer(serializers.ModelSerializer):
    """Serializer for JournalEntry model."""
    lines = JournalEntryLineSerializer(many=True)

    class Meta:
        model = JournalEntry
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        lines_data = validated_data.pop('lines')
        journal_entry = JournalEntry.objects.create(**validated_data)
        for line_data in lines_data:
            JournalEntryLine.objects.create(journal_entry=journal_entry, **line_data)
        return journal_entry
    
class SupplierInvoiceLineSerializer(serializers.ModelSerializer):
    """Serializer for SupplierInvoiceLine model."""
    class Meta:
        model = SupplierInvoiceLine
        fields = '__all__'
        read_only_fields = ['id']

class SupplierInvoiceSerializer(serializers.ModelSerializer):
    """Serializer for SupplierInvoice model."""
    lines = SupplierInvoiceLineSerializer(many=True)

    class Meta:
        model = SupplierInvoice
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        lines_data = validated_data.pop('lines')
        supplier_invoice = SupplierInvoice.objects.create(**validated_data)
        for line_data in lines_data:
            SupplierInvoiceLine.objects.create(supplier_invoice=supplier_invoice, **line_data)
        return supplier_invoice
    
class SupplierPaymentSerializer(serializers.ModelSerializer):
    """Serializer for SupplierPayment model."""
    class Meta:
        model = SupplierPayment
        fields = '__all__'
        read_only_fields = ['id']

class CustomerInvoiceLineSerializer(serializers.ModelSerializer):
    """Serializer for CustomerInvoiceLine model."""
    class Meta:
        model = CustomerInvoiceLine
        fields = '__all__'
        read_only_fields = ['id']

class CustomerInvoiceSerializer(serializers.ModelSerializer):
    """Serializer for CustomerInvoice model."""
    lines = CustomerInvoiceLineSerializer(many=True)

    class Meta:
        model = CustomerInvoice
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        lines_data = validated_data.pop('lines')
        customer_invoice = CustomerInvoice.objects.create(**validated_data)
        for line_data in lines_data:
            CustomerInvoiceLine.objects.create(customer_invoice=customer_invoice, **line_data)
        return customer_invoice

class CustomerPaymentSerializer(serializers.ModelSerializer):
    """Serializer for CustomerPayment model."""
    class Meta:
        model = CustomerPayment
        fields = '__all__'
        read_only_fields = ['id']

class ExpenseSerializer(serializers.ModelSerializer):
    """Serializer for Expense model."""
    class Meta:
        model = Expense
        fields = '__all__'
        read_only_fields = ['id']

class FinancialPeriodSerializer(serializers.ModelSerializer):
    """Serializer for FinancialPeriod model."""
    class Meta:
        model = FinancialPeriod
        fields = '__all__'
        read_only_fields = ['id']