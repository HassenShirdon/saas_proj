<!-- src/views/Products/ProductList.vue -->
<template>
  <div class="inventory-table-container">
    <div class="table-header d-flex justify-content-between align-items-center mb-3">
      <h2 class="table-title">All Product List</h2>
      <button class="btn btn-primary add-btn" @click="isEdit = false; selectedroduct = null;">
        <i class="bi bi-plus-lg"></i> Add Product
      </button>
    </div>
    <div class="table-responsive modern-table">
      <table class="table table-striped table-hover">
        <thead class="table-dark">
          <tr>
            <th>Sku</th>
            <th>Name</th>
            <th>Description</th>
            <th>Unit Cost</th>
            <th>Selling Price</th>
            <th>Current Stock</th>
            <th>Reorder Level</th>
            <th>Last Updated</th>
            <th class="text-center">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="product in store.products" :key="product.sku">
            <td>{{ product.sku }}</td>
            <td class="fw-semibold">{{ product.name }}</td>

            <td>
              <span v-if="product.description" class="desc-truncate" :title="product.description">
                {{ product.description }}
              </span>
              <span v-else class="text-muted">-</span>
            </td>
            <td>
              <span v-if="product.unit_cost">${{ product.unit_cost }}</span>
              <span v-else class="text-muted">-</span>
            </td>
            <td>
              <span v-if="product.selling_price">${{ product.selling_price }}</span>
              <span v-else class="text-muted">-</span>
            </td>
            <td>
              <span v-if="product.current_stock !== null && product.current_stock !== undefined">
                {{ product.current_stock }}
              </span>
              <span v-else class="text-muted">-</span>
            </td>
            <td>
              <span v-if="product.current_stock !== null && product.current_stock !== undefined">
                {{ product.reorder_level }}
              </span>
              <span v-else class="text-muted">-</span>
            </td>
            <td>
              <span v-if="product.current_stock !== null && product.current_stock !== undefined">
                {{ product.last_updated ? new Date(product.last_updated).toLocaleDateString() : '-' }}
              </span>
              <span v-else class="text-muted">-</span>
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
          <tr v-if="store.products.length === 0">
            <td colspan="8" class="text-center text-muted py-4">No Products found.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useProductStore } from '@/stores/inventory/productStore'
import ProductForm from '@/components/inventory_modals/productModal.vue'

const store = useProductStore()
const selectedproduct = ref(null)

const products = store.products
const loading = store.loading

onMounted(() => {
  store.fetchProducts()
})

const handleCreate = async (productData) => {
  await store.addProduct(productData)
}

const handleUpdate = async (productData) => {
  await store.updateProduct(selectedproduct.value.id, productData)
  selectedproduct.value = null
}

const edit = (product) => {
  selectedproduct.value = { ...product }
}

const remove = async (id) => {
  if (confirm('Delete this product?')) {
    await store.removeProduct(id)
  }
}
</script>
