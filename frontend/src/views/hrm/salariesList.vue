<!-- src/views/Salaries/salariesList.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="container d-flex justify-content-between align-items-center p-4 mb-4 shadow-sm">
            <h1 class="h2 mb-0">Salary List</h1>
            <button @click="addNewSalary" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Salary
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading salaries...</p>
        </div>

        <!-- Salaries Table -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Employee Name</th>
                        <th scope="col">Amount</th>
                        <th scope="col">Effective Date</th>
                        <th scope="col">End Date</th>
                        <th scope="col">Reason</th>
                        <th scope="col">Created At</th>
                        <th scope="col">Updated At</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(salary, index) in displaySalaries" :key="salary.id || `new-${index}`"
                        :class="{ 'table-warning': salary.isEditing || salary.isNew }">
                        <th scope="row">{{ salary.isNew ? 'NEW' : index + 1 }}</th>

                        <!-- Employee Name Field -->
                        <td>
                            <input v-if="salary.isEditing || salary.isNew" v-model="salary.employee" type="text"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.employee`] }" placeholder="Employee name"
                                @blur="validateField(index, 'employee')" />
                            <div v-if="errors[`${index}.employee`]" class="invalid-feedback">
                                {{ errors[`${index}.employee`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ salary.employee || '-' }}</span>
                        </td>

                        <!-- Amount Field -->
                        <td>
                            <input v-if="salary.isEditing || salary.isNew" v-model="salary.amount" type="number"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.amount`] }" placeholder="Amount"
                                @blur="validateField(index, 'amount')" />
                            <div v-if="errors[`${index}.amount`]" class="invalid-feedback">
                                {{ errors[`${index}.amount`] }}
                            </div>
                            <span v-else>€ {{ salary.amount || '-' }}</span>
                        </td>

                        <!-- Effective Date Field -->
                        <td>
                            <input v-if="salary.isEditing || salary.isNew" v-model="salary.effective_date" type="date"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.effective_date`] }"
                                @blur="validateField(index, 'effective_date')" />
                            <div v-if="errors[`${index}.effective_date`]" class="invalid-feedback">
                                {{ errors[`${index}.effective_date`] }}
                            </div>
                            <span v-else>{{ salary.effective_date || '-' }}</span>
                        </td>

                        <!-- End Date Field -->
                        <td>
                            <input v-if="salary.isEditing || salary.isNew" v-model="salary.end_date" type="date"
                                class="form-control form-control-sm" />
                            <span v-else>{{ salary.end_date || '-' }}</span>
                        </td>

                        <!-- Reason Field -->
                        <td>
                            <textarea v-if="salary.isEditing || salary.isNew" v-model="salary.reason"
                                class="form-control form-control-sm" rows="2" placeholder="Reason"></textarea>
                            <span v-else-if="salary.reason" class="d-inline-block text-truncate"
                                style="max-width: 200px;" :title="salary.reason">
                                {{ salary.reason }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>

                        <!-- Created At -->
                        <td>
                            <span v-if="salary.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(salary.created_at) }}</span>
                        </td>

                        <!-- Updated At -->
                        <td>
                            <span v-if="salary.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(salary.updated_at) }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="salary.isEditing || salary.isNew" class="btn-group" role="group">
                                <button @click="handleSave(salary, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Salary">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editSalary(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Salary">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteSalary(salary.id, index)" class="btn btn-outline-danger btn-sm"
                                    title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.salaries.length === 0 && displaySalaries.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No salaries found</h5>
                <p class="text-muted">Start by adding your first salary</p>
                <button @click="addNewSalary" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Salary
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useSalaryStore } from '@/stores/hrm/salaryStore'

const store = useSalaryStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

// Create a computed property that combines store salaries with any new/editing salaries
const displaySalaries = computed(() => {
    return store.salaries.map(salary => ({
        ...salary,
        isEditing: salary.isEditing || false,
        isNew: salary.isNew || false
    }))
})

onMounted(async () => {
    await store.fetchSalaries()
})

const addNewSalary = () => {
    const newSalary = {
        id: null,
        employee: '',
        amount: '',
        effective_date: '',
        end_date: '',
        reason: '',
        created_at: null,
        updated_at: null,
        isNew: true,
        isEditing: true
    }

    // Add to the beginning of the store's salaries array
    store.salaries.unshift(newSalary)
}

const editSalary = (index) => {
    // Store original data for cancel functionality
    originalData.value[index] = { ...store.salaries[index] }

    // Set editing mode
    store.salaries[index].isEditing = true
}

const cancelEdit = (index) => {
    const salary = store.salaries[index]

    if (salary.isNew) {
        // Remove new salary
        store.salaries.splice(index, 1)
    } else {
        // Restore original data
        if (originalData.value[index]) {
            Object.assign(store.salaries[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.salaries[index].isEditing = false
    }

    // Clear errors for this row
    clearRowErrors(index)
}

const handleSave = async (salary, index) => {
    try {
        isSaving.value = true

        // Clear previous errors
        clearRowErrors(index)

        // Validate the salary data
        if (!validateSalary(salary, index)) {
            isSaving.value = false
            return
        }

        // Prepare salary data
        const salaryData = {
            employee: salary.employee.trim(),
            amount: salary.amount,
            effective_date: salary.effective_date,
            end_date: salary.end_date || '',
            reason: salary.reason?.trim() || ''
        }

        if (salary.isNew) {
            // Create new salary
            await store.addSalary(salaryData)
            // Remove the temporary salary and refresh the list
            store.salaries.splice(index, 1)
            await store.fetchSalaries()
        } else {
            // Update existing salary
            await store.updateSalary(salary.id, salaryData)
            // Exit editing mode
            store.salaries[index].isEditing = false
            delete originalData.value[index]
        }

        // Show success message
        console.log(`Salary ${salary.isNew ? 'created' : 'updated'} successfully!`)

    } catch (error) {
        console.error('Error saving salary:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save salary. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateSalary = (salary, index) => {
    let isValid = true

    // Required field validation
    if (!salary.employee?.trim()) {
        errors.value[`${index}.employee`] = 'Employee name is required'
        isValid = false
    }

    if (!salary.amount) {
        errors.value[`${index}.amount`] = 'Amount is required'
        isValid = false
    }

    if (!salary.effective_date) {
        errors.value[`${index}.effective_date`] = 'Effective date is required'
        isValid = false
    }

    return isValid
}

const validateField = (index, field) => {
    const salary = store.salaries[index]
    const errorKey = `${index}.${field}`

    // Clear existing error
    delete errors.value[errorKey]

    // Validate specific field
    switch (field) {
        case 'employee':
            if (!salary.employee?.trim()) {
                errors.value[errorKey] = 'Employee name is required'
            }
            break
        case 'amount':
            if (!salary.amount) {
                errors.value[errorKey] = 'Amount is required'
            }
            break
        case 'effective_date':
            if (!salary.effective_date) {
                errors.value[errorKey] = 'Effective date is required'
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

const deleteSalary = async (id, index) => {
    if (confirm('Are you sure you want to delete this salary record? This action cannot be undone.')) {
        try {
            await store.deleteSalary(id)
        } catch (error) {
            console.error('Error deleting salary:', error)
            alert('Failed to delete salary. Please try again.')
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