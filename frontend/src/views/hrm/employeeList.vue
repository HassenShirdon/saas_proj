<!-- src/views/Employees/employeeList.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="container d-flex justify-content-between align-items-center p-4 mb-4 shadow-sm">
            <h1 class="h2 mb-0">Employee List</h1>
            <button @click="addNewEmployee" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Employee
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading employees...</p>
        </div>

        <!-- Employees Table -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">First Name</th>
                        <th scope="col">Last Name</th>
                        <th scope="col">Email</th>
                        <th scope="col">Phone Number</th>
                        <th scope="col">Date of Birth</th>
                        <th scope="col">Hired Date</th>
                        <th scope="col">Position</th>
                        <th scope="col">Department</th>
                        <th scope="col">Manager</th>
                        <th scope="col">Current Salary</th>
                        <th scope="col">Status</th>
                        <th scope="col">Created At</th>
                        <th scope="col">Updated At</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(employee, index) in displayEmployees" :key="employee.id || `new-${index}`"
                        :class="{ 'table-warning': employee.isEditing || employee.isNew }">
                        <th scope="row">{{ employee.isNew ? 'NEW' : index + 1 }}</th>

                        <!-- First Name Field -->
                        <td>
                            <input v-if="employee.isEditing || employee.isNew" v-model="employee.first_name" type="text"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.first_name`] }" placeholder="First name"
                                @blur="validateField(index, 'first_name')" />
                            <div v-if="errors[`${index}.first_name`]" class="invalid-feedback">
                                {{ errors[`${index}.first_name`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ employee.first_name || '-' }}</span>
                        </td>

                        <!-- Last Name Field -->
                        <td>
                            <input v-if="employee.isEditing || employee.isNew" v-model="employee.last_name" type="text"
                                class="form-control form-control-sm" placeholder="Last name" />
                            <span v-else>{{ employee.last_name || '-' }}</span>
                        </td>

                        <!-- Email Field -->
                        <td>
                            <input v-if="employee.isEditing || employee.isNew" v-model="employee.email" type="email"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.email`] }"
                                placeholder="email@example.com" @blur="validateField(index, 'email')" />
                            <div v-if="errors[`${index}.email`]" class="invalid-feedback">
                                {{ errors[`${index}.email`] }}
                            </div>
                            <a v-else-if="employee.email" :href="`mailto:${employee.email}`"
                                class="text-decoration-none">
                                {{ employee.email }}
                            </a>
                            <span v-else class="text-muted">-</span>
                        </td>

                        <!-- Phone Number Field -->
                        <td>
                            <input v-if="employee.isEditing || employee.isNew" v-model="employee.phone_number"
                                type="tel" class="form-control form-control-sm" placeholder="Phone number" />
                            <a v-else-if="employee.phone_number" :href="`tel:${employee.phone_number}`"
                                class="text-decoration-none">
                                {{ employee.phone_number }}
                            </a>
                            <span v-else class="text-muted">-</span>
                        </td>

                        <!-- Date of Birth Field -->
                        <td>
                            <input v-if="employee.isEditing || employee.isNew" v-model="employee.date_of_birth"
                                type="date" class="form-control form-control-sm" />
                            <span v-else-if="employee.date_of_birth" class="d-inline-block text-truncate"
                                style="max-width: 200px;" :title="employee.date_of_birth">
                                {{ employee.date_of_birth }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>

                        <!-- Hired Date Field -->
                        <td>
                            <input v-if="employee.isEditing || employee.isNew" v-model="employee.date_hired" type="date"
                                class="form-control form-control-sm" />
                            <span v-else>{{ employee.date_hired || '-' }}</span>
                        </td>

                        <!-- Position Field -->
                        <td>
                            <input v-if="employee.isEditing || employee.isNew" v-model="employee.position" type="text"
                                class="form-control form-control-sm" placeholder="Position" />
                            <span v-else>{{ employee.position || '-' }}</span>
                        </td>

                        <!-- Department Field -->
                        <td>
                            <input v-if="employee.isEditing || employee.isNew" v-model="employee.department" type="text"
                                class="form-control form-control-sm" placeholder="Department" />
                            <span v-else>{{ employee.department || '-' }}</span>
                        </td>

                        <!-- Manager Field -->
                        <td>
                            <input v-if="employee.isEditing || employee.isNew" v-model="employee.manager" type="text"
                                class="form-control form-control-sm" placeholder="Manager" />
                            <span v-else>{{ employee.manager || '-' }}</span>
                        </td>

                        <!-- Current Salary Field -->
                        <td>
                            <input v-if="employee.isEditing || employee.isNew" v-model="employee.current_salary"
                                type="number" class="form-control form-control-sm" placeholder="Salary" />
                            <span v-else>€ {{ employee.current_salary || '-' }}</span>
                        </td>

                        <!-- Status Field -->
                        <td>
                            <select v-if="employee.isEditing || employee.isNew" v-model="employee.status"
                                class="form-select form-select-sm">
                                <option value="Active">Active</option>
                                <option value="Inactive">Inactive</option>
                            </select>
                            <span v-else :class="employee.status === 'Active' ? 'text-success' : 'text-danger'">
                                {{ employee.status || '-' }}
                            </span>
                        </td>

                        <!-- Created At -->
                        <td>
                            <span v-if="employee.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(employee.created_at) }}</span>
                        </td>

                        <!-- Updated At -->
                        <td>
                            <span v-if="employee.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(employee.updated_at) }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="employee.isEditing || employee.isNew" class="btn-group" role="group">
                                <button @click="handleSave(employee, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Employee">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editEmployee(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Employee">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteEmployee(employee.id, index)"
                                    class="btn btn-outline-danger btn-sm" title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.employees.length === 0 && displayEmployees.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No employees found</h5>
                <p class="text-muted">Start by adding your first employee</p>
                <button @click="addNewEmployee" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Employee
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useEmployeeStore } from '@/stores/hrm/employeeStore'

const store = useEmployeeStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

// Create a computed property that combines store employees with any new/editing employees
const displayEmployees = computed(() => {
    return store.employees.map(employee => ({
        ...employee,
        isEditing: employee.isEditing || false,
        isNew: employee.isNew || false
    }))
})

onMounted(async () => {
    await store.fetchEmployees()
})

const addNewEmployee = () => {
    const newEmployee = {
        id: null,
        first_name: '',
        last_name: '',
        email: '',
        phone_number: '',
        date_of_birth: '',
        date_hired: '',
        position: '',
        department: '',
        manager: '',
        current_salary: '',
        status: 'Active',
        created_at: null,
        updated_at: null,
        isNew: true,
        isEditing: true
    }

    // Add to the beginning of the store's employees array
    store.employees.unshift(newEmployee)
}

const editEmployee = (index) => {
    // Store original data for cancel functionality
    originalData.value[index] = { ...store.employees[index] }

    // Set editing mode
    store.employees[index].isEditing = true
}

const cancelEdit = (index) => {
    const employee = store.employees[index]

    if (employee.isNew) {
        // Remove new employee
        store.employees.splice(index, 1)
    } else {
        // Restore original data
        if (originalData.value[index]) {
            Object.assign(store.employees[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.employees[index].isEditing = false
    }

    // Clear errors for this row
    clearRowErrors(index)
}

const handleSave = async (employee, index) => {
    try {
        isSaving.value = true

        // Clear previous errors
        clearRowErrors(index)

        // Validate the employee data
        if (!validateEmployee(employee, index)) {
            isSaving.value = false
            return
        }

        // Prepare employee data
        const employeeData = {
            first_name: employee.first_name.trim(),
            last_name: employee.last_name?.trim() || '',
            email: employee.email?.trim() || '',
            phone_number: employee.phone_number?.trim() || '',
            date_of_birth: employee.date_of_birth || '',
            date_hired: employee.date_hired || '',
            position: employee.position?.trim() || '',
            department: employee.department?.trim() || '',
            manager: employee.manager?.trim() || '',
            current_salary: employee.current_salary || '',
            status: employee.status
        }

        if (employee.isNew) {
            // Create new employee
            await store.addEmployee(employeeData)
            // Remove the temporary employee and refresh the list
            store.employees.splice(index, 1)
            await store.fetchEmployees()
        } else {
            // Update existing employee
            await store.updateEmployee(employee.id, employeeData)
            // Exit editing mode
            store.employees[index].isEditing = false
            delete originalData.value[index]
        }

        // Show success message
        console.log(`Employee ${employee.isNew ? 'created' : 'updated'} successfully!`)

    } catch (error) {
        console.error('Error saving employee:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save employee. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateEmployee = (employee, index) => {
    let isValid = true

    // Required field validation
    if (!employee.first_name?.trim()) {
        errors.value[`${index}.first_name`] = 'First name is required'
        isValid = false
    }

    // Email validation
    if (employee.email && !isValidEmail(employee.email)) {
        errors.value[`${index}.email`] = 'Please enter a valid email address'
        isValid = false
    }

    return isValid
}

const validateField = (index, field) => {
    const employee = store.employees[index]
    const errorKey = `${index}.${field}`

    // Clear existing error
    delete errors.value[errorKey]

    // Validate specific field
    switch (field) {
        case 'first_name':
            if (!employee.first_name?.trim()) {
                errors.value[errorKey] = 'First name is required'
            }
            break
        case 'email':
            if (employee.email && !isValidEmail(employee.email)) {
                errors.value[errorKey] = 'Please enter a valid email address'
            }
            break
    }
}

const isValidEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
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

const deleteEmployee = async (id, index) => {
    if (confirm('Are you sure you want to delete this employee? This action cannot be undone.')) {
        try {
            await store.removeEmployee(id)
        } catch (error) {
            console.error('Error deleting employee:', error)
            alert('Failed to delete employee. Please try again.')
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