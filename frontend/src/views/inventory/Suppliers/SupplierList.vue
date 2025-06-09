<template>
    <div class="container-fluid p-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Suppliers List</h1>
            <button @click="openAddModal" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Supplier
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading suppliers...</p>
        </div>

        <!-- Suppliers Table -->
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
                    <tr v-for="(supplier, index) in store.suppliers" :key="supplier.id">
                        <th scope="row">{{ index + 1 }}</th>
                        <td class="fw-semibold">{{ supplier.name }}</td>
                        <td>{{ supplier.contact_person || '-' }}</td>
                        <td>
                            <a v-if="supplier.email" :href="`mailto:${supplier.email}`" class="text-decoration-none">
                                {{ supplier.email }}
                            </a>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td>
                            <a v-if="supplier.phone_number" :href="`tel:${supplier.phone_number}`"
                                class="text-decoration-none">
                                {{ supplier.phone_number }}
                            </a>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td>
                            <span v-if="supplier.address" class="d-inline-block text-truncate" style="max-width: 200px;"
                                :title="supplier.address">
                                {{ supplier.address }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td class="text-center">
                            <div class="btn-group" role="group">
                                <button @click="openEditModal(supplier)" class="btn btn-sm btn-outline-primary"
                                    type="button" title="Edit Supplier">
                                    <i class="fas fa-edit"></i>
                                </button>
                                <button @click="deleteSupplier(supplier.id)" class="btn btn-sm btn-outline-danger"
                                    type="button" title="Delete Supplier">
                                    <i class="fas fa-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.suppliers.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No suppliers found</h5>
                <p class="text-muted">Start by adding your first supplier</p>
                <button @click="openAddModal" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Supplier
                </button>
            </div>
        </div>

        <!-- Supplier Modal Component -->
        <SupplierModal :show="showModal" :supplier="selectedSupplier" :is-edit="isEdit" @close="closeModal"
            @save="handleSave" />

        <!-- Debug info (remove in production) -->
        <div class="mt-4 p-3 bg-light border rounded small" v-if="showDebug">
            <h6 class="mb-2">Debug Info:</h6>
            <p class="mb-1">Loading: {{ store.loading }}</p>
            <p class="mb-1">Suppliers count: {{ store.suppliers.length }}</p>
            <details>
                <summary class="text-primary" style="cursor: pointer;">View Suppliers Data</summary>
                <pre class="mt-2 bg-white p-2 border rounded">{{ JSON.stringify(store.suppliers, null, 2) }}</pre>
            </details>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useSupplierStore } from '@/stores/inventory/supplierStore'
import SupplierModal from '@/components/suppliers/SupplierModal.vue'

const store = useSupplierStore()
const showModal = ref(false)
const selectedSupplier = ref(null)
const isEdit = ref(false)
const showDebug = ref(false) // Set to true for debugging

onMounted(async () => {
    console.log('Component mounted, fetching suppliers...')
    await store.fetchSuppliers()
    console.log('Suppliers fetched:', store.suppliers)
})

const openAddModal = () => {
    selectedSupplier.value = null
    isEdit.value = false
    showModal.value = true
}

const openEditModal = (supplier) => {
    selectedSupplier.value = { ...supplier }
    isEdit.value = true
    showModal.value = true
}

const closeModal = () => {
    showModal.value = false
    selectedSupplier.value = null
    isEdit.value = false
}

const handleSave = async (supplierData) => {
    try {
        if (isEdit.value) {
            await store.updateSupplier(selectedSupplier.value.id, supplierData)
        } else {
            await store.addSupplier(supplierData)
        }
        closeModal()
    } catch (error) {
        console.error('Error saving supplier:', error)
        // You might want to show an error message to the user here
    }
}

const deleteSupplier = async (id) => {
    if (confirm('Are you sure you want to delete this supplier? This action cannot be undone.')) {
        try {
            await store.removeSupplier(id)
        } catch (error) {
            console.error('Error deleting supplier:', error)
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