<template>
    <div class="container-fluid p-3">
        <div class="container d-flex justify-content-between align-items-center p-4 mb-4 shadow-sm ">
            <h1 class="h2 mb-0 ">Supplier Inovices</h1>
            <button @click="addNewSupplierInvoice" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Journal Entry
            </button>
        </div>
        <!-- loading state -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading Supplier Inovices...</p>
        </div>
        <div class="table-responsive">
            <table class="table table-striped table-bordered table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">S.No</th>
                        <th scope="col">Invoice Number</th>
                        <th scope="col">Invoice Date</th>
                        <th scope="col">Due Date</th>
                        <th scope="col">Total Amount</th>
                        <th scope="col">Tax Amount</th>
                        <th scope="col">Status</th>
                        <th scope="col">Supplier</th>
                        <th scope="col">Purchase Order</th>
                        <th scope="col">Journal Entry</th>
                        <th scope="col">Notes</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(supplierInvoice, index) in displaySupplierInvoiceLists"
                        :key="supplierInvoice.id || `new-${index}`"
                        :class="{ 'table-warning': supplierInvoice.isEditing || supplierInvoice.isNew }">
                        <th scope="row">{{ supplierInvoice.isNew ? 'New' : index + 1 }}</th>

                        <td>
                            <input v-model="supplierInvoice.invoice_number" type="number"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.invoice_number`] }"
                                @blur="validateSupplierInvoiceField('invoice_number', index)">
                            <div class="invalid-feedback">{{ errors[`${index}.invoice_number`] }}</div>
                        </td>

                        <td>
                            <input v-if="supplierInvoice.isEditing || supplierInvoice.isNew"
                                v-model="supplierInvoice.invoice_date" type="date" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.invoice_date`] }"
                                @blur="validateSupplierInvoiceField('invoice_date', index)">
                            <div v-if="errors[`${index}.invoice_date`]" class="invalid-feedback">
                                {{ errors[`${index}.invoice_date`] }}
                            </div>
                            <span v-else class="text-muted">
                                {{ formatDate(supplierInvoice.invoice_date) }}
                            </span>
                        </td>

                        <td>
                            <input v-if="supplierInvoice.isEditing || supplierInvoice.isNew"
                                v-model="supplierInvoice.due_date" type="date" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.due_date`] }"
                                @blur="validateSupplierInvoiceField('due_date', index)">
                            <div class="invalid-feedback">{{ errors[`${index}.due_date`] }}</div>
                        </td>
                        <td>
                            <input v-if="supplierInvoice.isEditing || supplierInvoice.isNew"
                                v-model="supplierInvoice.total_amount" type="number"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.total_amount`] }"
                                @blur="validateSupplierInvoiceField('total_amount', index)">
                            <div v-if="errors[`${index}.total_amount`]" class="invalid-feedback">
                                {{ errors[`${index}.total_amount`] }}
                            </div>
                            <span v-else class="text-muted">
                                {{ supplierInvoice.total_amount }}
                            </span>
                        </td>

                        <td>
                            <input v-if="supplierInvoice.isEditing || supplierInvoice.isNew"
                                v-model="supplierInvoice.tax_amount" type="number" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.tax_amount`] }"
                                @blur="validateSupplierInvoiceField('tax_amount', index)">
                            <div v-if="errors[`${index}.tax_amount`]" class="invalid-feedback">
                                {{ errors[`${index}.tax_amount`] }}
                            </div>
                        </td>
                        <td>
                            <input <input v-if="supplierInvoice.isEditing || supplierInvoice.isNew"
                                v-model="supplierInvoice.status" type="text" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.status`] }"
                                @blur="validateSupplierInvoiceField('status', index)">
                            <div v-if="errors[`${index}.status`]" class="invalid-feedback">
                                {{ errors[`${index}.status`] }}
                            </div>
                        </td>

                        <td>
                            <input <input v-if="supplierInvoice.isEditing || supplierInvoice.isNew"
                                v-model="supplierInvoice.supplier" type="text" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.supplier`] }"
                                @blur="validateSupplierInvoiceField('supplier', index)">
                            <div v-if="errors[`${index}.supplier`]" class="invalid-feedback">
                                {{ errors[`${index}.supplier`] }}
                            </div>
                        </td>
                        <td>
                            <input <input v-if="supplierInvoice.isEditing || supplierInvoice.isNew"
                                v-model="supplierInvoice.purchase_order" type="text"
                                class="form-control form-control-sm">
                            <div v-if="errors[`${index}.purchase_order`]" class="invalid-feedback">
                                {{ errors[`${index}.purchase_order`] }}
                            </div>
                        </td>
                        <td>
                            <input <input v-if="supplierInvoice.isEditing || supplierInvoice.isNew"
                                v-model="supplierInvoice.journal_entry" type="text" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.journal_entry`] }"
                                @blur="validateSupplierInvoiceField('journal_entry', index)">
                            <div v-if="errors[`${index}.journal_entry`]" class="invalid-feedback">
                                {{ errors[`${index}.journal_entry`] }}
                            </div>
                        </td>
                        <td>
                            <textarea <input v-if="supplierInvoice.isEditing || supplierInvoice.isNew"
                                v-model="supplierInvoice.notes" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.notes`] }"
                                @blur="validateSupplierInvoiceField('notes', index)"></textarea>
                            <div v-if="errors[`${index}.notes`]" class="invalid-feedback">
                                {{ errors[`${index}.notes`] }}
                            </div>
                        </td>
                        <td class="text-center">
                            <div v-if="supplierInvoice.isEditing || supplierInvoice.isNew" class="btn-group"
                                role="group">
                                <button @click="handleSave(supplierInvoice, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save supplierInvoice">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editSupplierInvoice(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit supplierInvoice">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteSupplierInvoice(supplierInvoice.id, index)"
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
    return store.supplierInvoiceLists.map(supplierInvoice => ({
        ...supplierInvoice,
        isEditing: supplierInvoice.isEditing || false,
        isNew: supplierInvoice.isNew || false,
    }));
});


onMounted(() => {

    store.fetchSupplierInvoices()
});

const addNewSupplierInvoice = () => {
    const newSupplierInvoice = {
        id: null,
        invoice_number: 0,
        invoice_date: new Date(),
        due_date: new Date(),
        total_amount: 0,
        tax_amount: 0,
        status: '',
        notes: '',
        supplier: '',
        purchase_order: '',
        journal_entry: '',
        isEditing: true,
        isNew: true,
    };
    store.supplierInvoiceLists.unshift(newSupplierInvoice);
};

const editSupplierInvoice = (index) => {
    store.supplierInvoiceLists[index].isEditing = true;
    originalData.value = { ...store.supplierInvoiceLists[index] };

};
const cancelEdit = (index) => {
    const supplierInvoice = store.supplierInvoiceLists[index];
    if (supplierInvoice.isNew) {
        store.supplierInvoiceLists.splice(index, 1);
    } else {
        if (!originalData.value[index]) {
            Object.assign(supplierInvoice, originalData.value);
            delete originalData.value[index];
        }
        supplierInvoice.isEditing = false;
    }
    clearRowErrors(index)
}

const handleSave = async (index) => {
    try {
        isSaving.value = true;
        clearRowErrors(index);
        if (!validateSupplierInvoice(supplierInvoice, index)) {
            isSaving.value = false;
            return;
        }

        const supplierInvoiceData = {
            id: Date.now(),
            invoice_number: supplierInvoice.invoice_number || 0,
            invoice_date: supplierInvoice.invoice_date.date() || new Date(),
            due_date: supplierInvoice.due_date.date() || new Date(),
            total_amount: supplierInvoice.total_amount || 0,
            tax_amount: supplierInvoice.tax_amount || 0,
            status: supplierInvoice.status || '',
            notes: supplierInvoice.notes?.trim() || '',
            supplier: supplierInvoice.supplier || '',
            purchase_order: supplierInvoice.purchase_order || '',
            journal_entry: supplierInvoice.journal_entry || '',

        }
        if (supplierInvoice.isNew) {
            await store.addSupplierInvoice(supplierInvoiceData);
            store.supplierInvoiceLists.splice(index, 1)
            await store.fetchSupplierInvoiceLists();

        } else {
            await store.updateSupplierInvoice(supplierInvoice.id, supplierInvoiceData);
            delete originalData.value[index];

        } console.log(`SupplierInvoice ${SupplierInvoice.isNew ? 'created' : 'updated'} successfully!`)
    } catch (error) {
        console.error('Error saving SupplierInvoice:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save SupplierInvoice. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateSupplierInvoice = (invoice, index) => {
    let isValid = true;

    if (!invoice.invoice_date) {
        errors.value[`${index}.invoice_date`] = 'Invoice date is required';
        isValid = false;
    }

    if (!invoice.due_date) {
        errors.value[`${index}.due_date`] = 'Due date is required';
        isValid = false;
    }

    if (!invoice.total_amount || invoice.total_amount <= 0) {
        errors.value[`${index}.total_amount`] = 'Total amount must be greater than 0';
        isValid = false;
    }

    if (invoice.tax_amount && invoice.tax_amount < 0) {
        errors.value[`${index}.tax_amount`] = 'Tax amount cannot be negative';
        isValid = false;
    }

    if (!invoice.status?.trim()) {
        errors.value[`${index}.status`] = 'Status is required';
        isValid = false;
    }

    if (!invoice.supplier?.trim()) {
        errors.value[`${index}.supplier`] = 'Supplier is required';
        isValid = false;
    }

    // Optional fields: journal_entry, notes, purchase_order

    return isValid;
};

const validateSupplierInvoiceField = (field, index) => {
    const invoice = store.supplierInvoiceLists[index];
    const errorKey = `${index}.${field}`;
    delete errors.value[errorKey]; // Clear previous error

    switch (field) {
        case 'invoice_date':
            if (!invoice.invoice_date) {
                errors.value[errorKey] = 'Invoice date is required';
            }
            break;

        case 'due_date':
            if (!invoice.due_date) {
                errors.value[errorKey] = 'Due date is required';
            }
            break;

        case 'total_amount':
            if (!invoice.total_amount || invoice.total_amount <= 0) {
                errors.value[errorKey] = 'Total amount must be greater than 0';
            }
            break;

        case 'tax_amount':
            if (invoice.tax_amount && invoice.tax_amount < 0) {
                errors.value[errorKey] = 'Tax amount cannot be negative';
            }
            break;

        case 'status':
            if (!invoice.status?.trim()) {
                errors.value[errorKey] = 'Status is required';
            }
            break;

        case 'supplier':
            if (!invoice.supplier?.trim()) {
                errors.value[errorKey] = 'Supplier is required';
            }
            break;

        case 'journal_entry':
            if (!invoice.journal_entry?.trim()) {
                errors.value[errorKey] = 'Journal entry is required';
            }
            break;

        case 'purchase_order':
            // Add validation if purchase_order is required
            break;

        case 'notes':
            // Notes are optional
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
    if (confirm('Are you sure you want to delete this Supplier Invoice ? this action cannot be undone.')) {
        try {
            await store.removeSupplierInvoice(id)
        } catch (error) {
            console.error('Error deleting SupplierInvoice:', error)
            alert('Failed to delete Supplier Invoice. Please try again.')
        }
    }
}
const formatDate = (dateString) => {
    if (!dateString) return '-'
    return new Date(dateString).toLocaleDateString()
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