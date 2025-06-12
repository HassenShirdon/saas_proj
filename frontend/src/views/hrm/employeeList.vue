<template>
    <div class="inventory-table-container">
        <div class="table-header">
            <h2 class="table-title">Employee List</h2>
            <button class="btn btn-primary add-btn" @click="isEdit = false; selectedEmployee = null;">
                <i class="bi bi-plus-lg"></i> Add Employee
            </button>
        </div>
        <div class="table-responsive modern-table">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>S. No </th>
                        <th>Fist Name</th>
                        <th>Last Name</th>
                        <th>Email</th>
                        <th>Date of Birth</th>
                        <th>Hired Date</th>
                        <th>Position</th>
                        <th class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(employee, index) in store.employees" :key="employee.email">
                        <td>{{ index + 1 }}</td>
                        <td class="fw-semibold">{{ employee.first_name }}</td>
                        <td>{{ employee.last_name || '-' }}</td>
                        <td> {{ employee.email }}

                        </td>
                        <td>
                            <span v-if="employee.date_of_birth">${{ employee.date_of_birth }}</span>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td>
                            <span v-if="employee.hired_date">${{ employee.hired_date }}</span>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td>
                            {{ employee.position }}
                        </td>
                        <td class="text-center">
                            <button class="btn btn-outline-primary btn-sm me-2" title="Edit">
                                <i class="bi bi-pencil"></i>
                            </button>
                            <button class="btn btn-outline-danger btn-sm" title="Delete">
                                <i class="bi bi-trash"></i>
                            </button>
                        </td>
                    </tr>
                    <tr v-if="store.employees.length === 0">
                        <td colspan="8" class="text-center text-muted py-4">No Employees found.</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useEmployeeStore } from '@/stores/hrm/employeeStore'


const store = useEmployeeStore()
const selectedEmployee = ref(null)
const isEdit = ref(false)

onMounted(async () => {
    await store.fetchEmployees()
})

const handleSave = async (employeeData) => {
    try {
        if (isEdit.value) {
            await store.updateEmployee(selectedEmployee.value.id, itemData)
        } else {
            await store.addEmployee(employeeData)
        }
    } catch (error) {
        console.error('Error saving item:', error)
    }
}

const deleteEmployee = async (id) => {
    if (confirm('Are you sure you want to delete this Employee? This action cannot be undone.')) {
        try {
            await store.removeEmployee(id)
        } catch (error) {
            console.error('Error deleting Employee:', error)
        }
    }
}
</script>

<style scoped>
.inventory-table-container {
    background: #fff;
    border-radius: 18px;
    box-shadow: 0 4px 24px 0 rgba(0, 0, 0, 0.07);
    padding: 32px 24px 24px 24px;
    max-width: 1100px;
    margin: 40px auto;
}

.table-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 18px;
}

.table-title {
    font-size: 1.7rem;
    font-weight: 700;
    color: #2d3748;
    margin: 0;
}

.add-btn {
    font-weight: 600;
    border-radius: 8px;
    padding: 8px 18px;
    font-size: 1rem;
    box-shadow: 0 2px 8px 0 rgba(0, 123, 255, 0.08);
    transition: background 0.2s;
}

.add-btn i {
    margin-right: 6px;
}

.table-responsive {
    margin-top: 20px;
}

.modern-inventory-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    background: #f9fafb;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.04);
}

.modern-inventory-table thead tr {
    background: linear-gradient(90deg, #2563eb 0%, #1e40af 100%);
    color: #fff;
}

.modern-inventory-table th,
.modern-inventory-table td {
    padding: 14px 16px;
    text-align: left;
    font-size: 1rem;
}

.modern-inventory-table th {
    font-weight: 700;
    letter-spacing: 0.02em;
    border-bottom: 2px solid #e5e7eb;
}

.modern-inventory-table tbody tr {
    background: #fff;
    transition: background 0.2s;
}

.modern-inventory-table tbody tr:hover {
    background: #f1f5f9;
}

.modern-inventory-table td {
    border-bottom: 1px solid #e5e7eb;
    vertical-align: middle;
}

.modern-inventory-table td .btn {
    min-width: 36px;
    min-height: 36px;
    border-radius: 6px;
    font-size: 1.1rem;
    transition: box-shadow 0.2s;
}

.modern-inventory-table td .btn-outline-primary {
    border-color: #2563eb;
    color: #2563eb;
}

.modern-inventory-table td .btn-outline-primary:hover {
    background: #2563eb;
    color: #fff;
}

.modern-inventory-table td .btn-outline-danger {
    border-color: #ef4444;
    color: #ef4444;
}

.modern-inventory-table td .btn-outline-danger:hover {
    background: #ef4444;
    color: #fff;
}

.desc-truncate {
    display: inline-block;
    max-width: 180px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    vertical-align: bottom;
}

.text-muted {
    color: #9ca3af !important;
}

@media (max-width: 900px) {
    .inventory-table-container {
        padding: 16px 4px;
    }

    .modern-inventory-table th,
    .modern-inventory-table td {
        padding: 10px 8px;
        font-size: 0.95rem;
    }

    .table-title {
        font-size: 1.2rem;
    }
}
</style>