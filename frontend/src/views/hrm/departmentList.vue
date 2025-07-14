<!-- src/views/Departments/departmentList.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="container d-flex justify-content-between align-items-center p-4 mb-4 shadow-sm">
            <h1 class="h2 mb-0">Department List</h1>
            <button @click="addNewDepartment" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Department
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading departments...</p>
        </div>

        <!-- Departments Table -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Department Name</th>
                        <th scope="col">Description</th>
                        <th scope="col">Manager</th>
                        <th scope="col">Created At</th>
                        <th scope="col">Updated At</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(department, index) in displayDepartments" :key="department.id || `new-${index}`"
                        :class="{ 'table-warning': department.isEditing || department.isNew }">
                        <th scope="row">{{ department.isNew ? 'NEW' : index + 1 }}</th>

                        <!-- Department Name Field -->
                        <td>
                            <input v-if="department.isEditing || department.isNew" v-model="department.name" type="text"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.name`] }"
                                placeholder="Department name" @blur="validateField(index, 'name')" />
                            <div v-if="errors[`${index}.name`]" class="invalid-feedback">
                                {{ errors[`${index}.name`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ department.name || '-' }}</span>
                        </td>

                        <!-- Description Field -->
                        <td>
                            <textarea v-if="department.isEditing || department.isNew" v-model="department.description"
                                class="form-control form-control-sm" rows="2"
                                placeholder="Department description"></textarea>
                            <span v-else-if="department.description" class="d-inline-block text-truncate"
                                style="max-width: 200px;" :title="department.description">
                                {{ department.description }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>

                        <!-- Manager Field -->
                        <td>
                            <input v-if="department.isEditing || department.isNew" v-model="department.manager"
                                type="text" class="form-control form-control-sm" placeholder="Manager name" />
                            <span v-else>{{ department.manager || '-' }}</span>
                        </td>

                        <!-- Created At -->
                        <td>
                            <span v-if="department.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(department.created_at) }}</span>
                        </td>

                        <!-- Updated At -->
                        <td>
                            <span v-if="department.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(department.updated_at) }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="department.isEditing || department.isNew" class="btn-group" role="group">
                                <button @click="handleSave(department, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Department">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editDepartment(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Department">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteDepartment(department.id, index)"
                                    class="btn btn-outline-danger btn-sm" title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.departments.length === 0 && displayDepartments.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No departments found</h5>
                <p class="text-muted">Start by adding your first department</p>
                <button @click="addNewDepartment" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Department
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useDepartmentStore } from '@/stores/hrm/departmentStore'

const store = useDepartmentStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

// Create a computed property that combines store departments with any new/editing departments
const displayDepartments = computed(() => {
    return store.departments.map(department => ({
        ...department,
        isEditing: department.isEditing || false,
        isNew: department.isNew || false
    }))
})

onMounted(async () => {
    await store.fetchDepartments()
})

const addNewDepartment = () => {
    const newDepartment = {
        id: null,
        name: '',
        description: '',
        manager: '',
        created_at: null,
        updated_at: null,
        isNew: true,
        isEditing: true
    }

    // Add to the beginning of the store's departments array
    store.departments.unshift(newDepartment)
}

const editDepartment = (index) => {
    // Store original data for cancel functionality
    originalData.value[index] = { ...store.departments[index] }

    // Set editing mode
    store.departments[index].isEditing = true
}

const cancelEdit = (index) => {
    const department = store.departments[index]

    if (department.isNew) {
        // Remove new department
        store.departments.splice(index, 1)
    } else {
        // Restore original data
        if (originalData.value[index]) {
            Object.assign(store.departments[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.departments[index].isEditing = false
    }

    // Clear errors for this row
    clearRowErrors(index)
}

const handleSave = async (department, index) => {
    try {
        isSaving.value = true

        // Clear previous errors
        clearRowErrors(index)

        // Validate the department data
        if (!validateDepartment(department, index)) {
            isSaving.value = false
            return
        }

        // Prepare department data
        const departmentData = {
            name: department.name.trim(),
            description: department.description?.trim() || '',
            manager: department.manager?.trim() || ''
        }

        if (department.isNew) {
            // Create new department
            await store.addDepartment(departmentData)
            // Remove the temporary department and refresh the list
            store.departments.splice(index, 1)
            await store.fetchDepartments()
        } else {
            // Update existing department
            await store.updateDepartment(department.id, departmentData)
            // Exit editing mode
            store.departments[index].isEditing = false
            delete originalData.value[index]
        }

        // Show success message
        console.log(`Department ${department.isNew ? 'created' : 'updated'} successfully!`)

    } catch (error) {
        console.error('Error saving department:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save department. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateDepartment = (department, index) => {
    let isValid = true

    // Required field validation
    if (!department.name?.trim()) {
        errors.value[`${index}.name`] = 'Department name is required'
        isValid = false
    }

    return isValid
}

const validateField = (index, field) => {
    const department = store.departments[index]
    const errorKey = `${index}.${field}`

    // Clear existing error
    delete errors.value[errorKey]

    // Validate specific field
    if (field === 'name' && !department.name?.trim()) {
        errors.value[errorKey] = 'Department name is required'
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

const deleteDepartment = async (id, index) => {
    if (confirm('Are you sure you want to delete this department? This action cannot be undone.')) {
        try {
            await store.deleteDepartment(id)
        } catch (error) {
            console.error('Error deleting department:', error)
            alert('Failed to delete department. Please try again.')
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