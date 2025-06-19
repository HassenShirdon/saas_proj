<!-- src/views/Customers/CustomerList.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Customers List</h1>
            <button @click="addNewCustomer" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Customer
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading customers...</p>
        </div>

        <!-- Customers Table -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Name</th>
                        <th scope="col">Contact Person</th>
                        <th scope="col">Email</th>
                        <th scope="col">Phone</th>
                        <th scope="col">Address</th>
                        <th scope="col">Status</th>
                        <th scope="col">Created At</th>
                        <th scope="col">Updated At</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(customer, index) in displayCustomers" :key="customer.id || `new-${index}`"
                        :class="{ 'table-warning': customer.isEditing || customer.isNew }">
                        <th scope="row">{{ customer.isNew ? 'NEW' : index + 1 }}</th>

                        <!-- Name Field -->
                        <td>
                            <input v-if="customer.isEditing || customer.isNew" v-model="customer.name" type="text"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.name`] }"
                                placeholder="Customer name" @blur="validateField(index, 'name')" />
                            <div v-if="errors[`${index}.name`]" class="invalid-feedback">
                                {{ errors[`${index}.name`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ customer.name }}</span>
                        </td>

                        <!-- Contact Person Field -->
                        <td>
                            <input v-if="customer.isEditing || customer.isNew" v-model="customer.contact_person"
                                type="text" class="form-control form-control-sm" placeholder="Contact person" />
                            <span v-else>{{ customer.contact_person || '-' }}</span>
                        </td>

                        <!-- Email Field -->
                        <td>
                            <input v-if="customer.isEditing || customer.isNew" v-model="customer.email" type="email"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.email`] }"
                                placeholder="email@example.com" @blur="validateField(index, 'email')" />
                            <div v-if="errors[`${index}.email`]" class="invalid-feedback">
                                {{ errors[`${index}.email`] }}
                            </div>
                            <a v-else-if="customer.email" :href="`mailto:${customer.email}`"
                                class="text-decoration-none">
                                {{ customer.email }}
                            </a>
                            <span v-else class="text-muted">-</span>
                        </td>

                        <!-- Phone Field -->
                        <td>
                            <input v-if="customer.isEditing || customer.isNew" v-model="customer.phone_number"
                                type="tel" class="form-control form-control-sm" placeholder="Phone number" />
                            <a v-else-if="customer.phone_number" :href="`tel:${customer.phone_number}`"
                                class="text-decoration-none">
                                {{ customer.phone_number }}
                            </a>
                            <span v-else class="text-muted">-</span>
                        </td>

                        <!-- Address Field -->
                        <td>
                            <textarea v-if="customer.isEditing || customer.isNew" v-model="customer.address"
                                class="form-control form-control-sm" rows="2" placeholder="Customer address"></textarea>
                            <span v-else-if="customer.address" class="d-inline-block text-truncate"
                                style="max-width: 200px;" :title="customer.address">
                                {{ customer.address }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>

                        <!-- Status Field -->
                        <td>
                            <select v-if="customer.isEditing || customer.isNew" v-model="customer.is_active"
                                class="form-select form-select-sm">
                                <option :value="true">Active</option>
                                <option :value="false">Inactive</option>
                            </select>
                            <span v-else :class="customer.is_active ? 'text-success' : 'text-danger'">
                                {{ customer.is_active ? 'Active' : 'Inactive' }}
                            </span>
                        </td>

                        <!-- Created At -->
                        <td>
                            <span v-if="customer.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(customer.created_at) }}</span>
                        </td>

                        <!-- Updated At -->
                        <td>
                            <span v-if="customer.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(customer.updated_at) }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="customer.isEditing || customer.isNew" class="btn-group" role="group">
                                <button @click="handleSave(customer, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Customer">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editCustomer(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Customer">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteCustomer(customer.id, index)"
                                    class="btn btn-outline-danger btn-sm" title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.customers.length === 0 && displayCustomers.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No customers found</h5>
                <p class="text-muted">Start by adding your first customer</p>
                <button @click="addNewCustomer" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Customer
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useCustomerStore } from '@/stores/inventory/customerStore'

const store = useCustomerStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

// Create a computed property that combines store customers with any new/editing customers
const displayCustomers = computed(() => {
    return store.customers.map(customer => ({
        ...customer,
        isEditing: customer.isEditing || false,
        isNew: customer.isNew || false
    }))
})

onMounted(async () => {
    await store.fetchCustomers()
})

const addNewCustomer = () => {
    const newCustomer = {
        id: null,
        name: '',
        contact_person: '',
        email: '',
        phone_number: '',
        address: '',
        is_active: true,
        created_at: null,
        updated_at: null,
        isNew: true,
        isEditing: true
    }

    // Add to the beginning of the store's customers array
    store.customers.unshift(newCustomer)
}

const editCustomer = (index) => {
    // Store original data for cancel functionality
    originalData.value[index] = { ...store.customers[index] }

    // Set editing mode
    store.customers[index].isEditing = true
}

const cancelEdit = (index) => {
    const customer = store.customers[index]

    if (customer.isNew) {
        // Remove new customer
        store.customers.splice(index, 1)
    } else {
        // Restore original data
        if (originalData.value[index]) {
            Object.assign(store.customers[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.customers[index].isEditing = false
    }

    // Clear errors for this row
    clearRowErrors(index)
}

// Modified handleSave function for inline editing
const handleSave = async (customer, index) => {
    try {
        isSaving.value = true

        // Clear previous errors
        clearRowErrors(index)

        // Validate the customer data
        if (!validateCustomer(customer, index)) {
            isSaving.value = false
            return
        }

        // Prepare customer data (exclude Vue-specific properties)
        const customerData = {
            name: customer.name.trim(),
            contact_person: customer.contact_person?.trim() || '',
            email: customer.email?.trim() || '',
            phone_number: customer.phone_number?.trim() || '',
            address: customer.address?.trim() || '',
            is_active: customer.is_active
        }

        if (customer.isNew) {
            // Create new customer using your existing store method
            await store.addCustomer(customerData)

            // Remove the temporary customer and refresh the list
            store.customers.splice(index, 1)
            await store.fetchCustomers()
        } else {
            // Update existing customer using your existing store method
            await store.updateCustomer(customer.id, customerData)

            // Exit editing mode
            store.customers[index].isEditing = false
            delete originalData.value[index]
        }

        // Show success message (if you have a toast/notification system)
        console.log(`Customer ${customer.isNew ? 'created' : 'updated'} successfully!`)

    } catch (error) {
        console.error('Error saving customer:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save customer. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateCustomer = (customer, index) => {
    let isValid = true

    // Required field validation
    if (!customer.name?.trim()) {
        errors.value[`${index}.name`] = 'Customer name is required'
        isValid = false
    }

    // Email validation
    if (customer.email && !isValidEmail(customer.email)) {
        errors.value[`${index}.email`] = 'Please enter a valid email address'
        isValid = false
    }

    return isValid
}

const validateField = (index, field) => {
    const customer = store.customers[index]
    const errorKey = `${index}.${field}`

    // Clear existing error
    delete errors.value[errorKey]

    // Validate specific field
    switch (field) {
        case 'name':
            if (!customer.name?.trim()) {
                errors.value[errorKey] = 'Customer name is required'
            }
            break
        case 'email':
            if (customer.email && !isValidEmail(customer.email)) {
                errors.value[errorKey] = 'Please enter a valid email address'
            }
            break
    }
}

const isValidEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return emailRegex.test(email)
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

const deleteCustomer = async (id, index) => {
    if (confirm('Are you sure you want to delete this customer? This action cannot be undone.')) {
        try {
            await store.removeCustomer(id)
        } catch (error) {
            console.error('Error deleting customer:', error)
            alert('Failed to delete customer. Please try again.')
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