<!-- src/views/Suppliers/SupplierList.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Supplier List</h1>
            <button @click="addNewSupplier" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Supplier
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading suppliers...</p>
        </div>

        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Contact Person</th>
                        <th scope="col">Email</th>
                        <th scope="col">Phone Number</th>
                        <th scope="col">Address</th>
                        <th scope="col">Status</th>
                        <th scope="col">Created At</th>
                        <th scope="col">Updated At</th>
                        <th class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(supplier, index) in displaySuppliers" :key="supplier.id || `new-${index}`"
                        :class="{ 'table-warning': supplier.isEditing || supplier.isNew }">

                        <!-- Name Field -->
                        <td>
                            <input v-if="supplier.isEditing || supplier.isNew" v-model="supplier.name" type="text"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.name`] }"
                                placeholder="Supplier name" @blur="validateField(index, 'name')" />
                            <div v-if="errors[`${index}.name`]" class="invalid-feedback">
                                {{ errors[`${index}.name`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ supplier.name }}</span>
                        </td>

                        <!-- Contact Person Field -->
                        <td>
                            <input v-if="supplier.isEditing || supplier.isNew" v-model="supplier.contact_person"
                                type="text" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.contact_person`] }"
                                placeholder="Contact person" @blur="validateField(index, 'contact_person')" />
                            <div v-if="errors[`${index}.contact_person`]" class="invalid-feedback">
                                {{ errors[`${index}.contact_person`] }}
                            </div>
                            <span v-else>{{ supplier.contact_person || '-' }}</span>
                        </td>

                        <!-- Email Field -->
                        <td>
                            <input v-if="supplier.isEditing || supplier.isNew" v-model="supplier.email" type="email"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.email`] }"
                                placeholder="email@example.com" @blur="validateField(index, 'email')" />
                            <div v-if="errors[`${index}.email`]" class="invalid-feedback">
                                {{ errors[`${index}.email`] }}
                            </div>
                            <span v-else>{{ supplier.email || '-' }}</span>
                        </td>

                        <!-- Phone Number Field -->
                        <td>
                            <input v-if="supplier.isEditing || supplier.isNew" v-model="supplier.phone_number"
                                type="tel" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.phone_number`] }" placeholder="Phone number"
                                @blur="validateField(index, 'phone_number')" />
                            <div v-if="errors[`${index}.phone_number`]" class="invalid-feedback">
                                {{ errors[`${index}.phone_number`] }}
                            </div>
                            <span v-else>{{ supplier.phone_number || '-' }}</span>
                        </td>

                        <!-- Address Field -->
                        <td>
                            <textarea v-if="supplier.isEditing || supplier.isNew" v-model="supplier.address"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.address`] }" placeholder="Address"
                                @blur="validateField(index, 'address')"></textarea>
                            <div v-if="errors[`${index}.address`]" class="invalid-feedback">
                                {{ errors[`${index}.address`] }}
                            </div>
                            <span v-else>{{ supplier.address || '-' }}</span>
                        </td>

                        <!-- Status Field -->
                        <td>
                            <select v-if="supplier.isEditing || supplier.isNew" v-model="supplier.is_active"
                                class="form-select form-select-sm">
                                <option :value="true">Active</option>
                                <option :value="false">Inactive</option>
                            </select>
                            <span v-else :class="supplier.is_active ? 'text-success' : 'text-danger'">
                                {{ supplier.is_active ? 'Active' : 'Inactive' }}
                            </span>
                        </td>

                        <!-- Created At -->
                        <td>
                            <span v-if="supplier.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(supplier.created_at) }}</span>
                        </td>

                        <!-- Updated At -->
                        <td>
                            <span v-if="supplier.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(supplier.updated_at) }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="supplier.isEditing || supplier.isNew" class="btn-group" role="group">
                                <button @click="handleSave(supplier, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Supplier">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editSupplier(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Supplier">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteSupplier(supplier.id, index)"
                                    class="btn btn-outline-danger btn-sm" title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.suppliers.length === 0 && displaySuppliers.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-truck fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No Suppliers found</h5>
                <p class="text-muted">Start by adding your first Supplier</p>
                <button @click="addNewSupplier" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Supplier
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useSupplierStore } from '@/stores/inventory/supplierStore'

const store = useSupplierStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

const displaySuppliers = computed(() => {
    return store.suppliers.map(supplier => ({
        ...supplier,
        isEditing: supplier.isEditing || false,
        isNew: supplier.isNew || false
    }))
})

onMounted(() => {
    store.fetchSuppliers()
})

const addNewSupplier = () => {
    const newSupplier = {
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
    store.suppliers.unshift(newSupplier)
}

const editSupplier = (index) => {
    originalData.value[index] = { ...store.suppliers[index] }
    store.suppliers[index].isEditing = true
}

const cancelEdit = (index) => {
    const supplier = store.suppliers[index]
    if (supplier.isNew) {
        store.suppliers.splice(index, 1)
    } else {
        if (originalData.value[index]) {
            Object.assign(store.suppliers[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.suppliers[index].isEditing = false
    }
    clearRowErrors(index)
}

const handleSave = async (supplier, index) => {
    try {
        isSaving.value = true
        clearRowErrors(index)

        if (!validateSupplier(supplier, index)) {
            isSaving.value = false
            return
        }

        const supplierData = {
            name: supplier.name.trim(),
            contact_person: supplier.contact_person?.trim() || '',
            email: supplier.email?.trim() || '',
            phone_number: supplier.phone_number?.trim() || '',
            address: supplier.address?.trim() || '',
            is_active: supplier.is_active
        }

        if (supplier.isNew) {
            await store.addSupplier(supplierData)
            store.suppliers.splice(index, 1)
            await store.fetchSuppliers()
        } else {
            await store.updateSupplier(supplier.id, supplierData)
            store.suppliers[index].isEditing = false
            delete originalData.value[index]
        }

        console.log(`Supplier ${supplier.isNew ? 'created' : 'updated'} successfully!`)
    } catch (error) {
        console.error('Error saving supplier:', error)
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            alert('Failed to save supplier. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateSupplier = (supplier, index) => {
    let isValid = true
    errors.value = {}

    if (!supplier.name?.trim()) {
        errors.value[`${index}.name`] = 'Supplier name is required'
        isValid = false
    } else if (supplier.name.length > 255) {
        errors.value[`${index}.name`] = 'Name must be less than 255 characters'
        isValid = false
    }

    if (supplier.contact_person && supplier.contact_person.length > 255) {
        errors.value[`${index}.contact_person`] = 'Contact person must be less than 255 characters'
        isValid = false
    }

    if (supplier.email && supplier.email.trim()) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
        if (!emailRegex.test(supplier.email)) {
            errors.value[`${index}.email`] = 'Please enter a valid email address'
            isValid = false
        }
    }

    if (supplier.phone_number && supplier.phone_number.length > 20) {
        errors.value[`${index}.phone_number`] = 'Phone number must be less than 20 characters'
        isValid = false
    }

    return isValid
}

const validateField = (index, field) => {
    const supplier = store.suppliers[index]
    const errorKey = `${index}.${field}`
    delete errors.value[errorKey]

    switch (field) {
        case 'name':
            if (!supplier.name?.trim()) {
                errors.value[errorKey] = 'Supplier name is required'
            } else if (supplier.name.length > 255) {
                errors.value[errorKey] = 'Name must be less than 255 characters'
            }
            break
        case 'contact_person':
            if (supplier.contact_person && supplier.contact_person.length > 255) {
                errors.value[errorKey] = 'Contact person must be less than 255 characters'
            }
            break
        case 'email':
            if (supplier.email && supplier.email.trim()) {
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
                if (!emailRegex.test(supplier.email)) {
                    errors.value[errorKey] = 'Please enter a valid email address'
                }
            }
            break
        case 'phone_number':
            if (supplier.phone_number && supplier.phone_number.length > 20) {
                errors.value[errorKey] = 'Phone number must be less than 20 characters'
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

const deleteSupplier = async (id, index) => {
    if (confirm('Are you sure you want to delete this supplier? This action cannot be undone.')) {
        try {
            await store.removeSupplier(id)
        } catch (error) {
            console.error('Error deleting supplier:', error)
            alert('Failed to delete supplier. Please try again.')
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