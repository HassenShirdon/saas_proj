<template>
  <table class="table table-auto">
    <thead class="bg-gray-200 text-white">
      <tr>
        <th scope="col">Id</th>
        <th scope="col">Name</th>
        <th scope="col">Contact_person</th>
        <th scope="col">Email</th>
        <th scope="col">Phone_number</th>
        <th scope="col">Address</th>
        <th scope="col">Action</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="customer in customers" :key="customer.id">
        <td class="border px-4 py-2">{{ customer.id }}</td>
        <td class="border px-4 py-2">{{ customer.name }}</td>
        <td class="border px-4 py-2">{{ customer.contact_person }}</td>
        <td class="border px-4 py-2">{{ customer.email }}</td>
        <td class="border px-4 py-2">{{ customer.phone_number }}</td>
        <td class="border px-4 py-2">{{ customer.address }}</td>
        <td class="border px-4 py-2">delete</td>
        <td class="border px-4 py-2">Edit</td>
      </tr>
    </tbody>
  </table>
</template>
<script setup>
import { ref, onMounted } from 'vue'
import { fetchCustomers } from '@/api/customers'

const customers = ref([])

onMounted(async () => {
  try {
    const response = await fetchCustomers()
    customers.value = response.data
    console.log('Loaded customers:', customers.value)
  } catch (error) {
    console.error('Error loading customers:', error)
  }
})
</script>

<style scoped>
/* .table-auto {
  border-collapse: collapse;
  width: 100%;
}
th,
td {
  text-align: left;
} */
</style>
