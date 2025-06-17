<template>
    <div class="inventory-table-container">
        <div class="table-header d-flex justify-content-between align-items-center mb-4">
            <h2 class="table-title">Department List</h2>
            <button class="btn btn-primary add-btn" @click="isEdit = false; selectedDepartment = null;">
                <i class="bi bi-plus-lg"></i> Add Department
            </button>
        </div>
        <div class="table-responsive modern-table">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>S.No </th>
                        <th>Department Name</th>
                        <th>Description</th>
                        <th>Manager</th>
                        <th class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="department in departments" :key="department.id">
                        <td>{{ department.id }}</td>
                        <td class="fw-semibold">{{ department.name }}</td>
                        <td>{{ department.description || '-' }}</td>
                        <td>{{ department.manager || '-' }}</td>

                        <td class="text-center">
                            <button class="btn btn-outline-primary btn-sm me-2" title="Edit">
                                <i class="bi bi-pencil"></i>
                            </button>
                            <button class="btn btn-outline-danger btn-sm" title="Delete">
                                <i class="bi bi-trash"></i>
                            </button>
                        </td>
                    </tr>
                    <tr v-if="departments.length === 0">
                        <td colspan="8" class="text-center text-muted py-4">No Departments found.</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useDepartmentStore } from '@/stores/hrm/departmentStore';

const departmentStore = useDepartmentStore();
const departments = ref([]);
const selectedDepartment = ref(null);
const isEdit = ref(false);


onMounted(async () => {
    await departmentStore.fetchDepartments();
    departments.value = departmentStore.departments;
});

const handleDelete = async (departmentId) => {
    try {
        await departmentStore.deleteDepartment(departmentId);
        departments.value = departments.value.filter(dept => dept.id !== departmentId);
    } catch (error) {
        console.error('Error deleting department:', error);
    }
};

const handleEdit = (department) => {
    departmentStore.setSelectedDepartment(department);
    departmentStore.isEditMode = true;
};

const handleAdd = () => {
    departmentStore.setSelectedDepartment(null);
    departmentStore.isEditMode = false;
};

const handleUpdate = async (departmentData) => {
    try {
        if (departmentStore.isEditMode) {
            await departmentStore.updateDepartment(departmentStore.selectedDepartment.id, departmentData);
        } else {
            await departmentStore.addDepartment(departmentData);
        }
        departments.value = departmentStore.departments;
    } catch (error) {
        console.error('Error saving department:', error);
    }
};

</script>