<template>
    <!-- Your template content here -->
    <div class="container-fluid p-3">
        <div class="container d-flex justify-content-between align-items-center p-4 mb-4 shadow-sm ">
            <h1 class="h2 mb-0 ">Customer Inovices</h1>
            <button @click="addNewCustomerInvoice" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Customer Invoice
            </button>
        </div>
        <!-- loading state -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading Customer Inovices...</p>
        </div>
        <div class="table-responsive">
            <table class="table table-striped table-bordered table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">S.No</th>
                        <th scope="col">Invoice Number</th>
                        <th scope="col">Customer</th>
                        <th scope="col">sales_order</th>
                        <th scope="col">Invoice Date</th>
                        <th scope="col">Due Date</th>
                        <th scope="col">Total Amount</th>
                        <th scope="col">Tax Amount</th>
                        <th scope="col">Status</th>
                        <th scope="col">Journal Entry</th>
                        <th scope="col">Notes</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(invoice, index) in displayCustomerInvoiceLists" :key="invoice.id || `new-${index}`"
                        :class="{ 'table-warning': invoice.isEditing || invoice.isNew }">
                        <th scope="row">{{ invoice.isNew ? 'New' : index + 1 }}</th>

                        <!-- invoice number -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.invoice_number"
                                type="number" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.invoice_number`] }"
                                placeholder="Payment Number"
                                @blur="validateCustomerInvoiceField('invoice_number', index)">
                            <div v-if="errors[`${index}.invoice_number`]" class="invalid-feedback">
                                {{ errors[`${index}.invoice_number`] }}</div>
                            <span v-else class="fw-semibold">{{ invoice.invoice_number }}</span>
                        </td>
                        <!-- Customer -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.customer" type="text"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.customer`] }" placeholder="Customer"
                                @blur="validateCustomerInvoiceField('customer', index)"/>
                            <div v-if="errors[`${index}.customer`]" class="invalid-feedback">
                                {{ errors[`${index}.customer`] }}</div>
                            <span v-else class="fw-semibold">{{ invoice.customer }}</span>
                        </td>
                        <!-- sales_order -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.sales_order" type="text"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.sales_order`] }" placeholder="Sales Order"
                                @blur="validateCustomerInvoiceField('sales_order', index)">
                            <div v-if="errors[`${index}.sales_order`]" class="invalid-feedback">
                                {{ errors[`${index}.sales_order`] }}</div>
                            <span v-else class="fw-semibold">{{ invoice.sales_order }}</span>
                        </td>
                        <!-- Invoice Date -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.invoice_date" type="date"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.invoice_date`] }"
                                @blur="validateCustomerInvoiceField('invoice_date', index)">
                            <div v-if="errors[`${index}.invoice_date`]" class="invalid-feedback">
                                {{ errors[`${index}.invoice_date`] }}</div>
                            <span v-else class="fw-semibold">{{ formatDate(invoice.invoice_date) }}</span>
                        </td>
                        <!-- Due Date -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.due_date" type="date"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.due_date`] }"
                                @blur="validateCustomerInvoiceField('due_date', index)">
                            <div v-if="errors[`${index}.due_date`]" class="invalid-feedback">
                                {{ errors[`${index}.due_date`] }}</div>
                            <span v-else class="fw-semibold">{{ formatDate(invoice.due_date) }}</span>
                        </td>
                        <!-- Total Amount -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model.number="invoice.total_amount"
                                type="number" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.total_amount`] }" placeholder="Total Amount"
                                @blur="validateCustomerInvoiceField('total_amount', index)">
                            <div v-if="errors[`${index}.total_amount`]" class="invalid-feedback">
                                {{ errors[`${index}.total_amount`] }}</div>
                            <span v-else class="fw-semibold">{{ invoice.total_amount.toFixed(2) }}</span>
                        </td>

                        <!-- Tax Amount -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model.number="invoice.tax_amount"
                                type="number" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.tax_amount`] }" placeholder="Tax Amount"
                                @blur="validateCustomerInvoiceField('tax_amount', index)">
                            <div v-if="errors[`${index}.tax_amount`]" class="invalid-feedback">
                                {{ errors[`${index}.tax_amount`] }}</div>
                            <span v-else class="fw-semibold">{{ invoice.tax_amount.toFixed(2) }}</span>
                        </td>
                        <!-- Status -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.status" type="text"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.status`] }" placeholder="Status"
                                @blur="validateCustomerInvoiceField('status', index)">
                            <div v-if="errors[`${index}.status`]" class="invalid-feedback">
                                {{ errors[`${index}.status`] }}</div>
                            <span v-else class="fw-semibold">{{ invoice.status }}</span>
                        </td>
                        <!-- Journal Entry -->
                        <td>
                            <input v-if="invoice.isEditing || invoice.isNew" v-model="invoice.journal_entry" type="text"
                                class="form-control form-control-sm" placeholder="Journal Entry">
                            <span v-else class="fw-semibold">{{ invoice.journal_entry }}</span>
                        </td>
                        <!-- Notes -->
                        <td>
                            <textarea v-if="invoice.isEditing || invoice.isNew" v-model="invoice.notes"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.notes`] }"
                                placeholder="Notes" @blur="validateCustomerInvoiceField('notes', index)"></textarea>
                            <div v-if="errors[`${index}.notes`]" class="invalid-feedback">
                                {{ errors[`${index}.notes`] }}</div>
                            <span v-else class="fw-semibold">{{ invoice.notes }}</span>
                        </td>
                        <!-- Actions -->
                        <td class="text-center">
                            <div class="btn-group" role="group">
                                <button v-if="invoice.isEditing || invoice.isNew" @click="handleSave(index)"
                                    class="btn btn-success btn-sm" :disabled="isSaving">
                                    <i class="fas fa-save"></i>
                                    Save
                                </button>
                                <button v-else @click="editCustomerInvoice(index)" class="btn btn-primary btn-sm">
                                    <i class="fas fa-edit"></i>
                                    Edit
                                </button>
                                <button v-if="!invoice.isNew" @click="deleteCustomerInvoice(invoice.id, index)"
                                    class="btn btn-danger btn-sm">
                                    <i class="fas fa-trash"></i>
                                    Delete
                                </button>
                                <button v-if="invoice.isEditing || invoice.isNew" @click="cancelEdit(index)"
                                    class="btn btn-secondary btn-sm">
                                    <i class="fas fa-times"></i>
                                    Cancel
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
import { ref, onMounted, computed } from 'vue'
import { useCustomerInvoiceStore } from '@/stores/finance/customerInvoiceStore'

const store = useCustomerInvoiceStore()
const loading = ref(false)
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

const displayCustomerInvoiceLists = computed(() => {
    return store.customerInvoices.map(invoice => ({
        ...invoice,
        isEditing: invoice.isEditing || false,
        isNew: invoice.isNew || false
    }))
})

onMounted(() => {
    store.fetchCustomerInvoices()
})

const addNewCustomerInvoice = () => {
    const newCustomerInvoice = {
        invoice_number: '',
        customer: '',
        sales_order: '',
        invoice_date: '',
        due_date: '',
        total_amount: 0,
        tax_amount: 0,
        status: '',
        journal_entry: null,
        notes: '',
        created_at: new Date().toISOString(),
        updated_at: new Date().toISOString(),
        isNew: true,
        isEditing: true
    }
    store.customerInvoices.push(newCustomerInvoice)
}

const editCustomerInvoice = (index) => {
    store.customerInvoices[index].isEditing = true
    originalData.value[index] = { ...store.customerInvoices[index] }
}

const cancelEdit = (index) => {
    const customerInvoice = store.customerInvoices[index]
    if (customerInvoice.isNew) {
        store.customerInvoices.splice(index, 1)
    } else {
        if (originalData.value[index]) {
            Object.assign(store.customerInvoices[index], originalData.value)
            delete originalData.value[index]
        }
        store.customerInvoices[index].isEditing = false
    }
    clearRowErrors(index)
}

const handleSave = async (index) => {
    try {
        isSaving.value = true
        clearRowErrors(index)
        const customerInvoice = store.customerInvoices[index]

        if (!validateCustomerInvoice(customerInvoice, index)) {
            isSaving.value = false
            return
        }

        const customerInvoiceData = {
            id: customerInvoice.id || null,
            invoice_number: customerInvoice.invoice_number || '',
            customer: customerInvoice.customer.trim() || '',
            sales_order: customerInvoice.sales_order || '',
            invoice_date: customerInvoice.invoice_date || '',
            due_date: customerInvoice.due_date || '',
            total_amount: customerInvoice.total_amount || 0,
            tax_amount: customerInvoice.tax_amount || 0,
            status: customerInvoice.status || '',
            journal_entry: customerInvoice.journal_entry || null,
            notes: customerInvoice.notes || '',
            created_at: customerInvoice.created_at || new Date().toISOString(),
            updated_at: customerInvoice.updated_at || new Date().toISOString()
        }

        if (customerInvoice.isNew) {
            await store.createCustomerInvoice(customerInvoiceData)
            store.customerInvoices.splice(index, 1)
            await store.fetchCustomerInvoices()
        } else {
            await store.updateCustomerInvoice(customerInvoice.id, customerInvoiceData)
            delete originalData.value[index]
        }
        console.log(`customerInvoice ${customerInvoice.isNew ? 'created' : 'updated'} successfully!`)
    } catch (error) {
        console.error('Error saving CustomerInvoice:', error)

        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            alert('Failed to save CustomerInvoice. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateCustomerInvoice = (invoice, index) => {
    let isValid = true

    if (!invoice.invoice_number?.trim()) {
        errors.value[`${index}.invoice_number`] = 'Invoice number is required'
        isValid = false
    }

    if (!invoice.customer) {
        errors.value[`${index}.customer`] = 'Customer is required'
        isValid = false
    }

    if (!invoice.invoice_date) {
        errors.value[`${index}.invoice_date`] = 'Invoice date is required'
        isValid = false
    }

    if (!invoice.due_date) {
        errors.value[`${index}.due_date`] = 'Due date is required'
        isValid = false
    }

    if (!invoice.total_amount || invoice.total_amount <= 0) {
        errors.value[`${index}.total_amount`] = 'Total amount must be greater than 0'
        isValid = false
    }

    if (invoice.tax_amount && invoice.tax_amount < 0) {
        errors.value[`${index}.tax_amount`] = 'Tax amount cannot be negative'
        isValid = false
    }

    if (!invoice.status?.trim()) {
        errors.value[`${index}.status`] = 'Status is required'
        isValid = false
    }

    return isValid
}

const validateCustomerInvoiceField = (field, index) => {
    const invoice = store.customerInvoices[index]
    const errorKey = `${index}.${field}`
    delete errors.value[errorKey]

    switch (field) {
        case 'invoice_number':
            if (!invoice.invoice_number?.trim()) {
                errors.value[errorKey] = 'Invoice number is required'
            }
            break

        case 'customer':
            if (!invoice.customer) {
                errors.value[errorKey] = 'Customer is required'
            }
            break

        case 'invoice_date':
            if (!invoice.invoice_date) {
                errors.value[errorKey] = 'Invoice date is required'
            }
            break

        case 'due_date':
            if (!invoice.due_date) {
                errors.value[errorKey] = 'Due date is required'
            }
            break

        case 'total_amount':
            if (!invoice.total_amount || invoice.total_amount <= 0) {
                errors.value[errorKey] = 'Total amount must be greater than 0'
            }
            break

        case 'tax_amount':
            if (invoice.tax_amount && invoice.tax_amount < 0) {
                errors.value[errorKey] = 'Tax amount cannot be negative'
            }
            break

        case 'status':
            if (!invoice.status?.trim()) {
                errors.value[errorKey] = 'Status is required'
            }
            break
    }
}

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

const deleteCustomerInvoice = async (id, index) => {
    if (confirm('Are you sure you want to delete this Customer Invoice? This action cannot be undone.')) {
        try {
            await store.removeCustomerInvoice(id)
        } catch (error) {
            console.error('Error deleting CustomerInvoice:', error)
            alert('Failed to delete Customer Invoice. Please try again.')
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