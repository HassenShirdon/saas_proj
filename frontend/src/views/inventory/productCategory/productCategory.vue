<!-- src/views/ProductCategories/ProductCategoryList.vue -->
<template>
    <div class="container-fluid p-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Product Category List</h1>
            <button @click="openAddModal" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Product Category
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading Product Categories...</p>
        </div>

        <!-- Product Categories Table -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Name</th>
                        <th scope="col">Description</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(productCategory, index) in store.productCategories" :key="productCategory.id">
                        <th scope="row">{{ index + 1 }}</th>
                        <td class="fw-semibold">{{ productCategory.name }}</td>
                        <td>{{ productCategory.description || '-' }}</td>
                        <td class="text-center">
                            <div class="btn-group" role="group">
                                <button @click="openEditModal(productCategory)" class="btn btn-sm btn-outline-primary"
                                    type="button" title="Edit Product Category">
                                    <i class="fas fa-edit"></i>
                                </button>
                                <button @click="deleteProductCategory(productCategory.id)"
                                    class="btn btn-sm btn-outline-danger" type="button" title="Delete Product Category">
                                    <i class="fas fa-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.productCategories.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-tags fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No product categories found</h5>
                <p class="text-muted">Start by adding your first product category</p>
                <button @click="openAddModal" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Product Category
                </button>
            </div>
        </div>

        <!-- Product Category Modal Component -->
        <ProductCategoryModal :show="showModal" :productCategory="selectedProductCategory" :is-edit="isEdit"
            @close="closeModal" @save="handleSave" />

        <!-- Debug info (remove in production) -->
        <div class="mt-4 p-3 bg-light border rounded small" v-if="showDebug">
            <h6 class="mb-2">Debug Info:</h6>
            <p class="mb-1">Loading: {{ store.loading }}</p>
            <p class="mb-1">Product Categories count: {{ store.productCategories.length }}</p>
            <details>
                <summary class="text-primary" style="cursor: pointer;">View Product Categories Data</summary>
                <pre
                    class="mt-2 bg-white p-2 border rounded">{{ JSON.stringify(store.productCategories, null, 2) }}</pre>
            </details>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useProductCategoryStore } from '@/stores/inventory/productCategoriesStore'
import ProductCategoryModal from '@/components/ProductCategory/ProductCategoryModal.vue'

const store = useProductCategoryStore()
const showModal = ref(false)
const selectedProductCategory = ref(null) // Fixed: consistent naming
const isEdit = ref(false)
const showDebug = ref(false) // Set to true for debugging

onMounted(async () => {
    console.log('Component mounted, fetching Product Categories...')
    await store.fetchProductCategories() // Fixed: correct method name
    console.log('Product Categories fetched:', store.productCategories)
})

const openAddModal = () => {
    selectedProductCategory.value = null
    isEdit.value = false
    showModal.value = true
}

const openEditModal = (productCategory) => {
    selectedProductCategory.value = { ...productCategory }
    isEdit.value = true
    showModal.value = true
}

const closeModal = () => {
    showModal.value = false
    selectedProductCategory.value = null
    isEdit.value = false
}

const handleSave = async (productCategoryData) => {
    try {
        if (isEdit.value) {
            await store.updateproductCategory(selectedProductCategory.value.id, productCategoryData)
        } else {
            await store.addproductCategory(productCategoryData)
        }
        closeModal()
    } catch (error) {
        console.error('Error saving product category:', error)
        // You might want to show an error message to the user here
    }
}

const deleteProductCategory = async (id) => {
    if (confirm('Are you sure you want to delete this product category? This action cannot be undone.')) {
        try {
            await store.removeproductCategory(id)
        } catch (error) {
            console.error('Error deleting product category:', error)
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