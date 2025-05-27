<template>
  <div class="customer-table-container">
    <div class="table-header text-center ">
      <h2 class="text-primary"><i class="bi bi-person-fill-gear p-2 "></i>Customer Management</h2>
      <div class="table-controls">

        <button class="btn-add" @click="openAddModal">
          <i class="bi bi-plus-lg"></i> Add Customer
        </button>
      </div>
    </div>

    <div class="table-responsive">
      <table class="customer-table">
        <thead>
          <tr>
            <th class="text-center" style="width: 80px;">ID</th>
            <th>Customer Name</th>
            <th>Contact Person</th>
            <th>Email</th>
            <th>Phone</th>
            <th class="text-center" style="width: 120px;">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="customer in filteredCustomers" :key="customer.id">
            <td class="text-center">{{ customer.id }}</td>
            <td>
              <div class="customer-name">
                <div class="avatar">{{ getInitials(customer.name) }}</div>
                <span>{{ customer.name }}</span>
              </div>
            </td>
            <td>{{ customer.contact_person }}</td>
            <td>
              <a :href="`mailto:${customer.email}`" class="email-link">
                {{ customer.email }}
              </a>
            </td>
            <td>
              <a :href="`tel:${customer.phone_number}`" class="phone-link">
                {{ formatPhoneNumber(customer.phone_number) }}
              </a>
            </td>
            <td class="action-buttons">
              <button class="btn-action btn-edit" @click="editCustomer(customer.id)">
                <i class="bi bi-pencil"></i>
              </button>
              <button class="btn-action btn-delete" @click="confirmDelete(customer.id)">
                <i class="bi bi-trash"></i>
              </button>
              <button class="btn-action btn-view" @click="viewCustomer(customer.id)">
                <i class="bi bi-eye"></i>
              </button>
            </td>
          </tr>
          <tr v-if="filteredCustomers.length === 0">
            <td colspan="6" class="no-results">
              No customers found matching your search criteria
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="table-footer">
      <div class="pagination-info">
        Showing {{ filteredCustomers.length }} of {{ customers.length }} customers
      </div>
      <div class="pagination-controls">
        <button class="btn-pagination" :disabled="currentPage === 1" @click="prevPage">
          <i class="bi bi-chevron-left"></i>
        </button>
        <span class="page-indicator">Page {{ currentPage }}</span>
        <button class="btn-pagination" :disabled="currentPage * itemsPerPage >= customers.length" @click="nextPage">
          <i class="bi bi-chevron-right"></i>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { fetchCustomers } from '@/api/customers'

const customers = ref([])
const searchQuery = ref('')
const currentPage = ref(1)
const itemsPerPage = ref(10)

onMounted(async () => {
  try {
    const response = await fetchCustomers()
    customers.value = response.data
  } catch (error) {
    console.error('Error loading customers:', error)
  }
})

const filteredCustomers = computed(() => {
  const query = searchQuery.value.toLowerCase()
  return customers.value.filter(customer =>
    customer.name.toLowerCase().includes(query) ||
    customer.contact_person.toLowerCase().includes(query) ||
    customer.email.toLowerCase().includes(query) ||
    customer.phone_number.includes(query))
})

function formatPhoneNumber(phone) {
  return phone.replace(/(\d{3})(\d{3})(\d{4})/, '($1) $2-$3')
}

function getInitials(name) {
  return name.split(' ').map(n => n[0]).join('').toUpperCase()
}

function prevPage() {
  if (currentPage.value > 1) currentPage.value--
}

function nextPage() {
  if (currentPage.value * itemsPerPage.value < customers.value.length) currentPage.value++
}

function editCustomer(id) {
  console.log('Edit customer', id)
  // Implement edit functionality
}

function confirmDelete(id) {
  console.log('Delete customer', id)
  // Implement delete confirmation modal
}

function viewCustomer(id) {
  console.log('View customer', id)
  // Implement view functionality
}

function openAddModal() {
  console.log('Open add customer modal')
  // Implement add customer modal
}
</script>

<style scoped>
.customer-table-container {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  overflow: hidden;
  font-family: 'Segoe UI', system-ui, sans-serif;
}

.table-header {
  padding: 20px 24px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #f0f0f0;
}

.table-header h2 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #2d3748;
  margin: 0;
}

.table-controls {
  display: flex;
  align-items: center;
  gap: 16px;
}

.search-box {
  position: relative;
  display: flex;
  align-items: center;
}

.search-box i {
  position: absolute;
  left: 12px;
  color: #718096;
}

.search-box input {
  padding: 8px 12px 8px 36px;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 0.875rem;
  width: 240px;
  transition: all 0.2s;
}

.search-box input:focus {
  outline: none;
  border-color: #00aaff;
  box-shadow: 0 0 0 2px rgba(0, 170, 255, 0.2);
}

.btn-add {
  background: #00aaff;
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 8px;
  font-weight: 500;
  font-size: 0.875rem;
  display: flex;
  align-items: center;
  gap: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-add:hover {
  background: #0088cc;
  transform: translateY(-1px);
}

.table-responsive {
  overflow-x: auto;
}

.customer-table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
}

.customer-table thead th {
  background: #f8fafc;
  color: #4a5568;
  font-weight: 600;
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  padding: 12px 16px;
  border-bottom: 1px solid #e2e8f0;
  text-align: left;
}

.customer-table tbody tr {
  transition: background 0.2s;
}

.customer-table tbody tr:hover {
  background: #f8fafc;
}

.customer-table td {
  padding: 16px;
  border-bottom: 1px solid #f0f0f0;
  color: #4a5568;
  font-size: 0.875rem;
}

.customer-name {
  display: flex;
  align-items: center;
  gap: 12px;
}

.avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: #00aaff;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 500;
  font-size: 0.75rem;
}

.email-link,
.phone-link {
  color: #4a5568;
  text-decoration: none;
  transition: color 0.2s;
}

.email-link:hover {
  color: #00aaff;
  text-decoration: underline;
}

.phone-link:hover {
  color: #00aaff;
}

.action-buttons {
  display: flex;
  gap: 8px;
  justify-content: center;
}

.btn-action {
  width: 32px;
  height: 32px;
  border-radius: 6px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-edit {
  background: #e6f7ff;
  color: #00aaff;
}

.btn-edit:hover {
  background: #00aaff;
  color: white;
}

.btn-delete {
  background: #fff2f0;
  color: #ff4d4f;
}

.btn-delete:hover {
  background: #ff4d4f;
  color: white;
}

.btn-view {
  background: #f6ffed;
  color: #52c41a;
}

.btn-view:hover {
  background: #52c41a;
  color: white;
}

.no-results {
  text-align: center;
  padding: 24px;
  color: #718096;
  font-style: italic;
}

.table-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 24px;
  border-top: 1px solid #f0f0f0;
}

.pagination-info {
  color: #718096;
  font-size: 0.875rem;
}

.pagination-controls {
  display: flex;
  align-items: center;
  gap: 12px;
}

.btn-pagination {
  width: 32px;
  height: 32px;
  border-radius: 6px;
  border: 1px solid #e2e8f0;
  background: white;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.2s;
}

.btn-pagination:hover {
  border-color: #00aaff;
  color: #00aaff;
}

.btn-pagination:disabled {
  opacity: 0.5;
  cursor: not-allowed;
  border-color: #e2e8f0;
  color: inherit;
}

.page-indicator {
  font-size: 0.875rem;
  color: #4a5568;
}
</style>