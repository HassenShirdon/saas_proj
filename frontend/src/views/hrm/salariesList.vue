<template>
    <div class="container-fluid p-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">salaries</h1>
            <button @click="openAddModal" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Salary
            </button>
        </div>

        <!-- Loading State -->
        <!-- <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading salary...</p>
        </div> -->

        <!-- salaries Table -->
        <div class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">S. No</th>
                        <th scope="col">Employee Name</th>
                        <th scope="col">amount</th>
                        <th scope="col">Payment date</th>
                        <th scope="col">Notes</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="salary in salaries" :key="salary.id">
                        <th scope="row">{{ salary.id }}</th>
                        <td class="fw-semibold">{{ salary.employee }}</td>
                        <td>{{ salaries.employee || '-' }}</td>
                        <td>

                            {{ salary.amount }}
                            < </td>
                        <td>

                            {{ salary.payment_date }}
                        </td>
                        <td>

                            {{ salary.notes }}
                        </td>
                        <td class="text-center">
                            <div class="btn-group" role="group">

                                <button @click="openEditModal(salary)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit salary">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deletesalary(salary.id)" class="btn btn-outline-danger btn-sm"
                                    title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>

                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <!-- <div v-if="salaries.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No salary found</h5>
                <p class="text-muted">Start by adding your first salary</p>
            </div> -->
        </div>

        <!-- salary Modal Component -->

    </div>
</template>
<script>
import { ref, onMounted } from 'vue'
import { useSalaryStore } from '@/stores/hrm/salaryStore'

const store = useSalaryStore()
const salaries = ref([])
const selectedSalary = ref(null)
const isEdit = ref(false)


onMounted(async () => {
    await store.fetchSalaries()
    salaries.value = store.salaries
})

const handleSave = async (salaryData) => {
    try {
        if (isEdit.value) {
            await store.updateSalary(selectedsalaryData)
        } else {
            await store.addSalary(salaryData)
        }
    } catch (error) {
        console.error('Error saving Leave:', error)
        // You might want to show an error message to the user here
    }
}
const handleDelete = async (salaryId) => {
    try {
        await departmentStore.deleteSalary(salaryId);
        salaries.value = salaries.value.filter(sal => sal.id !== salaryId);
    } catch (error) {
        console.error('Error deleting department:', error);
    }
};


</script>
<style></style>