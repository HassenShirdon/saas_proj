<template>
    <div class="container-fluid p-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Attendancess</h1>
            <button @click="openAddModal" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add attendance
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading Attendance...</p>
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
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(attendance, index) in store.attendances" :key="attendance.id">
                        <th scope="row">{{ index + 1 }}</th>
                        <td class="fw-semibold">{{ attendance.employee }}</td>
                        <td>{{ attandance.date || '-' }}</td>
                        <td>

                            {{ attendance.check_in_time }}
                            < </td>
                        <td>

                            {{ customer.phone_number }}

                        </td>
                        <td>

                            {{ attendance.check_out_time }}
                        </td>
                        <td class="text-center">
                            <div class="btn-group" role="group">

                                <button @click="openEditModal(attendance)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Customer">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteAttendance(attendance.id)" class="btn btn-outline-danger btn-sm"
                                    title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>

                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.attendances.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No attendance found</h5>
                <p class="text-muted">Start by adding your first attendance</p>
                <button @click="openAddModal" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Attendance
                </button>
            </div>
        </div>

        <!-- Customer Modal Component -->

    </div>
</template>
<script setup>
import { onMounted, ref } from 'vue'
import { useAttendanceStore } from '@/stores/hrm/attendanceStore'
import AttendanceModal from '@/components/hrm_modals/attendanceModal.vue'

const store = useAttendanceStore()
const showModal = ref(false)
const selectedAttendance = ref(null)
const isEdit = ref(false)

onMounted(async () => {
    await store.fetchAttendances()
})
const openAddModal = () => {
    selectedAttendance.value = null
    isEdit.value = false
    showModal.value = true
}
const openEditModal = (attendance) => {
    selectedAttendance.value = { ...attendance }
    isEdit.value = true
    showModal.value = true
}
const closeModal = () => {
    showModal.value = false
    selectedAttendance.value = null
    isEdit.value = false
}
const handleSave = async (attendanceData) => {
    try {
        if (isEdit.value) {
            await store.updateAttendance(selectedAttendance.value.id, attendanceData)
        } else {
            await store.addAttendance(attendanceData)
        }
        closeModal()
    } catch (error) {
        console.error('Error saving attendance:', error)
        // You might want to show an error message to the user here
    }
}
const deleteAttendance = async (id) => {
    if (confirm('Are you sure you want to delete this attendance record? This action cannot be undone.')) {
        try {
            await store.removeAttendance(id)
        } catch (error) {
            console.error('Error deleting attendance:', error)
            // You might want to show an error message to the user here
        }
    }
}




</script>