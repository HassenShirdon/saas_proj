<!-- src/views/Inventory/StockMovementList.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Stock Movements</h1>
            <button @click="addNewMovement" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Movement
            </button>
        </div>

        <!-- Filter Controls -->
        <div class="row mb-3">
            <div class="col-md-3">
                <select v-model="filters.movement_type" class="form-select form-select-sm">
                    <option value="">All Movement Types</option>
                    <option v-for="type in movementTypes" :value="type.value" :key="type.value">
                        {{ type.label }}
                    </option>
                </select>
            </div>
            <div class="col-md-3">
                <input v-model="filters.item_name" type="text" class="form-control form-control-sm" placeholder="Filter by item name" />
            </div>
            <div class="col-md-3">
                <input v-model="filters.date_from" type="date" class="form-control form-control-sm" placeholder="From date" />
            </div>
            <div class="col-md-3">
                <input v-model="filters.date_to" type="date" class="form-control form-control-sm" placeholder="To date" />
            </div>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading stock movements...</p>
        </div>

        <!-- Stock Movements Table -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Item</th>
                        <th scope="col">Movement Type</th>
                        <th scope="col">Quantity</th>
                        <th scope="col">Unit Cost</th>
                        <th scope="col">Total Cost</th>
                        <th scope="col">Date</th>
                        <th scope="col">Reason</th>
                        <th scope="col">Created By</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(movement, index) in filteredMovements" :key="movement.id || `new-${index}`"
                        :class="{ 'table-warning': movement.isEditing || movement.isNew }">
                        <th scope="row">{{ movement.isNew ? 'NEW' : index + 1 }}</th>

                        <!-- Item Field -->
                        <td>
                            <span class="fw-semibold">{{ movement.inventory_item?.product?.name || 'N/A' }}</span>
                        </td>

                        <!-- Movement Type Field -->
                        <td>
                            <select v-if="movement.isEditing || movement.isNew" v-model="movement.movement_type"
                                class="form-select form-select-sm" :class="{ 'is-invalid': errors[`${index}.movement_type`] }">
                                <option v-for="type in movementTypes" :value="type.value" :key="type.value">
                                    {{ type.label }}
                                </option>
                            </select>
                            <div v-if="errors[`${index}.movement_type`]" class="invalid-feedback">
                                {{ errors[`${index}.movement_type`] }}
                            </div>
                            <span v-else class="badge" :class="movementTypeClass(movement.movement_type)">
                                {{ getMovementTypeLabel(movement.movement_type) }}
                            </span>
                        </td>

                        <!-- Quantity Field -->
                        <td>
                            <input v-if="movement.isEditing || movement.isNew" v-model="movement.quantity" type="number"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.quantity`] }"
                                step="0.01" min="0.01" @blur="validateField(index, 'quantity')" />
                            <div v-if="errors[`${index}.quantity`]" class="invalid-feedback">
                                {{ errors[`${index}.quantity`] }}
                            </div>
                            <span v-else>{{ movement.quantity }}</span>
                        </td>

                        <!-- Unit Cost Field -->
                        <td>
                            <input v-if="movement.isEditing || movement.isNew" v-model="movement.unit_cost" type="number"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.unit_cost`] }"
                                step="0.0001" min="0" @blur="calculateTotalCost(index)" />
                            <div v-if="errors[`${index}.unit_cost`]" class="invalid-feedback">
                                {{ errors[`${index}.unit_cost`] }}
                            </div>
                            <span v-else>{{ formatCurrency(movement.unit_cost) }}</span>
                        </td>

                        <!-- Total Cost Field -->
                        <td>
                            <span v-if="movement.isEditing || movement.isNew">{{ formatCurrency(movement.total_cost) }}</span>
                            <span v-else>{{ formatCurrency(movement.total_cost) }}</span>
                        </td>

                        <!-- Date Field -->
                        <td>
                            <input v-if="movement.isEditing || movement.isNew" v-model="movement.recorded_at" type="datetime-local"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.recorded_at`] }" />
                            <div v-if="errors[`${index}.recorded_at`]" class="invalid-feedback">
                                {{ errors[`${index}.recorded_at`] }}
                            </div>
                            <span v-else>{{ formatDateTime(movement.recorded_at) }}</span>
                        </td>

                        <!-- Reason Field -->
                        <td>
                            <input v-if="movement.isEditing || movement.isNew" v-model="movement.reason" type="text"
                                class="form-control form-control-sm" placeholder="Reason for movement" />
                            <span v-else>{{ movement.reason || '-' }}</span>
                        </td>

                        <!-- Created By Field -->
                        <td>
                            <span>{{ movement.created_by || 'System' }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="movement.isEditing || movement.isNew" class="btn-group" role="group">
                                <button @click="handleSave(movement, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Movement">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editMovement(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Movement">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteMovement(movement.id, index)"
                                    class="btn btn-outline-danger btn-sm" title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.StockMovement.length === 0 && filteredMovements.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-boxes fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No stock movements found</h5>
                <p class="text-muted">Start by adding your first stock movement</p>
                <button @click="addNewMovement" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Movement
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useStockmovementStore } from '@/stores/inventory/stockmovementStore'

const store = useStockmovementStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

const filters = ref({
    movement_type: '',
    item_name: '',
    date_from: '',
    date_to: ''
})

const movementTypes = [
    { value: 'purchase', label: 'Purchase Receipt' },
    { value: 'sale', label: 'Sale Shipment' },
    { value: 'adjustment_in', label: 'Adjustment In' },
    { value: 'adjustment_out', label: 'Adjustment Out' },
    { value: 'transfer_in', label: 'Transfer In' },
    { value: 'transfer_out', label: 'Transfer Out' },
    { value: 'return_in', label: 'Return In' },
    { value: 'return_out', label: 'Return Out' }
]

// Create a computed property that filters movements
const filteredMovements = computed(() => {
    return store.StockMovement.filter(movement => {
        // Filter by movement type
        if (filters.value.movement_type && movement.movement_type !== filters.value.movement_type) {
            return false
        }
        
        // Filter by item name
        if (filters.value.item_name && 
            !movement.inventory_item?.product?.name?.toLowerCase().includes(filters.value.item_name.toLowerCase())) {
            return false
        }
        
        // Filter by date range
        if (filters.value.date_from || filters.value.date_to) {
            const movementDate = new Date(movement.recorded_at).setHours(0, 0, 0, 0)
            const fromDate = filters.value.date_from ? new Date(filters.value.date_from).setHours(0, 0, 0, 0) : null
            const toDate = filters.value.date_to ? new Date(filters.value.date_to).setHours(0, 0, 0, 0) : null
            
            if (fromDate && movementDate < fromDate) return false
            if (toDate && movementDate > toDate) return false
        }
        
        return true
    }).map(movement => ({
        ...movement,
        isEditing: movement.isEditing || false,
        isNew: movement.isNew || false
    }))
})

onMounted(async () => {
    await store.fetchStockMovement()
})

const addNewMovement = () => {
    const newMovement = {
        id: null,
        inventory_item: null,
        movement_type: 'purchase',
        quantity: 1,
        unit_cost: null,
        total_cost: null,
        recorded_at: new Date().toISOString().slice(0, 16),
        reason: '',
        created_by: null,
        isNew: true,
        isEditing: true
    }

    // Add to the beginning of the store's movements array
    store.StockMovement.unshift(newMovement)
}

const editMovement = (index) => {
    // Store original data for cancel functionality
    originalData.value[index] = { ...store.StockMovement[index] }

    // Set editing mode
    store.StockMovement[index].isEditing = true
}

const cancelEdit = (index) => {
    const movement = store.StockMovement[index]

    if (movement.isNew) {
        // Remove new movement
        store.StockMovement.splice(index, 1)
    } else {
        // Restore original data
        if (originalData.value[index]) {
            Object.assign(store.StockMovement[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.StockMovement[index].isEditing = false
    }

    // Clear errors for this row
    clearRowErrors(index)
}

const handleSave = async (movement, index) => {
    try {
        isSaving.value = true

        // Clear previous errors
        clearRowErrors(index)

        // Validate the movement data
        if (!validateMovement(movement, index)) {
            isSaving.value = false
            return
        }

        // Prepare movement data (exclude Vue-specific properties)
        const movementData = {
            inventory_item: movement.inventory_item?.id,
            movement_type: movement.movement_type,
            quantity: parseFloat(movement.quantity),
            unit_cost: movement.unit_cost ? parseFloat(movement.unit_cost) : null,
            total_cost: movement.total_cost ? parseFloat(movement.total_cost) : null,
            recorded_at: movement.recorded_at,
            reason: movement.reason?.trim() || '',
            created_by: movement.created_by
        }

        if (movement.isNew) {
            // Create new movement
            await store.addStockMovement(movementData)

            // Remove the temporary movement and refresh the list
            store.StockMovement.splice(index, 1)
            await store.fetchStockMovement()
        } else {
            // Update existing movement
            await store.updateStockMovement(movement.id, movementData)

            // Exit editing mode
            store.StockMovement[index].isEditing = false
            delete originalData.value[index]
        }

        // Show success message (if you have a toast/notification system)
        console.log(`Stock movement ${movement.isNew ? 'created' : 'updated'} successfully!`)

    } catch (error) {
        console.error('Error saving stock movement:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save stock movement. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const calculateTotalCost = (index) => {
    const movement = store.StockMovement[index]
    if (movement.quantity && movement.unit_cost) {
        movement.total_cost = parseFloat(movement.quantity) * parseFloat(movement.unit_cost)
    }
}

const validateMovement = (movement, index) => {
    let isValid = true

    // Required field validation
    if (!movement.movement_type) {
        errors.value[`${index}.movement_type`] = 'Movement type is required'
        isValid = false
    }

    if (!movement.quantity || parseFloat(movement.quantity) <= 0) {
        errors.value[`${index}.quantity`] = 'Quantity must be greater than 0'
        isValid = false
    }

    if (!movement.recorded_at) {
        errors.value[`${index}.recorded_at`] = 'Date is required'
        isValid = false
    }

    return isValid
}

const validateField = (index, field) => {
    const movement = store.StockMovement[index]
    const errorKey = `${index}.${field}`

    // Clear existing error
    delete errors.value[errorKey]

    // Validate specific field
    switch (field) {
        case 'movement_type':
            if (!movement.movement_type) {
                errors.value[errorKey] = 'Movement type is required'
            }
            break
        case 'quantity':
            if (!movement.quantity || parseFloat(movement.quantity) <= 0) {
                errors.value[errorKey] = 'Quantity must be greater than 0'
            }
            break
        case 'recorded_at':
            if (!movement.recorded_at) {
                errors.value[errorKey] = 'Date is required'
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

const deleteMovement = async (id, index) => {
    if (confirm('Are you sure you want to delete this stock movement? This action cannot be undone.')) {
        try {
            await store.removeStockMovement(id)
        } catch (error) {
            console.error('Error deleting stock movement:', error)
            alert('Failed to delete stock movement. Please try again.')
        }
    }
}

const formatDateTime = (dateString) => {
    if (!dateString) return '-'
    const date = new Date(dateString)
    return date.toLocaleDateString() + ' ' + date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' })
}

const formatCurrency = (value) => {
    if (value === null || value === undefined) return '-'
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(value)
}

const getMovementTypeLabel = (type) => {
    const found = movementTypes.find(t => t.value === type)
    return found ? found.label : type
}

const movementTypeClass = (type) => {
    switch (type) {
        case 'purchase':
        case 'adjustment_in':
        case 'transfer_in':
        case 'return_in':
            return 'bg-success text-white'
        case 'sale':
        case 'adjustment_out':
        case 'transfer_out':
        case 'return_out':
            return 'bg-danger text-white'
        default:
            return 'bg-secondary text-white'
    }
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

.badge {
    font-size: 0.75rem;
    padding: 0.35em 0.65em;
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