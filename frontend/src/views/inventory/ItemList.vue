<!-- src/views/Inventory/ItemList.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Inventory Items</h1>
            <button @click="addNewItem" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i> Add Item
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading inventory items...</p>
        </div>

        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">Product</th>
                        <th scope="col">Current Stock</th>
                        <th scope="col">Reserved Stock</th>
                        <th scope="col">Available Stock</th>
                        <th scope="col">Reorder Level</th>
                        <th scope="col">Maximum Level</th>
                        <th scope="col">Total Cost</th>
                        <th scope="col">Average Cost</th>
                        <th scope="col">Status</th>
                        <th scope="col">Last Updated</th>
                        <th class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(item, index) in displayItems" :key="item.id || `new-${index}`" :class="{
                        'table-warning': item.isEditing || item.isNew,
                        'table-danger': item.is_below_reorder_level && !item.isEditing && !item.isNew
                    }">

                        <!-- Product Field -->
                        <td>
                            <select v-if="item.isEditing || item.isNew" v-model="item.product"
                                class="form-select form-select-sm" :class="{ 'is-invalid': errors[`${index}.product`] }"
                                @blur="validateField(index, 'product')">
                                <option value="">Select Product</option>
                                <option v-for="product in availableProducts" :key="product.id" :value="product.id">
                                    {{ product.name }} - {{ product.sku }}
                                </option>
                            </select>
                            <div v-if="errors[`${index}.product`]" class="invalid-feedback">
                                {{ errors[`${index}.product`] }}
                            </div>
                            <span v-else class="fw-semibold">
                                {{ getProductName(item.product) }}
                            </span>
                        </td>

                        <!-- Current Stock Field -->
                        <td>
                            <input v-if="item.isEditing || item.isNew" v-model="item.current_stock" type="number"
                                step="0.01" min="0" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.current_stock`] }" placeholder="0.00"
                                @blur="validateField(index, 'current_stock')" />
                            <div v-if="errors[`${index}.current_stock`]" class="invalid-feedback">
                                {{ errors[`${index}.current_stock`] }}
                            </div>
                            <span v-else>{{ formatNumber(item.current_stock) }}</span>
                        </td>

                        <!-- Reserved Stock Field -->
                        <td>
                            <input v-if="item.isEditing || item.isNew" v-model="item.reserved_stock" type="number"
                                step="0.01" min="0" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.reserved_stock`] }" placeholder="0.00"
                                @blur="validateField(index, 'reserved_stock')" />
                            <div v-if="errors[`${index}.reserved_stock`]" class="invalid-feedback">
                                {{ errors[`${index}.reserved_stock`] }}
                            </div>
                            <span v-else>{{ formatNumber(item.reserved_stock) }}</span>
                        </td>

                        <!-- Available Stock Field (Read-only) -->
                        <td>
                            <span v-if="item.isEditing || item.isNew" class="text-muted">
                                {{ formatNumber((item.current_stock || 0) - (item.reserved_stock || 0)) }}
                            </span>
                            <span v-else>{{ formatNumber(item.available_stock) }}</span>
                        </td>

                        <!-- Reorder Level Field -->
                        <td>
                            <input v-if="item.isEditing || item.isNew" v-model="item.reorder_level" type="number"
                                step="0.01" min="0" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.reorder_level`] }" placeholder="10.00"
                                @blur="validateField(index, 'reorder_level')" />
                            <div v-if="errors[`${index}.reorder_level`]" class="invalid-feedback">
                                {{ errors[`${index}.reorder_level`] }}
                            </div>
                            <span v-else>{{ formatNumber(item.reorder_level) }}</span>
                        </td>

                        <!-- Maximum Level Field -->
                        <td>
                            <input v-if="item.isEditing || item.isNew" v-model="item.maximum_level" type="number"
                                step="0.01" min="0" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.maximum_level`] }" placeholder="Optional"
                                @blur="validateField(index, 'maximum_level')" />
                            <div v-if="errors[`${index}.maximum_level`]" class="invalid-feedback">
                                {{ errors[`${index}.maximum_level`] }}
                            </div>
                            <span v-else>{{ item.maximum_level ? formatNumber(item.maximum_level) : '-' }}</span>
                        </td>

                        <!-- Total Cost Field -->
                        <td>
                            <input v-if="item.isEditing || item.isNew" v-model="item.total_cost" type="number"
                                step="0.01" min="0" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.total_cost`] }" placeholder="0.00"
                                @blur="validateField(index, 'total_cost')" />
                            <div v-if="errors[`${index}.total_cost`]" class="invalid-feedback">
                                {{ errors[`${index}.total_cost`] }}
                            </div>
                            <span v-else>${{ formatNumber(item.total_cost) }}</span>
                        </td>

                        <!-- Average Cost Field (Read-only) -->
                        <td>
                            <span v-if="item.isEditing || item.isNew" class="text-muted">
                                ${{ formatNumber(calculateAverageCost(item), 4) }}
                            </span>
                            <span v-else>${{ formatNumber(item.average_cost, 4) }}</span>
                        </td>

                        <!-- Status Field -->
                        <td>
                            <span v-if="item.is_below_reorder_level && !item.isEditing && !item.isNew"
                                class="badge bg-danger">
                                <i class="fas fa-exclamation-triangle me-1"></i>Low Stock
                            </span>
                            <span v-else class="badge bg-success">Normal</span>
                        </td>

                        <!-- Last Updated -->
                        <td>
                            <span v-if="item.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(item.last_updated) }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="item.isEditing || item.isNew" class="btn-group" role="group">
                                <button @click="handleSave(item, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Item">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editItem(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Item">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteItem(item.id, index)" class="btn btn-outline-danger btn-sm"
                                    title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.items.length === 0 && displayItems.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-boxes fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No Inventory Items found</h5>
                <p class="text-muted">Start by adding your first inventory item</p>
                <button @click="addNewItem" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Item
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useItemsStore } from '@/stores/inventory/itemsStore'

const store = useItemsStore()

const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

// Mock products data - replace with actual products store
const availableProducts = ref([
    { id: 1, name: 'Product A', sku: 'SKU001' },
    { id: 2, name: 'Product B', sku: 'SKU002' },
    // Add more products as needed
])

const displayItems = computed(() => {
    return store.items.map(item => ({
        ...item,
        isEditing: item.isEditing || false,
        isNew: item.isNew || false
    }))
})

onMounted(() => {
    store.fetchItems()
})

const addNewItem = () => {
    const newItem = {
        id: null,
        product: '',
        current_stock: 0.00,
        reserved_stock: 0.00,
        available_stock: 0.00,
        reorder_level: 10.00,
        maximum_level: null,
        total_cost: 0.00,
        average_cost: 0.0000,
        is_below_reorder_level: false,
        last_updated: null,
        isNew: true,
        isEditing: true
    }
    store.items.unshift(newItem)
}

const editItem = (index) => {
    originalData.value[index] = { ...store.items[index] }
    store.items[index].isEditing = true
}

const cancelEdit = (index) => {
    const item = store.items[index]
    if (item.isNew) {
        store.items.splice(index, 1)
    } else {
        if (originalData.value[index]) {
            Object.assign(store.items[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.items[index].isEditing = false
    }
    clearRowErrors(index)
}

const handleSave = async (item, index) => {
    try {
        isSaving.value = true
        clearRowErrors(index)

        if (!validateItem(item, index)) {
            isSaving.value = false
            return
        }

        const itemData = {
            product: item.product,
            current_stock: parseFloat(item.current_stock) || 0.00,
            reserved_stock: parseFloat(item.reserved_stock) || 0.00,
            reorder_level: parseFloat(item.reorder_level) || 10.00,
            maximum_level: item.maximum_level ? parseFloat(item.maximum_level) : null,
            total_cost: parseFloat(item.total_cost) || 0.00
        }

        if (item.isNew) {
            await store.addItem(itemData)
            store.items.splice(index, 1)
            await store.fetchItems()
        } else {
            await store.updateItem(item.id, itemData)
            store.items[index].isEditing = false
            delete originalData.value[index]
        }

        console.log(`Item ${item.isNew ? 'created' : 'updated'} successfully!`)
    } catch (error) {
        console.error('Error saving item:', error)
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            alert('Failed to save item. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateItem = (item, index) => {
    let isValid = true
    errors.value = {}

    if (!item.product) {
        errors.value[`${index}.product`] = 'Product is required'
        isValid = false
    }

    if (item.current_stock < 0) {
        errors.value[`${index}.current_stock`] = 'Current stock cannot be negative'
        isValid = false
    }

    if (item.reserved_stock < 0) {
        errors.value[`${index}.reserved_stock`] = 'Reserved stock cannot be negative'
        isValid = false
    }

    if (item.reorder_level < 0) {
        errors.value[`${index}.reorder_level`] = 'Reorder level cannot be negative'
        isValid = false
    }

    if (item.maximum_level && item.maximum_level < 0) {
        errors.value[`${index}.maximum_level`] = 'Maximum level cannot be negative'
        isValid = false
    }

    if (item.total_cost < 0) {
        errors.value[`${index}.total_cost`] = 'Total cost cannot be negative'
        isValid = false
    }

    if (parseFloat(item.reserved_stock) > parseFloat(item.current_stock)) {
        errors.value[`${index}.reserved_stock`] = 'Reserved stock cannot exceed current stock'
        isValid = false
    }

    return isValid
}

const validateField = (index, field) => {
    const item = store.items[index]
    const errorKey = `${index}.${field}`
    delete errors.value[errorKey]

    switch (field) {
        case 'product':
            if (!item.product) {
                errors.value[errorKey] = 'Product is required'
            }
            break
        case 'current_stock':
        case 'reserved_stock':
        case 'reorder_level':
        case 'total_cost':
            if (item[field] < 0) {
                errors.value[errorKey] = `${field.replace('_', ' ')} cannot be negative`
            }
            if (field === 'reserved_stock' && parseFloat(item.reserved_stock) > parseFloat(item.current_stock)) {
                errors.value[errorKey] = 'Reserved stock cannot exceed current stock'
            }
            break
        case 'maximum_level':
            if (item.maximum_level && item.maximum_level < 0) {
                errors.value[errorKey] = 'Maximum level cannot be negative'
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

const deleteItem = async (id, index) => {
    if (confirm('Are you sure you want to delete this inventory item? This action cannot be undone.')) {
        try {
            await store.removeItem(id)
        } catch (error) {
            console.error('Error deleting item:', error)
            alert('Failed to delete item. Please try again.')
        }
    }
}

const formatDate = (dateString) => {
    if (!dateString) return '-'
    return new Date(dateString).toLocaleDateString()
}

const formatNumber = (number, decimals = 2) => {
    if (number === null || number === undefined) return '0.00'
    return parseFloat(number).toFixed(decimals)
}

const calculateAverageCost = (item) => {
    const currentStock = parseFloat(item.current_stock) || 0
    const totalCost = parseFloat(item.total_cost) || 0
    return currentStock > 0 ? totalCost / currentStock : 0
}

const getProductName = (productId) => {
    const product = availableProducts.value.find(p => p.id === productId)
    return product ? `${product.name} - ${product.sku}` : 'Unknown Product'
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

.table-warning {
    background-color: #fff3cd !important;
}

.table-danger {
    background-color: #f8d7da !important;
}

.form-control-sm,
.form-select-sm {
    min-width: 100px;
}

.invalid-feedback {
    display: block;
    font-size: 0.75rem;
}

.badge {
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
        min-width: 80px;
    }
}
</style>