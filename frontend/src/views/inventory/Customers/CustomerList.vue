<!-- src/views/Customers/CustomerList.vue -->
<template>
    <div class="container-fluid p-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Customers List</h1>
            <button @click="openAddModal" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Customer
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading customers...</p>
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
                    <tr v-for="(customer, index) in store.customers" :key="customer.id">
                        <th scope="row">{{ index + 1 }}</th>
                        <td class="fw-semibold">{{ customer.name }}</td>
                        <td>{{ customer.contact_person || '-' }}</td>
                        <td>
                            <a v-if="customer.email" :href="`mailto:${customer.email}`" class="text-decoration-none">
                                {{ customer.email }}
                            </a>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td>
                            <a v-if="customer.phone_number" :href="`tel:${customer.phone_number}`"
                                class="text-decoration-none">
                                {{ customer.phone_number }}
                            </a>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td>
                            <span v-if="customer.address" class="d-inline-block text-truncate" style="max-width: 200px;"
                                :title="customer.address">
                                {{ customer.address }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td class="text-center">
                            <div class="btn-group" role="group">
                                <button @click="openEditModal(customer)" class="btn btn-sm btn-outline-primary"
                                    type="button" title="Edit Customer">
                                    <i class="fas fa-edit"></i>
                                </button>
                                <button @click="deleteCustomer(customer.id)" class="btn btn-sm btn-outline-danger"
                                    type="button" title="Delete Customer">
                                    <i class="fas fa-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.customers.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No customers found</h5>
                <p class="text-muted">Start by adding your first customer</p>
                <button @click="openAddModal" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Customer
                </button>
            </div>
        </div>

        <!-- Customer Modal Component -->
        <CustomerModal :show="showModal" :customer="selectedCustomer" :is-edit="isEdit" @close="closeModal"
            @save="handleSave" />

        <!-- Debug info (remove in production) -->
        <div class="mt-4 p-3 bg-light border rounded small" v-if="showDebug">
            <h6 class="mb-2">Debug Info:</h6>
            <p class="mb-1">Loading: {{ store.loading }}</p>
            <p class="mb-1">Customers count: {{ store.customers.length }}</p>
            <details>
                <summary class="text-primary" style="cursor: pointer;">View Customers Data</summary>
                <pre class="mt-2 bg-white p-2 border rounded">{{ JSON.stringify(store.customers, null, 2) }}</pre>
            </details>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCustomerStore } from '@/stores/inventory/customerStore'
import CustomerModal from '@/components/customers/CustomerModal.vue'

const store = useCustomerStore()
const showModal = ref(false)
const selectedCustomer = ref(null)
const isEdit = ref(false)
const showDebug = ref(false) // Set to true for debugging

onMounted(async () => {
    console.log('Component mounted, fetching customers...')
    await store.fetchCustomers()
    console.log('Customers fetched:', store.customers)
})

const openAddModal = () => {
    selectedCustomer.value = null
    isEdit.value = false
    showModal.value = true
}

const openEditModal = (customer) => {
    selectedCustomer.value = { ...customer }
    isEdit.value = true
    showModal.value = true
}

const closeModal = () => {
    showModal.value = false
    selectedCustomer.value = null
    isEdit.value = false
}

const handleSave = async (customerData) => {
    try {
        if (isEdit.value) {
            await store.updateCustomer(selectedCustomer.value.id, customerData)
        } else {
            await store.addCustomer(customerData)
        }
        closeModal()
    } catch (error) {
        console.error('Error saving customer:', error)
        // You might want to show an error message to the user here
    }
}

const deleteCustomer = async (id) => {
    if (confirm('Are you sure you want to delete this customer? This action cannot be undone.')) {
        try {
            await store.removeCustomer(id)
        } catch (error) {
            console.error('Error deleting customer:', error)
            // You might want to show an error message to the user here
        }
    }
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

@media (max-width: 768px) {
    .table-responsive {
        font-size: 0.875rem;
    }

    .btn-sm {
        padding: 0.25rem 0.5rem;
        font-size: 0.75rem;
    }
}
</style>