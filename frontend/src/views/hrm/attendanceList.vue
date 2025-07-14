<!-- src/views/Attendance/attendanceList.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="container d-flex justify-content-between align-items-center p-4 mb-4 shadow-sm">
            <h1 class="h2 mb-0">Attendance List</h1>
            <button @click="addNewAttendance" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Attendance
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading attendance...</p>
        </div>

        <!-- Attendance Table -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Employee</th>
                        <th scope="col">Date</th>
                        <th scope="col">Check-in Time</th>
                        <th scope="col">Check-out Time</th>
                        <th scope="col">Status</th>
                        <th scope="col">Created At</th>
                        <th scope="col">Updated At</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(attendance, index) in displayAttendances" :key="attendance.id || `new-${index}`"
                        :class="{ 'table-warning': attendance.isEditing || attendance.isNew }">
                        <th scope="row">{{ attendance.isNew ? 'NEW' : index + 1 }}</th>

                        <!-- Employee Field -->
                        <td>
                            <input v-if="attendance.isEditing || attendance.isNew" v-model="attendance.employee"
                                type="text" class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.employee`] }" placeholder="Employee name"
                                @blur="validateField(index, 'employee')" />
                            <div v-if="errors[`${index}.employee`]" class="invalid-feedback">
                                {{ errors[`${index}.employee`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ attendance.employee || '-' }}</span>
                        </td>

                        <!-- Date Field -->
                        <td>
                            <input v-if="attendance.isEditing || attendance.isNew" v-model="attendance.date" type="date"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.date`] }"
                                @blur="validateField(index, 'date')" />
                            <div v-if="errors[`${index}.date`]" class="invalid-feedback">
                                {{ errors[`${index}.date`] }}
                            </div>
                            <span v-else>{{ attendance.date || '-' }}</span>
                        </td>

                        <!-- Check-in Time Field -->
                        <td>
                            <input v-if="attendance.isEditing || attendance.isNew" v-model="attendance.check_in_time"
                                type="time" class="form-control form-control-sm" placeholder="Check-in time" />
                            <span v-else>{{ attendance.check_in_time || '-' }}</span>
                        </td>

                        <!-- Check-out Time Field -->
                        <td>
                            <input v-if="attendance.isEditing || attendance.isNew" v-model="attendance.check_out_time"
                                type="time" class="form-control form-control-sm" placeholder="Check-out time" />
                            <span v-else>{{ attendance.check_out_time || '-' }}</span>
                        </td>

                        <!-- Status Field -->
                        <td>
                            <select v-if="attendance.isEditing || attendance.isNew" v-model="attendance.is_active"
                                class="form-select form-select-sm">
                                <option :value="true">Present</option>
                                <option :value="false">Absent</option>
                            </select>
                            <span v-else :class="attendance.is_active ? 'text-success' : 'text-danger'">
                                {{ attendance.is_active ? 'Present' : 'Absent' }}
                            </span>
                        </td>

                        <!-- Created At -->
                        <td>
                            <span v-if="attendance.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(attendance.created_at) }}</span>
                        </td>

                        <!-- Updated At -->
                        <td>
                            <span v-if="attendance.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(attendance.updated_at) }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="attendance.isEditing || attendance.isNew" class="btn-group" role="group">
                                <button @click="handleSave(attendance, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Attendance">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editAttendance(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Attendance">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteAttendance(attendance.id, index)"
                                    class="btn btn-outline-danger btn-sm" title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.attendances.length === 0 && displayAttendances.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No attendance found</h5>
                <p class="text-muted">Start by adding your first attendance</p>
                <button @click="addNewAttendance" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Attendance
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useAttendanceStore } from '@/stores/hrm/attendanceStore'

const store = useAttendanceStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

// Create a computed property that combines store attendances with any new/editing attendances
const displayAttendances = computed(() => {
    return store.attendances.map(attendance => ({
        ...attendance,
        isEditing: attendance.isEditing || false,
        isNew: attendance.isNew || false
    }))
})

onMounted(async () => {
    await store.fetchAttendances()
})

const addNewAttendance = () => {
    const newAttendance = {
        id: null,
        employee: '',
        date: '',
        check_in_time: '',
        check_out_time: '',
        is_active: true,
        created_at: null,
        updated_at: null,
        isNew: true,
        isEditing: true
    }

    // Add to the beginning of the store's attendances array
    store.attendances.unshift(newAttendance)
}

const editAttendance = (index) => {
    // Store original data for cancel functionality
    originalData.value[index] = { ...store.attendances[index] }

    // Set editing mode
    store.attendances[index].isEditing = true
}

const cancelEdit = (index) => {
    const attendance = store.attendances[index]

    if (attendance.isNew) {
        // Remove new attendance
        store.attendances.splice(index, 1)
    } else {
        // Restore original data
        if (originalData.value[index]) {
            Object.assign(store.attendances[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.attendances[index].isEditing = false
    }

    // Clear errors for this row
    clearRowErrors(index)
}

const handleSave = async (attendance, index) => {
    try {
        isSaving.value = true

        // Clear previous errors
        clearRowErrors(index)

        // Validate the attendance data
        if (!validateAttendance(attendance, index)) {
            isSaving.value = false
            return
        }

        // Prepare attendance data (exclude Vue-specific properties)
        const attendanceData = {
            employee: attendance.employee.trim(),
            date: attendance.date,
            check_in_time: attendance.check_in_time || '',
            check_out_time: attendance.check_out_time || '',
            is_active: attendance.is_active
        }

        if (attendance.isNew) {
            // Create new attendance
            await store.addAttendance(attendanceData)

            // Remove the temporary attendance and refresh the list
            store.attendances.splice(index, 1)
            await store.fetchAttendances()
        } else {
            // Update existing attendance
            await store.updateAttendance(attendance.id, attendanceData)

            // Exit editing mode
            store.attendances[index].isEditing = false
            delete originalData.value[index]
        }

        // Show success message
        console.log(`Attendance ${attendance.isNew ? 'created' : 'updated'} successfully!`)

    } catch (error) {
        console.error('Error saving attendance:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save attendance. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateAttendance = (attendance, index) => {
    let isValid = true

    // Required field validation
    if (!attendance.employee?.trim()) {
        errors.value[`${index}.employee`] = 'Employee name is required'
        isValid = false
    }

    if (!attendance.date) {
        errors.value[`${index}.date`] = 'Date is required'
        isValid = false
    }

    return isValid
}

const validateField = (index, field) => {
    const attendance = store.attendances[index]
    const errorKey = `${index}.${field}`

    // Clear existing error
    delete errors.value[errorKey]

    // Validate specific field
    switch (field) {
        case 'employee':
            if (!attendance.employee?.trim()) {
                errors.value[errorKey] = 'Employee name is required'
            }
            break
        case 'date':
            if (!attendance.date) {
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

const deleteAttendance = async (id, index) => {
    if (confirm('Are you sure you want to delete this attendance record? This action cannot be undone.')) {
        try {
            await store.removeAttendance(id)
        } catch (error) {
            console.error('Error deleting attendance:', error)
            alert('Failed to delete attendance. Please try again.')
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