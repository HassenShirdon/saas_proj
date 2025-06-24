<!-- src/views/PurchaseOrders/PurchaseOrderList.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Purchase Order List</h1>
            <button @click="addNewPurchaseOrder" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Purchase Order
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading purchase orders...</p>
        </div>

        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">PO Number</th>
                        <th scope="col">Supplier</th>
                        <th scope="col">Order Date</th>
                        <th scope="col">Delivery Date</th>
                        <th scope="col">Total Amount</th>
                        <th scope="col">Tax Amount</th>
                        <th scope="col">Status</th>
                        <th scope="col">Notes</th>
                        <th scope="col">Created At</th>
                        <th scope="col">Updated At</th>
                        <th class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(purchaseOrder, index) in displayPurchaseOrders"
                        :key="purchaseOrder.id || `new-${index}`"
                        :class="{ 'table-warning': purchaseOrder.isEditing || purchaseOrder.isNew }">

                        <!-- PO Number Field -->
                        <td>
                            <input v-if="purchaseOrder.isEditing || purchaseOrder.isNew"
                                v-model="purchaseOrder.po_number" type="text" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.po_number`] }"
                                placeholder="PO Number (auto-generated if empty)"
                                @blur="validateField(index, 'po_number')" />
                            <div v-if="errors[`${index}.po_number`]" class="invalid-feedback">
                                {{ errors[`${index}.po_number`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ purchaseOrder.po_number }}</span>
                        </td>

                        <!-- Supplier Field -->
                        <td>
                            <select v-if="purchaseOrder.isEditing || purchaseOrder.isNew"
                                v-model="purchaseOrder.supplier" class="form-select form-select-sm"
                                :class="{ 'is-invalid': errors[`${index}.supplier`] }"
                                @blur="validateField(index, 'supplier')">
                                <option value="">Select Supplier</option>
                                <option v-for="supplier in suppliers" :key="supplier.id" :value="supplier.id">
                                    {{ supplier.name }}
                                </option>
                            </select>
                            <div v-if="errors[`${index}.supplier`]" class="invalid-feedback">
                                {{ errors[`${index}.supplier`] }}
                            </div>
                            <span v-else>{{ getSupplierName(purchaseOrder.supplier) || '-' }}</span>
                        </td>

                        <!-- Order Date Field -->
                        <td>
                            <input v-if="purchaseOrder.isEditing || purchaseOrder.isNew"
                                v-model="purchaseOrder.order_date" type="date" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.order_date`] }"
                                @blur="validateField(index, 'order_date')" />
                            <div v-if="errors[`${index}.order_date`]" class="invalid-feedback">
                                {{ errors[`${index}.order_date`] }}
                            </div>
                            <span v-else>{{ formatDate(purchaseOrder.order_date) }}</span>
                        </td>

                        <!-- Delivery Date Field -->
                        <td>
                            <input v-if="purchaseOrder.isEditing || purchaseOrder.isNew"
                                v-model="purchaseOrder.delivery_date" type="date" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.delivery_date`] }"
                                @blur="validateField(index, 'delivery_date')" />
                            <div v-if="errors[`${index}.delivery_date`]" class="invalid-feedback">
                                {{ errors[`${index}.delivery_date`] }}
                            </div>
                            <span v-else>{{ formatDate(purchaseOrder.delivery_date) }}</span>
                        </td>

                        <!-- Total Amount Field -->
                        <td>
                            <input v-if="purchaseOrder.isEditing || purchaseOrder.isNew"
                                v-model="purchaseOrder.total_amount" type="number" step="0.01" min="0"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.total_amount`] }" placeholder="0.00"
                                @blur="validateField(index, 'total_amount')" />
                            <div v-if="errors[`${index}.total_amount`]" class="invalid-feedback">
                                {{ errors[`${index}.total_amount`] }}
                            </div>
                            <span v-else>${{ formatCurrency(purchaseOrder.total_amount) }}</span>
                        </td>

                        <!-- Tax Amount Field -->
                        <td>
                            <input v-if="purchaseOrder.isEditing || purchaseOrder.isNew"
                                v-model="purchaseOrder.tax_amount" type="number" step="0.01" min="0"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.tax_amount`] }" placeholder="0.00"
                                @blur="validateField(index, 'tax_amount')" />
                            <div v-if="errors[`${index}.tax_amount`]" class="invalid-feedback">
                                {{ errors[`${index}.tax_amount`] }}
                            </div>
                            <span v-else>${{ formatCurrency(purchaseOrder.tax_amount) }}</span>
                        </td>

                        <!-- Status Field -->
                        <td>
                            <select v-if="purchaseOrder.isEditing || purchaseOrder.isNew" v-model="purchaseOrder.status"
                                class="form-select form-select-sm" :class="{ 'is-invalid': errors[`${index}.status`] }">
                                <option value="draft">Draft</option>
                                <option value="sent">Sent</option>
                                <option value="partially_received">Partially Received</option>
                                <option value="received">Received</option>
                                <option value="completed">Completed</option>
                                <option value="cancelled">Cancelled</option>
                            </select>
                            <div v-if="errors[`${index}.status`]" class="invalid-feedback">
                                {{ errors[`${index}.status`] }}
                            </div>
                            <span v-else :class="getStatusClass(purchaseOrder.status)">
                                {{ formatStatus(purchaseOrder.status) }}
                            </span>
                        </td>

                        <!-- Notes Field -->
                        <td>
                            <textarea v-if="purchaseOrder.isEditing || purchaseOrder.isNew"
                                v-model="purchaseOrder.notes" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.notes`] }" placeholder="Notes"
                                @blur="validateField(index, 'notes')"></textarea>
                            <div v-if="errors[`${index}.notes`]" class="invalid-feedback">
                                {{ errors[`${index}.notes`] }}
                            </div>
                            <span v-else class="text-truncate" :title="purchaseOrder.notes">{{ purchaseOrder.notes ||
                                '-' }}</span>
                        </td>

                        <!-- Created At -->
                        <td>
                            <span v-if="purchaseOrder.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(purchaseOrder.created_at) }}</span>
                        </td>

                        <!-- Updated At -->
                        <td>
                            <span v-if="purchaseOrder.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(purchaseOrder.updated_at) }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="purchaseOrder.isEditing || purchaseOrder.isNew" class="btn-group" role="group">
                                <button @click="handleSave(purchaseOrder, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Purchase Order">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editPurchaseOrder(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Purchase Order">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deletePurchaseOrder(purchaseOrder.id, index)"
                                    class="btn btn-outline-danger btn-sm" title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.purchaseOrders.length === 0 && displayPurchaseOrders.length === 0"
                class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-file-invoice fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No Purchase Orders found</h5>
                <p class="text-muted">Start by creating your first Purchase Order</p>
                <button @click="addNewPurchaseOrder" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Purchase Order
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { usePurchaseOrderStore } from '@/stores/inventory/purchaseOrderStore'
import { useSupplierStore } from '@/stores/inventory/supplierStore'

const store = usePurchaseOrderStore()
const supplierStore = useSupplierStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

const displayPurchaseOrders = computed(() => {
    return store.purchaseOrders.map(purchaseOrder => ({
        ...purchaseOrder,
        isEditing: purchaseOrder.isEditing || false,
        isNew: purchaseOrder.isNew || false
    }))
})

const suppliers = computed(() => {
    return supplierStore.suppliers || []
})

onMounted(() => {
    store.fetchPurchaseOrders()
    supplierStore.fetchSuppliers()
})

const addNewPurchaseOrder = () => {
    const newPurchaseOrder = {
        id: null,
        po_number: '',
        supplier: '',
        order_date: new Date().toISOString().split('T')[0],
        delivery_date: '',
        total_amount: 0,
        tax_amount: 0,
        status: 'draft',
        notes: '',
        created_at: null,
        updated_at: null,
        isNew: true,
        isEditing: true
    }
    store.purchaseOrders.unshift(newPurchaseOrder)
}

const editPurchaseOrder = (index) => {
    originalData.value[index] = { ...store.purchaseOrders[index] }
    store.purchaseOrders[index].isEditing = true
}

const cancelEdit = (index) => {
    const purchaseOrder = store.purchaseOrders[index]
    if (purchaseOrder.isNew) {
        store.purchaseOrders.splice(index, 1)
    } else {
        if (originalData.value[index]) {
            Object.assign(store.purchaseOrders[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.purchaseOrders[index].isEditing = false
    }
    clearRowErrors(index)
}

const handleSave = async (purchaseOrder, index) => {
    try {
        isSaving.value = true
        clearRowErrors(index)

        if (!validatePurchaseOrder(purchaseOrder, index)) {
            isSaving.value = false
            return
        }

        const purchaseOrderData = {
            po_number: purchaseOrder.po_number?.trim() || '',
            supplier: purchaseOrder.supplier,
            order_date: purchaseOrder.order_date,
            delivery_date: purchaseOrder.delivery_date || null,
            total_amount: parseFloat(purchaseOrder.total_amount) || 0,
            tax_amount: parseFloat(purchaseOrder.tax_amount) || 0,
            status: purchaseOrder.status,
            notes: purchaseOrder.notes?.trim() || ''
        }

        if (purchaseOrder.isNew) {
            await store.addPurchaseOrder(purchaseOrderData)
            store.purchaseOrders.splice(index, 1)
            await store.fetchPurchaseOrders()
        } else {
            await store.updatePurchaseOrder(purchaseOrder.id, purchaseOrderData)
            store.purchaseOrders[index].isEditing = false
            delete originalData.value[index]
        }

        console.log(`Purchase Order ${purchaseOrder.isNew ? 'created' : 'updated'} successfully!`)
    } catch (error) {
        console.error('Error saving purchase order:', error)
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            alert('Failed to save purchase order. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validatePurchaseOrder = (purchaseOrder, index) => {
    let isValid = true
    errors.value = {}

    // PO Number is optional since it's auto-generated
    if (purchaseOrder.po_number && purchaseOrder.po_number.length > 50) {
        errors.value[`${index}.po_number`] = 'PO number must be less than 50 characters'
        isValid = false
    }

    if (!purchaseOrder.supplier) {
        errors.value[`${index}.supplier`] = 'Supplier is required'
        isValid = false
    }

    if (!purchaseOrder.order_date) {
        errors.value[`${index}.order_date`] = 'Order date is required'
        isValid = false
    }

    if (purchaseOrder.total_amount < 0) {
        errors.value[`${index}.total_amount`] = 'Total amount cannot be negative'
        isValid = false
    }

    if (purchaseOrder.tax_amount < 0) {
        errors.value[`${index}.tax_amount`] = 'Tax amount cannot be negative'
        isValid = false
    }

    if (purchaseOrder.delivery_date && purchaseOrder.order_date) {
        const orderDate = new Date(purchaseOrder.order_date)
        const deliveryDate = new Date(purchaseOrder.delivery_date)
        if (deliveryDate < orderDate) {
            errors.value[`${index}.delivery_date`] = 'Delivery date cannot be before order date'
            isValid = false
        }
    }

    return isValid
}

const validateField = (index, field) => {
    const purchaseOrder = store.purchaseOrders[index]
    const errorKey = `${index}.${field}`
    delete errors.value[errorKey]

    switch (field) {
        case 'po_number':
            if (purchaseOrder.po_number && purchaseOrder.po_number.length > 50) {
                errors.value[errorKey] = 'PO number must be less than 50 characters'
            }
            break
        case 'supplier':
            if (!purchaseOrder.supplier) {
                errors.value[errorKey] = 'Supplier is required'
            }
            break
        case 'order_date':
            if (!purchaseOrder.order_date) {
                errors.value[errorKey] = 'Order date is required'
            }
            break
        case 'total_amount':
            if (purchaseOrder.total_amount < 0) {
                errors.value[errorKey] = 'Total amount cannot be negative'
            }
            break
        case 'tax_amount':
            if (purchaseOrder.tax_amount < 0) {
                errors.value[errorKey] = 'Tax amount cannot be negative'
            }
            break
        case 'delivery_date':
            if (purchaseOrder.delivery_date && purchaseOrder.order_date) {
                const orderDate = new Date(purchaseOrder.order_date)
                const deliveryDate = new Date(purchaseOrder.delivery_date)
                if (deliveryDate < orderDate) {
                    errors.value[errorKey] = 'Delivery date cannot be before order date'
                }
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

const deletePurchaseOrder = async (id, index) => {
    if (confirm('Are you sure you want to delete this purchase order? This action cannot be undone.')) {
        try {
            await store.removePurchaseOrder(id)
        } catch (error) {
            console.error('Error deleting purchase order:', error)
            alert('Failed to delete purchase order. Please try again.')
        }
    }
}

const getSupplierName = (supplierId) => {
    const supplier = suppliers.value.find(s => s.id === supplierId)
    return supplier ? supplier.name : ''
}

const formatDate = (dateString) => {
    if (!dateString) return '-'
    return new Date(dateString).toLocaleDateString()
}

const formatCurrency = (amount) => {
    if (!amount && amount !== 0) return '0.00'
    return parseFloat(amount).toFixed(2)
}

const formatStatus = (status) => {
    if (!status) return '-'
    return status.charAt(0).toUpperCase() + status.slice(1).replace('_', ' ')
}

const getStatusClass = (status) => {
    const statusClasses = {
        'draft': 'text-secondary',
        'sent': 'text-info',
        'partially_received': 'text-warning',
        'received': 'text-primary',
        'completed': 'text-success',
        'cancelled': 'text-danger'
    }
    return statusClasses[status] || 'text-muted'
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
    max-width: 150px;
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
    max-height: 80px;
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

    .text-truncate {
        max-width: 100px;
    }
}
</style>