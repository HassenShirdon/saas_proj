<template>
    <div class="container-fluid p-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Employee List</h1>
            <button @click="openAddModal" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Employee
            </button>
        </div>
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading employee...</p>
        </div>
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">S.No</th>
                        <th scope="col">First Name</th>
                        <th scope="col">Last Name</th>
                        <th scope="col">Email</th>
                        <th scope="col">Date of Birth</th>
                        <th scope="col">Hired Date</th>
                        <th scope="col">Position</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(employee, index) in store.employees" :key="employee.id">
                        <th scope="row">{{ index + 1 }}</th>
                        <td class="fw-semibold">{{ employee.first_name }}</td>
                        <td>{{ employee.last_name || '-' }}</td>
                        <td>
                            <a v-if="employee.email" :href="`mailto:${employee.email}`" class="text-decoration-none">
                                {{ employee.email }}
                            </a>
                            <span v-else class="text-muted">-</span>
                        </td>

                        <td>
                            <span v-if="employee.date_of_birth" class="d-inline-block text-truncate"
                                style="max-width: 200px;" :title="employee.date_of_birth">
                                {{ employee.date_of_birth }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td>{{ employee.hired_date || '-' }}</td>
                        <td>{{ employee.position || '-' }}</td>
                        <td class="text-center">
                            <div class="btn-group" role="group">

                                <button @click="openEditModal(employee)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Employee">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteEmployee(employee.id)" class="btn btn-outline-danger btn-sm"
                                    title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>

                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.employees.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No Employees found</h5>
                <p class="text-muted">Start by adding your first Employee</p>
                <button @click="openAddModal" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Employee
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useEmployeeStore } from '@/stores/hrm/employeeStore'

const store = useEmployeeStore()
const selectedEmployee = ref(null)
const showModal = ref(false)
const isEdit = ref(false)

onMounted(async () => {
    console.log('Component mounted, fetching employees...')
    await store.fetchEmployees()
    console.log('Employees fetched:', store.employees)
})

const openAddModal = () => {
    selectedEmployee.value = null
    isEdit.value = false
    showModal.value = true
}

const openEditModal = (employee) => {
    selectedEmployee.value = { ...employee }
    isEdit.value = true
    showModal.value = true
}
const closeModal = () => {
    showModal.value = false
    selectedEmployee.value = null
    isEdit.value = false
}

const handleSave = async (employeeData) => {
    try {
        if (isEdit.value) {
            await store.updateEmployee(selectedEmployee.value.id, employeeData)
        } else {
            await store.addEmployee(employeeData)
        }
        closeModal()
    } catch (error) {
        console.error('Error saving employee:', error)
        // You might want to show an error message to the user here
    }
}

const deleteEmployee = async (id) => {
    if (confirm('Are you sure you want to delete this employee? This action cannot be undone.')) {
        try {
            await store.removeEmployee(id)
        } catch (error) {
            console.error('Error deleting employee:', error)
            // You might want to show an error message to the user here
        }
    }
}




</script>