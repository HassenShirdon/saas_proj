<!-- src/views/Products/ProductCategoryList.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0">Product Categories</h1>
            <button @click="addNewCategory" class="btn btn-primary" type="button">
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

        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">Name</th>
                        <th scope="col">Description</th>
                        <th scope="col">Created At</th>
                        <th scope="col">Updated At</th>
                        <th class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(category, index) in displayCategories" :key="category.id || `new-${index}`"
                        :class="{ 'table-warning': category.isEditing || category.isNew }">

                        <!-- Name Field -->
                        <td>
                            <input v-if="category.isEditing || category.isNew" v-model="category.name" type="text"
                                class="form-control form-control-sm" :class="{ 'is-invalid': errors[`${index}.name`] }"
                                placeholder="Category name" @blur="validateField(index, 'name')" />
                            <div v-if="errors[`${index}.name`]" class="invalid-feedback">
                                {{ errors[`${index}.name`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ category.name }}</span>
                        </td>

                        <!-- Description Field -->
                        <td>
                            <textarea v-if="category.isEditing || category.isNew" v-model="category.description"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.description`] }"
                                placeholder="Category description (optional)"
                                @blur="validateField(index, 'description')"></textarea>
                            <div v-if="errors[`${index}.description`]" class="invalid-feedback">
                                {{ errors[`${index}.description`] }}
                            </div>
                            <span v-else>{{ category.description || '-' }}</span>
                        </td>

                        <!-- Created At -->
                        <td>
                            <span v-if="category.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(category.created_at) }}</span>
                        </td>

                        <!-- Updated At -->
                        <td>
                            <span v-if="category.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(category.updated_at) }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="category.isEditing || category.isNew" class="btn-group" role="group">
                                <button @click="handleSave(category, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Category">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editCategory(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Category">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteCategory(category.id, index)"
                                    class="btn btn-outline-danger btn-sm" title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.productCategories.length === 0 && displayCategories.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-tags fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No Categories found</h5>
                <p class="text-muted">Start by adding your first Product Category</p>
                <button @click="addNewCategory" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Category
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { useProductCategoryStore } from '@/stores/inventory/productCategoriesStore'

const store = useProductCategoryStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

const displayCategories = computed(() => {
    return store.productCategories.map(category => ({
        ...category,
        isEditing: category.isEditing || false,
        isNew: category.isNew || false
    }))
})

onMounted(() => {
    store.fetchProductCategories()
})

const addNewCategory = () => {
    const newCategory = {
        id: null,
        name: '',
        description: '',
        created_at: null,
        updated_at: null,
        isNew: true,
        isEditing: true
    }
    store.productCategories.unshift(newCategory)
}

const editCategory = (index) => {
    originalData.value[index] = { ...store.productCategories[index] }
    store.productCategories[index].isEditing = true
}

const cancelEdit = (index) => {
    const category = store.productCategories[index]
    if (category.isNew) {
        store.productCategories.splice(index, 1)
    } else {
        if (originalData.value[index]) {
            Object.assign(store.productCategories[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.productCategories[index].isEditing = false
    }
    clearRowErrors(index)
}

const handleSave = async (category, index) => {
    try {
        isSaving.value = true
        clearRowErrors(index)

        if (!validateCategory(category, index)) {
            isSaving.value = false
            return
        }

        const categoryData = {
            name: category.name.trim(),
            description: category.description?.trim() || ''
        }

        if (category.isNew) {
            await store.addProductCategory(categoryData)
            store.productCategories.splice(index, 1)
            await store.fetchProductCategories()
        } else {
            await store.updateProductCategory(category.id, categoryData)
            store.productCategories[index].isEditing = false
            delete originalData.value[index]
        }

        console.log(`Category ${category.isNew ? 'created' : 'updated'} successfully!`)
    } catch (error) {
        console.error('Error saving category:', error)
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            alert('Failed to save category. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateCategory = (category, index) => {
    let isValid = true
    errors.value = {}

    if (!category.name?.trim()) {
        errors.value[`${index}.name`] = 'Category name is required'
        isValid = false
    } else if (category.name.length > 255) {
        errors.value[`${index}.name`] = 'Name must be less than 255 characters'
        isValid = false
    }

    if (category.description && category.description.length > 1000) {
        errors.value[`${index}.description`] = 'Description must be less than 1000 characters'
        isValid = false
    }

    return isValid
}

const validateField = (index, field) => {
    const category = store.productCategories[index]
    const errorKey = `${index}.${field}`
    delete errors.value[errorKey]

    switch (field) {
        case 'name':
            if (!category.name?.trim()) {
                errors.value[errorKey] = 'Category name is required'
            } else if (category.name.length > 255) {
                errors.value[errorKey] = 'Name must be less than 255 characters'
            }
            break
        case 'description':
            if (category.description && category.description.length > 1000) {
                errors.value[errorKey] = 'Description must be less than 1000 characters'
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

const deleteCategory = async (id, index) => {
    if (confirm('Are you sure you want to delete this category? This action cannot be undone.')) {
        try {
            await store.removeProductCategory(id)
        } catch (error) {
            console.error('Error deleting category:', error)
            alert('Failed to delete category. Please try again.')
        }
    }
}

const formatDate = (dateString) => {
    if (!dateString) return '-'
    return new Date(dateString).toLocaleDateString()
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
    min-width: 200px;
    resize: vertical;
    min-height: 60px;
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

    textarea.form-control-sm {
        min-width: 150px;
    }
}
</style>