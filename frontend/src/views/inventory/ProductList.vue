<!-- src/views/Products/ProductList.vue -->
<template>
  <div class="container-fluid p-2">
    <div class="d-flex justify-content-between align-items-center mb-4">
      <h1 class="h2 mb-0">Product List</h1>
      <button @click="addNewProduct" class="btn btn-primary" type="button">
        <i class="fas fa-plus me-2"></i>Add Product
      </button>
    </div>

    <!-- loading State -->
    <div v-if="store.loading" class="text-center py-5">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
      <p class="mt-2 text-muted">Loading products...</p>
    </div>

    <div v-else class="table-responsive">
      <table class="table table-striped table-hover">
        <thead class="table-dark">
          <tr>
            <th scope="col">Sku</th>
            <th scope="col">Name</th>
            <th scope="col">Description</th>
            <th scope="col">Category</th>
            <th scope="col">Standard Cost</th>
            <th scope="col">Selling Price</th>
            <th scope="col">Status</th>
            <th scope="col">Created At</th>
            <th scope="col">Updated At</th>
            <th class="text-center">Actions</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(product, index) in displayProducts" :key="product.id || `new-${index}`"
            :class="{ 'table-warning': product.isEditing || product.isNew }">

            <!-- SKU Field -->
            <td>
              <span v-if="!product.isEditing && !product.isNew">{{ product.sku || '-' }}</span>
              <input v-else v-model="product.sku" type="text" class="form-control form-control-sm" placeholder="SKU" />
            </td>

            <!-- Name Field -->
            <td>
              <input v-if="product.isEditing || product.isNew" v-model="product.name" type="text"
                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.name`] }"
                placeholder="Product name" @blur="validateField(index, 'name')" />
              <div v-if="errors[`${index}.name`]" class="invalid-feedback">
                {{ errors[`${index}.name`] }}
              </div>
              <span v-else class="fw-semibold">{{ product.name }}</span>
            </td>

            <!-- Description Field -->
            <td>
              <textarea v-if="product.isEditing || product.isNew" v-model="product.description"
                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.description`] }"
                placeholder="Description" @blur="validateField(index, 'description')"></textarea>
              <div v-if="errors[`${index}.description`]" class="invalid-feedback">
                {{ errors[`${index}.description`] }}
              </div>
              <span v-else>{{ product.description || '-' }}</span>
            </td>

            <!-- Category Field -->
            <td>
              <input v-if="product.isEditing || product.isNew" v-model="product.category" type="text"
                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.category`] }"
                placeholder="Category" @blur="validateField(index, 'category')" />
              <div v-if="errors[`${index}.category`]" class="invalid-feedback">
                {{ errors[`${index}.category`] }}
              </div>
              <span v-else>{{ product.category || '-' }}</span>
            </td>

            <!-- Standard Cost Field -->
            <td>
              <input v-if="product.isEditing || product.isNew" v-model.number="product.standard_cost" type="number"
                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.standard_cost`] }"
                placeholder="0.00" min="0" step="0.01" @blur="validateField(index, 'standard_cost')" />
              <div v-if="errors[`${index}.standard_cost`]" class="invalid-feedback">
                {{ errors[`${index}.standard_cost`] }}
              </div>
              <span v-else>{{ product.standard_cost ? formatCurrency(product.standard_cost) : '-' }}</span>
            </td>

            <!-- Selling Price Field -->
            <td>
              <input v-if="product.isEditing || product.isNew" v-model.number="product.selling_price" type="number"
                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.selling_price`] }"
                placeholder="0.00" min="0" step="0.01" @blur="validateField(index, 'selling_price')" />
              <div v-if="errors[`${index}.selling_price`]" class="invalid-feedback">
                {{ errors[`${index}.selling_price`] }}
              </div>
              <span v-else>{{ product.selling_price ? formatCurrency(product.selling_price) : '-' }}</span>
            </td>

            <!-- Status Field -->
            <td>
              <select v-if="product.isEditing || product.isNew" v-model="product.is_active"
                class="form-select form-select-sm">
                <option :value="true">Active</option>
                <option :value="false">Inactive</option>
              </select>
              <span v-else :class="product.is_active ? 'text-success' : 'text-danger'">
                {{ product.is_active ? 'Active' : 'Inactive' }}
              </span>
            </td>

            <!-- Created At -->
            <td>
              <span v-if="product.isNew" class="text-muted">-</span>
              <span v-else>{{ formatDate(product.created_at) }}</span>
            </td>

            <!-- Updated At -->
            <td>
              <span v-if="product.isNew" class="text-muted">-</span>
              <span v-else>{{ formatDate(product.updated_at) }}</span>
            </td>

            <!-- Actions -->
            <td class="text-center">
              <div v-if="product.isEditing || product.isNew" class="btn-group" role="group">
                <button @click="handleSave(product, index)" class="btn btn-success btn-sm" :disabled="isSaving"
                  title="Save Product">
                  <i class="bi bi-check-lg"></i>
                </button>
                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                  <i class="bi bi-x-lg"></i>
                </button>
              </div>
              <div v-else class="btn-group" role="group">
                <button @click="editProduct(index)" class="btn btn-outline-primary btn-sm me-2" title="Edit Product">
                  <i class="bi bi-pencil"></i>
                </button>
                <button @click="deleteProduct(product.id, index)" class="btn btn-outline-danger btn-sm" title="Delete">
                  <i class="bi bi-trash"></i>
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>

      <!-- Empty State -->
      <div v-if="store.products.length === 0 && displayProducts.length === 0" class="text-center py-5">
        <div class="mb-3">
          <i class="fas fa-boxes fa-3x text-muted"></i>
        </div>
        <h5 class="text-muted">No Products found</h5>
        <p class="text-muted">Start by adding your first Product</p>
        <button @click="addNewProduct" class="btn btn-primary">
          <i class="fas fa-plus me-2"></i>Add Product
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useProductStore } from '@/stores/inventory/productStore'

const store = useProductStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

const displayProducts = computed(() => {
  return store.products.map(product => ({
    ...product,
    isEditing: product.isEditing || false,
    isNew: product.isNew || false
  }))
})

onMounted(() => {
  store.fetchProducts()
})

const addNewProduct = () => {
  const newProduct = {
    id: null,
    sku: '',
    name: '',
    description: '',
    category: '',
    standard_cost: 0,
    selling_price: 0,
    is_active: true,
    created_at: null,
    updated_at: null,
    isNew: true,
    isEditing: true
  }
  store.products.unshift(newProduct)
}

const editProduct = (index) => {
  originalData.value[index] = { ...store.products[index] }
  store.products[index].isEditing = true
}

const cancelEdit = (index) => {
  const product = store.products[index]
  if (product.isNew) {
    store.products.splice(index, 1)
  } else {
    if (originalData.value[index]) {
      Object.assign(store.products[index], originalData.value[index])
      delete originalData.value[index]
    }
    store.products[index].isEditing = false
  }
  clearRowErrors(index)
}

const handleSave = async (product, index) => {
  try {
    isSaving.value = true
    clearRowErrors(index)

    if (!validateProduct(product, index)) {
      isSaving.value = false
      return
    }

    const productData = {
      sku: product.sku.trim(),
      name: product.name.trim(),
      description: product.description?.trim() || '',
      category: String(product.category).trim(),
      standard_cost: parseFloat(product.standard_cost),
      selling_price: parseFloat(product.selling_price),
      is_active: product.is_active
    }

    if (product.isNew) {
      await store.addProduct(productData)
      store.products.splice(index, 1)
      await store.fetchProducts()
    } else {
      await store.updateProduct(product.id, productData)
      store.products[index].isEditing = false
      delete originalData.value[index]
    }

    console.log(`Product ${product.isNew ? 'created' : 'updated'} successfully!`)
  } catch (error) {
    console.error('Error saving product:', error)
    if (error.response?.status === 400 && error.response.data) {
      handleBackendErrors(error.response.data, index)
    } else {
      alert('Failed to save product. Please try again.')
    }
  } finally {
    isSaving.value = false
  }
}

const validateProduct = (product, index) => {
  let isValid = true
  errors.value = {}

  if (!product.sku?.trim()) {
    errors.value[`${index}.sku`] = 'SKU is required'
    isValid = false
  }

  if (!product.name?.trim()) {
    errors.value[`${index}.name`] = 'Product name is required'
    isValid = false
  } else if (product.name.length > 100) {
    errors.value[`${index}.name`] = 'Name must be less than 100 characters'
    isValid = false
  }

  if (product.description && product.description.length > 500) {
    errors.value[`${index}.description`] = 'Description must be less than 500 characters'
    isValid = false
  }
  if (!product.category || String(product.category).trim() === '') {
    errors.value[`${index}.category`] = 'Category is required'
    isValid = false
  }

  if (isNaN(product.standard_cost)) {
    errors.value[`${index}.standard_cost`] = 'Standard cost must be a number'
    isValid = false
  } else if (product.standard_cost < 0) {
    errors.value[`${index}.standard_cost`] = 'Standard cost cannot be negative'
    isValid = false
  }

  if (isNaN(product.selling_price)) {
    errors.value[`${index}.selling_price`] = 'Selling price must be a number'
    isValid = false
  } else if (product.selling_price < 0) {
    errors.value[`${index}.selling_price`] = 'Selling price cannot be negative'
    isValid = false
  }

  return isValid
}

const validateField = (index, field) => {
  const product = store.products[index]
  const errorKey = `${index}.${field}`
  delete errors.value[errorKey]

  switch (field) {
    case 'sku':
      if (!product.sku?.trim()) {
        errors.value[errorKey] = 'SKU is required'
      }
      break
    case 'name':
      if (!product.name?.trim()) {
        errors.value[errorKey] = 'Product name is required'
      } else if (product.name.length > 100) {
        errors.value[errorKey] = 'Name must be less than 100 characters'
      }
      break
    case 'description':
      if (product.description && product.description.length > 500) {
        errors.value[errorKey] = 'Description must be less than 500 characters'
      }
      break
    case 'category':
      if (!product.category?.trim()) {
        errors.value[errorKey] = 'Category is required'
      }
      break
    case 'standard_cost':
      if (isNaN(product.standard_cost)) {
        errors.value[errorKey] = 'Standard cost must be a number'
      } else if (product.standard_cost < 0) {
        errors.value[errorKey] = 'Standard cost cannot be negative'
      }
      break
    case 'selling_price':
      if (isNaN(product.selling_price)) {
        errors.value[errorKey] = 'Selling price must be a number'
      } else if (product.selling_price < 0) {
        errors.value[errorKey] = 'Selling price cannot be negative'
      }
      break
  }
}

const handleBackendErrors = (backendErrors, index) => {
  Object.keys(backendErrors).forEach(field => {
    const errorKey = `${index}.${field}`
    errors.value[errorKey] = Array.isArray(backendErrors[field])
      ? backendErrors[field][0]
      : backendErrors[field]
  })
}

const clearRowErrors = (index) => {
  Object.keys(errors.value).forEach(key => {
    if (key.startsWith(`${index}.`)) {
      delete errors.value[key]
    }
  })
}

const deleteProduct = async (id, index) => {
  if (confirm('Are you sure you want to delete this product? This action cannot be undone.')) {
    try {
      await store.removeProduct(id)
    } catch (error) {
      console.error('Error deleting product:', error)
      alert('Failed to delete product. Please try again.')
    }
  }
}

const formatDate = (dateString) => {
  if (!dateString) return '-'
  return new Date(dateString).toLocaleDateString()
}

const formatCurrency = (value) => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
  }).format(value)
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

.table-warning {
  background-color: #fff3cd !important;
}

.form-control-sm,
.form-select-sm {
  min-width: 120px;
}

textarea.form-control-sm {
  min-width: 150px;
  resize: vertical;
}

.invalid-feedback {
  display: block;
  font-size: 0.75rem;
}

@media (max-width: 768px) {
  .table-responsive {
    font-size: 0.875rem;
  }

  .btn-sm {
    padding: 0.25rem 0.5rem;
    font-size: 0.75rem;
  }

  .form-control-sm,
  .form-select-sm {
    min-width: 100px;
  }
}
</style>