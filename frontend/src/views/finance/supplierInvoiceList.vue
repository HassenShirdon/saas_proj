<template>
    <div class="container-fluid p-3">
        <div class="container d-flex justify-content-between align-items-center p-4 mb-4 shadow-sm ">
            <h1 class="h2 mb-0 ">Supplier Payments</h1>
            <button @click="addNewSupplierInvoice" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Payment
            </button>
        </div>
        <!-- loading state -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading Supplier Payments...</p>
        </div>
        <div class="table-responsive">
            <table class="table table-striped table-bordered table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">S.No</th>
                        <th scope="col">Payment Number</th>
                        <th scope="col">Supplier</th>
                        <th scope="col">Payment Date</th>
                        <th scope="col">Payment Method</th>
                        <th scope="col">Reference</th>
                        <th scope="col">Amount</th>
                        <th scope="col">Journal Entry</th>
                        <th scope="col">Notes</th>
                        <th scope="col">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(invoice, index) in displaySupplierInvoiceLists" :key="invoice.id || `new-${index}`"
                        :class="{ 'table-warning': invoice.isEditing || invoice.isNew }">
                        <th scope="row">{{ invoice.isNew ? 'New' : index + 1 }}</th>

                        <!-- payment number -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.payment_number"
                                type="number" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.payment_number`] }"
                                placeholder="Payment Number"
                                @blur="validateSupplierInvoiceField('payment_number', index)">
                            <div v-if="errors[`${index}.payment_number`]" class="invalid-feedback">
                                {{ errors[`${index}.payment_number`] }}</div>
                            <span v-else class="fw-semibold">{{ invoice.payment_number }}</span>
                        </td>

                        <!-- supplier -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.supplier" type="text"
                                class="form-control form-control-sm" placeholder="Supplier"
                                :class="{ 'is-invalid': errors[`${index}.supplier`] }"
                                @blur="validateSupplierInvoiceField('supplier', index)">
                            <div v-if="errors[`${index}.supplier`]" class="invalid-feedback">
                                {{ errors[`${index}.supplier`] }}
                            </div>
                            <span v-else class="text-muted">
                                {{ invoice.supplier }}
                            </span>
                        </td>

                        <!-- payment date -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.payment_date" type="date"
                                placeholder="Payment Date" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.payment_date`] }"
                                @blur="validateSupplierInvoiceField('payment_date', index)">
                            <div v-if="errors[`${index}.payment_date`]" class="invalid-feedback"></div>
                            <span v-else class="text-muted">
                                {{ formatDate(invoice.payment_date) }}
                            </span>
                        </td>

                        <!-- payment method -->
                        <td>
                            <select v-if="invoice.isEditing || invoice.isNew" v-model="invoice.payment_method"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.payment_method`] }"
                                @blur="validateSupplierInvoiceField('payment_method', index)">
                                <option value="">Select Method</option>
                                <option value="cash">Cash</option>
                                <option value="check">Check</option>
                                <option value="bank_transfer">Bank Transfer</option>
                                <option value="credit_card">Credit Card</option>
                                <option value="other">Other</option>
                            </select>
                            <div v-if="errors[`${index}.payment_method`]" class="invalid-feedback">
                                {{ errors[`${index}.payment_method`] }}
                            </div>
                            <span v-else class="text-muted">
                                {{ invoice.payment_method }}
                            </span>
                        </td>

                        <!-- reference -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.reference" type="text"
                                class="form-control form-control-sm" placeholder="Reference">
                            <span v-else class="text-muted">
                                {{ invoice.reference }}
                            </span>
                        </td>

                        <!-- amount -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.amount" type="number"
                                step="0.01" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.amount`] }" placeholder="Amount"
                                @blur="validateSupplierInvoiceField('amount', index)">
                            <div v-if="errors[`${index}.amount`]" class="invalid-feedback">
                                {{ errors[`${index}.amount`] }}
                            </div>
                            <span v-else class="text-muted">
                                {{ formatCurrency(invoice.amount) }}
                            </span>
                        </td>

                        <!-- journal entry -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.journal_entry" type="text"
                                class="form-control form-control-sm" placeholder="Journal Entry">
                            <span v-else class="text-muted">
                                {{ invoice.journal_entry }}
                            </span>
                        </td>

                        <!-- notes -->
                        <td>
                            <textarea v-if="invoice.isEditing || invoice.isNew" v-model="invoice.notes"
                                class="form-control form-control-sm" placeholder="Notes"></textarea>
                            <span v-else class="text-muted">
                                {{ invoice.notes }}
                            </span>
                        </td>

                        <td class="text-center">
                            <div v-if="invoice.isEditing || invoice.isNew" class="btn-group" role="group">
                                <button @click="handleSave(invoice, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save invoice">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editSupplierInvoice(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit invoice">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteSupplierInvoice(invoice.id, index)"
                                    class="btn btn-outline-danger btn-sm" title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup>
import { useSupplierInvoiceStore } from '@/stores/finance/supplierInvoiceStore';
import { ref, onMounted, computed } from 'vue';

const store = useSupplierInvoiceStore();
const loading = ref(false);
const errors = ref({});
const isSaving = ref(false);
const originalData = ref({});

const displaySupplierInvoiceLists = computed(() => {
    return store.supplierInvoices.map(invoice => ({
        ...invoice,
        isEditing: invoice.isEditing || false,
        isNew: invoice.isNew || false,
    }));
});

onMounted(() => {
    store.fetchSupplierInvoices()
});

const addNewSupplierInvoice = () => {
    const newInvoice = {
        id: null,
        payment_number: '',
        supplier: '',
        payment_date: new Date().toISOString().split('T')[0],
        payment_method: '',
        reference: '',
        amount: 0,
        journal_entry: '',
        notes: '',
        isEditing: true,
        isNew: true,
    };
    store.supplierInvoices.unshift(newInvoice);
};

const editSupplierInvoice = (index) => {
    store.supplierInvoices[index].isEditing = true;
    originalData.value[index] = { ...store.supplierInvoices[index] };
};

const cancelEdit = (index) => {
    const invoice = store.supplierInvoices[index];
    if (invoice.isNew) {
        store.supplierInvoices.splice(index, 1);
    } else {
        if (originalData.value[index]) {
            Object.assign(invoice, originalData.value[index]);
            delete originalData.value[index];
        }
        store.supplierInvoices[index].isEditing = false;
    }
    clearRowErrors(index)
}

const handleSave = async (invoice, index) => {
    try {
        isSaving.value = true;
        clearRowErrors(index);
        if (!validateSupplierInvoice(invoice, index)) {
            isSaving.value = false;
            return;
        }

        const invoiceData = {
            id: invoice.id || null,
            payment_number: invoice.payment_number,
            supplier: invoice.supplier,
            payment_date: invoice.payment_date,
            payment_method: invoice.payment_method,
            reference: invoice.reference,
            amount: parseFloat(invoice.amount),
            journal_entry: invoice.journal_entry,
            notes: invoice.notes?.trim() || '',
        };

        if (invoice.isNew) {
            await store.addSupplierInvoice(invoiceData);
            store.supplierInvoices.splice(index, 1)
            await store.fetchSupplierInvoices();
        } else {
            await store.updateSupplierInvoice(invoice.id, invoiceData);
            delete originalData.value[index];
        }
        console.log(`Payment ${invoice.isNew ? 'created' : 'updated'} successfully!`)
    } catch (error) {
        console.error('Error saving payment:', error)
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            alert('Failed to save payment. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateSupplierInvoice = (invoice, index) => {
    let isValid = true;

    if (!invoice.payment_number) {
        errors.value[`${index}.payment_number`] = 'Payment number is required';
        isValid = false;
    }

    if (!invoice.supplier?.trim()) {
        errors.value[`${index}.supplier`] = 'Supplier is required';
        isValid = false;
    }

    if (!invoice.payment_date) {
        errors.value[`${index}.payment_date`] = 'Payment date is required';
        isValid = false;
    }

    if (!invoice.payment_method) {
        errors.value[`${index}.payment_method`] = 'Payment method is required';
        isValid = false;
    }

    if (!invoice.amount || invoice.amount <= 0) {
        errors.value[`${index}.amount`] = 'Amount must be greater than 0';
        isValid = false;
    }

    return isValid;
};

const validateSupplierInvoiceField = (field, index) => {
    const invoice = store.supplierInvoices[index];
    const errorKey = `${index}.${field}`;
    delete errors.value[errorKey]; // Clear previous error

    switch (field) {
        case 'payment_number':
            if (!invoice.payment_number) {
                errors.value[errorKey] = 'Payment number is required';
            }
            break;

        case 'supplier':
            if (!invoice.supplier?.trim()) {
                errors.value[errorKey] = 'Supplier is required';
            }
            break;

        case 'payment_date':
            if (!invoice.payment_date) {
                errors.value[errorKey] = 'Payment date is required';
            }
            break;

        case 'payment_method':
            if (!invoice.payment_method) {
                errors.value[errorKey] = 'Payment method is required';
            }
            break;

        case 'amount':
            if (!invoice.amount || invoice.amount <= 0) {
                errors.value[errorKey] = 'Amount must be greater than 0';
            }
            break;
    }
};

const handleBackendErrors = (backendErrors, index) => {
    Object.keys(backendErrors).forEach(field => {
        const errorKey = `${index}.${field}`
        errors.value[errorKey] = Array.isArray(backendErrors[field])
            ? backendErrors[field][0]
            : backendErrors[field]
    })
}

const clearRowErrors = (index) => {
    Object.keys(errors.value).forEach(key => {
        if (key.startsWith(`${index}.`)) {
            delete errors.value[key]
        }
    })
}

const deleteSupplierInvoice = async (id, index) => {
    if (confirm('Are you sure you want to delete this payment? This action cannot be undone.')) {
        try {
            await store.removeSupplierInvoice(id)
        } catch (error) {
            console.error('Error deleting payment:', error)
            alert('Failed to delete payment. Please try again.')
        }
    }
}

const formatDate = (dateString) => {
    if (!dateString) return '-'
    return new Date(dateString).toLocaleDateString()
}

const formatCurrency = (amount) => {
    if (amount === null || amount === undefined) return '-'
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(amount)
}
</script>

<style scoped>
.table-responsive {
    border-radius: 0.375rem;
    overflow: hidden;
    box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
}

.table {
    margin-bottom: 0;
}

.btn-group .btn {
    margin: 0 1px;
}

.text-truncate {
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.table-warning {
    background-color: #fff3cd !important;
}

.form-control-sm,
.form-select-sm {
    min-width: 120px;
}

textarea.form-control-sm {
    min-width: 150px;
    resize: vertical;
}

.invalid-feedback {
    display: block;
    font-size: 0.75rem;
}

@media (max-width: 768px) {
    .table-responsive {
        font-size: 0.875rem;
    }

    .btn-sm {
        padding: 0.25rem 0.5rem;
        font-size: 0.75rem;
    }

    .form-control-sm,
    .form-select-sm {
        min-width: 100px;
    }
}
</style>