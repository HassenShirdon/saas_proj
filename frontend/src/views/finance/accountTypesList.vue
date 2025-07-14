<!-- src/views/Finance/AccountTypes.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="container d-flex justify-content-between align-items-center p-4 mb-4 shadow-sm">
            <h1 class="h2 mb-0">Account Types</h1>
            <button @click="addNewAccountType" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Account Type
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading account types...</p>
        </div>

        <!-- Account Types Table -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Account Name</th>
                        <th scope="col">Normal Balance</th>
                        <th scope="col">Category</th>
                        <th scope="col">Description</th>
                        <th scope="col">Created At</th>
                        <th scope="col">Updated At</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(accountType, index) in displayAccountTypes" :key="accountType.id || `new-${index}`"
                        :class="{ 'table-warning': accountType.isEditing || accountType.isNew }">
                        <th scope="row">{{ accountType.isNew ? 'NEW' : index + 1 }}</th>

                        <!-- Account Name Field -->
                        <td>
                            <input v-if="accountType.isEditing || accountType.isNew" v-model="accountType.name"
                                type="text" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.name`] }" placeholder="Account name"
                                @blur="validateField(index, 'name')" />
                            <div v-if="errors[`${index}.name`]" class="invalid-feedback">
                                {{ errors[`${index}.name`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ accountType.name || '-' }}</span>
                        </td>

                        <!-- Normal Balance Field -->
                        <td>
                            <select v-if="accountType.isEditing || accountType.isNew"
                                v-model="accountType.normal_balance" class="form-select form-select-sm"
                                :class="{ 'is-invalid': errors[`${index}.normal_balance`] }"
                                @blur="validateField(index, 'normal_balance')">
                                <option value="" disabled>Select balance</option>
                                <option value="Debit">Debit</option>
                                <option value="Credit">Credit</option>
                            </select>
                            <div v-if="errors[`${index}.normal_balance`]" class="invalid-feedback">
                                {{ errors[`${index}.normal_balance`] }}
                            </div>
                            <span v-else>{{ accountType.normal_balance || '-' }}</span>
                        </td>

                        <!-- Category Field -->
                        <td>
                            <input v-if="accountType.isEditing || accountType.isNew" v-model="accountType.category"
                                type="text" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.category`] }" placeholder="Category"
                                @blur="validateField(index, 'category')" />
                            <div v-if="errors[`${index}.category`]" class="invalid-feedback">
                                {{ errors[`${index}.category`] }}
                            </div>
                            <span v-else>{{ accountType.category || '-' }}</span>
                        </td>

                        <!-- Description Field -->
                        <td>
                            <textarea v-if="accountType.isEditing || accountType.isNew"
                                v-model="accountType.description" class="form-control form-control-sm" rows="2"
                                placeholder="Description"></textarea>
                            <span v-else-if="accountType.description" class="d-inline-block text-truncate"
                                style="max-width: 200px;" :title="accountType.description">
                                {{ accountType.description }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>

                        <!-- Created At -->
                        <td>
                            <span v-if="accountType.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(accountType.created_at) }}</span>
                        </td>

                        <!-- Updated At -->
                        <td>
                            <span v-if="accountType.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(accountType.updated_at) }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="accountType.isEditing || accountType.isNew" class="btn-group" role="group">
                                <button @click="handleSave(accountType, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Account Type">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editAccountType(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Account Type">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteAccountType(accountType.id, index)"
                                    class="btn btn-outline-danger btn-sm" title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.accounts.length === 0 && displayAccountTypes.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No account types found</h5>
                <p class="text-muted">Start by adding your first account type</p>
                <button @click="addNewAccountType" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Account Type
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useAccountTypeStore } from '@/stores/finance/accountTypeStore'

const store = useAccountTypeStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

// Create a computed property that combines store account types with any new/editing account types
const displayAccountTypes = computed(() => {
    return store.accounts.map(accountType => ({
        ...accountType,
        isEditing: accountType.isEditing || false,
        isNew: accountType.isNew || false
    }))
})

onMounted(async () => {
    await store.fetchAccountTypes()
})

const addNewAccountType = () => {
    const newAccountType = {
        id: null,
        name: '',
        normal_balance: '',
        category: '',
        description: '',
        created_at: null,
        updated_at: null,
        isNew: true,
        isEditing: true
    }

    // Add to the beginning of the store's accountTypes array
    store.accountTypes.unshift(newAccountType)
}

const editAccountType = (index) => {
    // Store original data for cancel functionality
    originalData.value[index] = { ...store.accountTypes[index] }

    // Set editing mode
    store.accountTypes[index].isEditing = true
}

const cancelEdit = (index) => {
    const accountType = store.accountTypes[index]

    if (accountType.isNew) {
        // Remove new account type
        store.accountTypes.splice(index, 1)
    } else {
        // Restore original data
        if (originalData.value[index]) {
            Object.assign(store.accountTypes[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.accountTypes[index].isEditing = false
    }

    // Clear errors for this row
    clearRowErrors(index)
}

const handleSave = async (accountType, index) => {
    try {
        isSaving.value = true

        // Clear previous errors
        clearRowErrors(index)

        // Validate the account type data
        if (!validateAccountType(accountType, index)) {
            isSaving.value = false
            return
        }

        // Prepare account type data
        const accountTypeData = {
            name: accountType.name.trim(),
            normal_balance: accountType.normal_balance,
            category: accountType.category.trim(),
            description: accountType.description?.trim() || ''
        }

        if (accountType.isNew) {
            // Create new account type
            await store.addAccountType(accountTypeData)
            // Remove the temporary account type and refresh the list
            store.accountTypes.splice(index, 1)
            await store.fetchAccountTypes()
        } else {
            // Update existing account type
            await store.updateAccountType(accountType.id, accountTypeData)
            // Exit editing mode
            store.accountTypes[index].isEditing = false
            delete originalData.value[index]
        }

        // Show success message
        console.log(`Account Type ${accountType.isNew ? 'created' : 'updated'} successfully!`)

    } catch (error) {
        console.error('Error saving account type:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save account type. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateAccountType = (accountType, index) => {
    let isValid = true

    // Required field validation
    if (!accountType.name?.trim()) {
        errors.value[`${index}.name`] = 'Account name is required'
        isValid = false
    }

    if (!accountType.normal_balance) {
        errors.value[`${index}.normal_balance`] = 'Normal balance is required'
        isValid = false
    }

    if (!accountType.category?.trim()) {
        errors.value[`${index}.category`] = 'Category is required'
        isValid = false
    }

    return isValid
}

const validateField = (index, field) => {
    const accountType = store.accountTypes[index]
    const errorKey = `${index}.${field}`

    // Clear existing error
    delete errors.value[errorKey]

    // Validate specific field
    switch (field) {
        case 'name':
            if (!accountType.name?.trim()) {
                errors.value[errorKey] = 'Account name is required'
            }
            break
        case 'normal_balance':
            if (!accountType.normal_balance) {
                errors.value[errorKey] = 'Normal balance is required'
            }
            break
        case 'category':
            if (!accountType.category?.trim()) {
                errors.value[errorKey] = 'Category is required'
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

const deleteAccountType = async (id, index) => {
    if (confirm('Are you sure you want to delete this account type? This action cannot be undone.')) {
        try {
            await store.removeAccountType(id)
        } catch (error) {
            console.error('Error deleting account type:', error)
            alert('Failed to delete account type. Please try again.')
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