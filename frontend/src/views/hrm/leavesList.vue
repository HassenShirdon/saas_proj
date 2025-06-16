<template>
    <div class="container-fluid p-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Leaves</h1>
            <button @click="openAddModal" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Leave
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading Leave...</p>
        </div>

        <!-- leaves Table -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Employee Name</th>
                        <th scope="col">date</th>
                        <th scope="col">check_in_time</th>
                        <th scope="col">check_out_time</th>
                        <th scope="col">Reason</th>
                        <th scope="col">Status</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="leave in store.leaves" :key="leave.id">
                        <th scope="row">{{ leave.id }}</th>
                        <td class="fw-semibold">{{ leave.employee }}</td>
                        <td>{{ leaves.date || '-' }}</td>
                        <td>

                            {{ leave.check_in_time }}
                            < </td>
                        <td>

                            {{ leave.check_out_time }}
                        </td>
                        <td>

                            {{ leave.reason }}
                        </td>
                        <td>

                            {{ leave.status }}
                        </td>
                        <td class="text-center">
                            <div class="btn-group" role="group">

                                <button @click="openEditModal(leave)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit leave">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteleave(leave.id)" class="btn btn-outline-danger btn-sm"
                                    title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>

                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.leaves.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No leave found</h5>
                <p class="text-muted">Start by adding your first leave</p>
                <button @click="openAddModal" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add leave
                </button>
            </div>
        </div>

        <!-- leave Modal Component -->

    </div>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { useLeavesStore } from '@/stores/hrm/leavesStore';

const store = useLeavesStore();
const leaves = ref([]);
const selectedLeave = ref(null)
const isEdit = ref(false)



onMounted(async () => {
    await store.fetchLeaves()
})

const handleSave = async (leaveData) => {
    try {
        if (isEdit.value) {
            await store.updateleave(selectedLeave.values.id, leaveData)
        } else {
            await store.addLeave(leaveData)
        }
    } catch (error) {
        console.error('Error saving Leave:', error)
        // You might want to show an error message to the user here
    }
}

</script>
<style></style>