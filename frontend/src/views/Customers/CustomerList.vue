<!-- src/views/Customers/CustomerList.vue -->
<template>
    <div class="p-4">
        <h1 class="text-2xl font-bold mb-4">Customers List</h1>

        <ul v-if="!store.loading">
            <li v-for="customer in store.customers" :key="customer.id" class="border p-2 my-2">
                <div class="flex justify-between">
                    <div>
                        <h2 class="font-semibold">{{ customer.name }}</h2>
                        <p>Contact: {{ customer.contact_person }}</p>
                        <p>Email: {{ customer.email }}</p>
                        <p>Phone: {{ customer.phone }}</p>
                    </div>
                    <div class="space-x-2">
                        <button @click="edit(customer)" class="p-1 bg-blue-500 text-white rounded">✏️</button>
                        <button @click="remove(customer.id)" class="p-1 bg-red-500 text-white rounded">🗑️</button>
                    </div>
                </div>
            </li>
        </ul>

        <p v-else>Loading...</p>

        <!-- Debug info -->
        <div class="mt-4 p-2 bg-gray-100 text-sm">
            <p>Debug Info:</p>
            <p>Loading: {{ store.loading }}</p>
            <p>Customers count: {{ store.customers.length }}</p>
            <p>Customers data: {{ JSON.stringify(store.customers, null, 2) }}</p>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useCustomerStore } from '@/stores/inventory/customerStore'

const store = useCustomerStore()
const selected = ref(null)

onMounted(async () => {
    console.log('Component mounted, fetching customers...')
    await store.fetchCustomers()
    console.log('Customers fetched:', store.customers)
})

const handleCreate = async (data) => {
    await store.addCustomer(data)
}

const handleUpdate = async (data) => {
    await store.updateCustomer(selected.value.id, data)
    selected.value = null
}

const edit = (customer) => {
    selected.value = { ...customer }
}

const remove = async (id) => {
    if (confirm('Delete this customer?')) {
        await store.removeCustomer(id)
    }
}
</script>