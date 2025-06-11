<template>
    <div class="container-fluid p-4">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Product Categories</h1>
            <button @click="openAddModal" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Category
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading categories...</p>
        </div>

        <!-- Table or Empty State -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-primary">
                    <tr>
                        <th scope="col">S.No</th>
                        <th scope="col">Name</th>
                        <th scope="col">Description</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(cat, idx) in store.productCategories" :key="cat.id">
                        <th scope="row">{{ idx + 1 }}</th>
                        <td class="fw-semibold">{{ cat.name }}</td>
                        <td>
                            <span v-if="cat.description" class="d-inline-block text-truncate" style="max-width: 200px;"
                                :title="cat.description">
                                {{ cat.description }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td class="text-center">
                            <div class="btn-group" role="group">

                                <button @click="openEditModal(cat)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteProductCategory(cat.id)" class="btn btn-outline-danger btn-sm"
                                    title="Delete">
                                    <i class="bi bi-trash"></i>
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
                <h5 class="text-muted">No categories found</h5>
                <p class="text-muted">Start by adding your first product category</p>
                <button @click="openAddModal" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Category
                </button>
            </div>
        </div>

        <!-- Modal -->
        <ProductCategoryModal :show="showModal" :productCategory="selectedProductCategory" :is-edit="isEdit"
            @close="closeModal" @save="handleSave" />
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useProductCategoryStore } from '@/stores/inventory/productCategoriesStore'
import ProductCategoryModal from '@/components/ProductCategory/ProductCategoryModal.vue'

const store = useProductCategoryStore()
const showModal = ref(false)
const selectedProductCategory = ref(null)
const isEdit = ref(false)

onMounted(async () => {
    await store.fetchProductCategories()
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
        // Handle error
    }
}

const deleteProductCategory = async (id) => {
    if (confirm('Are you sure you want to delete this category? This action cannot be undone.')) {
        try {
            await store.removeproductCategory(id)
        } catch (error) {
            // Handle error
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
