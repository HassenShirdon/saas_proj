<!-- src/views/Leaves/leavesList.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="container d-flex justify-content-between align-items-center p-4 mb-4 shadow-sm">
            <h1 class="h2 mb-0">Leave List</h1>
            <button @click="addNewLeave" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Leave
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading leaves...</p>
        </div>

        <!-- Leaves Table -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Employee Name</th>
                        <th scope="col">Date</th>
                        <th scope="col">Start Time</th>
                        <th scope="col">End Time</th>
                        <th scope="col">Reason</th>
                        <th scope="col">Status</th>
                        <th scope="col">Created At</th>
                        <th scope="col">Updated At</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(leave, index) in displayLeaves" :key="leave.id || `new-${index}`"
                        :class="{ 'table-warning': leave.isEditing || leave.isNew }">
                        <th scope="row">{{ leave.isNew ? 'NEW' : index + 1 }}</th>

                        <!-- Employee Name Field -->
                        <td>
                            <input v-if="leave.isEditing || leave.isNew" v-model="leave.employee" type="text"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.employee`] }" placeholder="Employee name"
                                @blur="validateField(index, 'employee')" />
                            <div v-if="errors[`${index}.employee`]" class="invalid-feedback">
                                {{ errors[`${index}.employee`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ leave.employee || '-' }}</span>
                        </td>

                        <!-- Date Field -->
                        <td>
                            <input v-if="leave.isEditing || leave.isNew" v-model="leave.date" type="date"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.date`] }"
                                @blur="validateField(index, 'date')" />
                            <div v-if="errors[`${index}.date`]" class="invalid-feedback">
                                {{ errors[`${index}.date`] }}
                            </div>
                            <span v-else>{{ leave.date || '-' }}</span>
                        </td>

                        <!-- Start Time Field -->
                        <td>
                            <input v-if="leave.isEditing || leave.isNew" v-model="leave.check_in_time" type="time"
                                class="form-control form-control-sm" placeholder="Start time" />
                            <span v-else>{{ leave.check_in_time || '-' }}</span>
                        </td>

                        <!-- End Time Field -->
                        <td>
                            <input v-if="leave.isEditing || leave.isNew" v-model="leave.check_out_time" type="time"
                                class="form-control form-control-sm" placeholder="End time" />
                            <span v-else>{{ leave.check_out_time || '-' }}</span>
                        </td>

                        <!-- Reason Field -->
                        <td>
                            <textarea v-if="leave.isEditing || leave.isNew" v-model="leave.reason"
                                class="form-control form-control-sm" rows="2" placeholder="Reason"></textarea>
                            <span v-else-if="leave.reason" class="d-inline-block text-truncate"
                                style="max-width: 200px;" :title="leave.reason">
                                {{ leave.reason }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>

                        <!-- Status Field -->
                        <td>
                            <select v-if="leave.isEditing || leave.isNew" v-model="leave.status"
                                class="form-select form-select-sm">
                                <option value="Approved">Approved</option>
                                <option value="Pending">Pending</option>
                                <option value="Rejected">Rejected</option>
                            </select>
                            <span v-else :class="{
                                'text-success': leave.status === 'Approved',
                                'text-warning': leave.status === 'Pending',
                                'text-danger': leave.status === 'Rejected'
                            }">
                                {{ leave.status || '-' }}
                            </span>
                        </td>

                        <!-- Created At -->
                        <td>
                            <span v-if="leave.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(leave.created_at) }}</span>
                        </td>

                        <!-- Updated At -->
                        <td>
                            <span v-if="leave.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(leave.updated_at) }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="leave.isEditing || leave.isNew" class="btn-group" role="group">
                                <button @click="handleSave(leave, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Leave">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editLeave(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Leave">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteLeave(leave.id, index)" class="btn btn-outline-danger btn-sm"
                                    title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.leaves.length === 0 && displayLeaves.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No leaves found</h5>
                <p class="text-muted">Start by adding your first leave</p>
                <button @click="addNewLeave" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Leave
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useLeavesStore } from '@/stores/hrm/leavesStore'

const store = useLeavesStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

// Create a computed property that combines store leaves with any new/editing leaves
const displayLeaves = computed(() => {
    return store.leaves.map(leave => ({
        ...leave,
        isEditing: leave.isEditing || false,
        isNew: leave.isNew || false
    }))
})

onMounted(async () => {
    await store.fetchLeaves()
})

const addNewLeave = () => {
    const newLeave = {
        id: null,
        employee: '',
        date: '',
        check_in_time: '',
        check_out_time: '',
        reason: '',
        status: 'Pending',
        created_at: null,
        updated_at: null,
        isNew: true,
        isEditing: true
    }

    // Add to the beginning of the store's leaves array
    store.leaves.unshift(newLeave)
}

const editLeave = (index) => {
    // Store original data for cancel functionality
    originalData.value[index] = { ...store.leaves[index] }

    // Set editing mode
    store.leaves[index].isEditing = true
}

const cancelEdit = (index) => {
    const leave = store.leaves[index]

    if (leave.isNew) {
        // Remove new leave
        store.leaves.splice(index, 1)
    } else {
        // Restore original data
        if (originalData.value[index]) {
            Object.assign(store.leaves[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.leaves[index].isEditing = false
    }

    // Clear errors for this row
    clearRowErrors(index)
}

const handleSave = async (leave, index) => {
    try {
        isSaving.value = true

        // Clear previous errors
        clearRowErrors(index)

        // Validate the leave data
        if (!validateLeave(leave, index)) {
            isSaving.value = false
            return
        }

        // Prepare leave data
        const leaveData = {
            employee: leave.employee.trim(),
            date: leave.date,
            check_in_time: leave.check_in_time || '',
            check_out_time: leave.check_out_time || '',
            reason: leave.reason?.trim() || '',
            status: leave.status
        }

        if (leave.isNew) {
            // Create new leave
            await store.addLeave(leaveData)
            // Remove the temporary leave and refresh the list
            store.leaves.splice(index, 1)
            await store.fetchLeaves()
        } else {
            // Update existing leave
            await store.updateLeave(leave.id, leaveData)
            // Exit editing mode
            store.leaves[index].isEditing = false
            delete originalData.value[index]
        }

        // Show success message
        console.log(`Leave ${leave.isNew ? 'created' : 'updated'} successfully!`)

    } catch (error) {
        console.error('Error saving leave:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save leave. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateLeave = (leave, index) => {
    let isValid = true

    // Required field validation
    if (!leave.employee?.trim()) {
        errors.value[`${index}.employee`] = 'Employee name is required'
        isValid = false
    }

    if (!leave.date) {
        errors.value[`${index}.date`] = 'Date is required'
        isValid = false
    }

    return isValid
}

const validateField = (index, field) => {
    const leave = store.leaves[index]
    const errorKey = `${index}.${field}`

    // Clear existing error
    delete errors.value[errorKey]

    // Validate specific field
    switch (field) {
        case 'employee':
            if (!leave.employee?.trim()) {
                errors.value[errorKey] = 'Employee name is required'
            }
            break
        case 'date':
            if (!leave.date) {
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

const deleteLeave = async (id, index) => {
    if (confirm('Are you sure you want to delete this leave record? This action cannot be undone.')) {
        try {
            await store.deleteLeave(id)
        } catch (error) {
            console.error('Error deleting leave:', error)
            alert('Failed to delete leave. Please try again.')
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