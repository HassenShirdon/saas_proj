<!-- src/components/inventory/ProductCategoryModal.vue -->
<template>
    <div class="modal fade" :class="{ show: show }" :style="{ display: show ? 'block' : 'none' }" tabindex="-1"
        role="dialog" aria-labelledby="productCategoryModalLabel" :aria-hidden="!show">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="productCategoryModalLabel">
                        {{ isEdit ? 'Edit Product Category' : 'Add New Product Category' }}
                    </h5>
                    <button type="button" class="btn-close" @click="closeModal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <form @submit.prevent="submitForm">
                        <div class="row">
                            <!-- Name Field -->
                            <div class="col-md-12 mb-3">
                                <label for="categoryName" class="form-label">
                                    Category Name <span class="text-danger">*</span>
                                </label>
                                <input 
                                    type="text" 
                                    class="form-control" 
                                    :class="{ 'is-invalid': errors.Name }"
                                    id="categoryName" 
                                    v-model="form.Name" 
                                    placeholder="Enter category name"
                                    required
                                >
                                <div v-if="errors.Name" class="invalid-feedback">
                                    {{ errors.Name }}
                                </div>
                            </div>

                            <!-- Description Field -->
                            <div class="col-md-12 mb-3">
                                <label for="categoryDescription" class="form-label">
                                    Description
                                </label>
                                <textarea 
                                    class="form-control" 
                                    :class="{ 'is-invalid': errors.Description }"
                                    id="categoryDescription" 
                                    v-model="form.Description" 
                                    placeholder="Enter category description (optional)"
                                    rows="4"
                                ></textarea>
                                <div v-if="errors.Description" class="invalid-feedback">
                                    {{ errors.Description }}
                                </div>
                                <div class="form-text">
                                    Provide a brief description of what products belong to this category.
                                </div>
                            </div>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" @click="closeModal">
                        <i class="fas fa-times me-2"></i>Cancel
                    </button>
                    <button type="button" class="btn btn-primary" @click="submitForm" :disabled="loading">
                        <span v-if="loading" class="spinner-border spinner-border-sm me-2" role="status"></span>
                        <i v-else class="fas fa-save me-2"></i>
                        {{ isEdit ? 'Update Category' : 'Add Category' }}
                    </button>
                </div>
            </div>
        </div>
    </div>
    
    <!-- Modal Backdrop -->
    <div v-if="show" class="modal-backdrop fade show" @click="closeModal"></div>
</template>

<script setup>
import { ref, watch, computed } from 'vue'

// Props
const props = defineProps({
    show: {
        type: Boolean,
        default: false
    },
    productCategory: {
        type: Object,
        default: null
    },
    isEdit: {
        type: Boolean,
        default: false
    }
})

// Emits
const emit = defineEmits(['close', 'save'])

// Reactive data
const form = ref({
    Name: '',
    Description: ''
})

const errors = ref({
    Name: '',
    Description: ''
})

const loading = ref(false)

// Methods (defined first to avoid hoisting issues)
const resetForm = () => {
    form.value = {
        Name: '',
        Description: ''
    }
    clearErrors()
}

const clearErrors = () => {
    errors.value = {
        Name: '',
        Description: ''
    }
}

// Computed
const isFormValid = computed(() => {
    return form.value.Name.trim().length > 0
})

// Watch for prop changes to populate form
watch(() => props.productCategory, (newCategory) => {
    if (newCategory) {
        form.value = {
            Name: newCategory.Name || '',
            Description: newCategory.Description || ''
        }
    } else {
        resetForm()
    }
}, { immediate: true })

// Watch for modal show/hide to reset form
watch(() => props.show, (isShown) => {
    if (isShown) {
        // Clear errors when modal opens
        clearErrors()
        // Focus on first input after modal is shown
        setTimeout(() => {
            const firstInput = document.getElementById('categoryName')
            if (firstInput) {
                firstInput.focus()
            }
        }, 100)
    } else {
        // Reset form when modal closes
        if (!props.isEdit) {
            resetForm()
        }
    }
})

const validateForm = () => {
    clearErrors()
    let isValid = true

    // Validate Name
    if (!form.value.Name || form.value.Name.trim().length === 0) {
        errors.value.Name = 'Category name is required'
        isValid = false
    } else if (form.value.Name.trim().length < 2) {
        errors.value.Name = 'Category name must be at least 2 characters long'
        isValid = false
    } else if (form.value.Name.trim().length > 100) {
        errors.value.Name = 'Category name must not exceed 100 characters'
        isValid = false
    }

    // Validate Description (optional but if provided, check length)
    if (form.value.Description && form.value.Description.trim().length > 500) {
        errors.value.Description = 'Description must not exceed 500 characters'
        isValid = false
    }

    return isValid
}

const submitForm = async () => {
    if (!validateForm()) {
        return
    }

    loading.value = true
    
    try {
        // Prepare data for submission
        const categoryData = {
            Name: form.value.Name.trim(),
            Description: form.value.Description.trim() || null
        }

        // Emit save event with form data
        emit('save', categoryData)
        
    } catch (error) {
        console.error('Error submitting form:', error)
        // Handle any submission errors here
    } finally {
        loading.value = false
    }
}

const closeModal = () => {
    if (!loading.value) {
        emit('close')
    }
}

// Handle Escape key to close modal
const handleKeydown = (event) => {
    if (event.key === 'Escape' && props.show && !loading.value) {
        closeModal()
    }
}

// Add event listener for Escape key
document.addEventListener('keydown', handleKeydown)
</script>

<style scoped>
.modal {
    background-color: rgba(0, 0, 0, 0.5);
}

.modal.show {
    display: block !important;
}

.modal-backdrop {
    position: fixed;
    top: 0;
    left: 0;
    z-index: 1040;
    width: 100vw;
    height: 100vh;
    background-color: #000;
    opacity: 0.5;
}

.modal-dialog {
    position: relative;
    width: auto;
    margin: 1.75rem auto;
    pointer-events: none;
    z-index: 1050;
}

.modal-content {
    position: relative;
    display: flex;
    flex-direction: column;
    width: 100%;
    pointer-events: auto;
    background-color: #fff;
    background-clip: padding-box;
    border: 1px solid rgba(0, 0, 0, 0.2);
    border-radius: 0.5rem;
    box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.075);
}

.modal-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1rem 1rem;
    border-bottom: 1px solid #dee2e6;
    border-top-left-radius: calc(0.5rem - 1px);
    border-top-right-radius: calc(0.5rem - 1px);
}

.modal-title {
    margin-bottom: 0;
    line-height: 1.5;
    font-weight: 500;
}

.modal-body {
    position: relative;
    flex: 1 1 auto;
    padding: 1rem;
}

.modal-footer {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding: 0.75rem;
    border-top: 1px solid #dee2e6;
    border-bottom-right-radius: calc(0.5rem - 1px);
    border-bottom-left-radius: calc(0.5rem - 1px);
    gap: 0.5rem;
}

.btn-close {
    box-sizing: content-box;
    width: 1em;
    height: 1em;
    padding: 0.25em 0.25em;
    color: #000;
    background: transparent url("data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16' fill='%23000'%3e%3cpath d='m.235.867l15.364 15.364-.707.707l-15.364-15.364z'/%3e%3cpath d='m15.598.933l.707.707l-15.364 15.364-.707-.707z'/%3e%3c/svg%3e") center/1em auto no-repeat;
    border: 0;
    border-radius: 0.375rem;
    opacity: 0.5;
    cursor: pointer;
}

.btn-close:hover {
    opacity: 0.75;
}

.form-label {
    margin-bottom: 0.5rem;
    font-weight: 500;
}

.text-danger {
    color: #dc3545 !important;
}

.is-invalid {
    border-color: #dc3545;
}

.invalid-feedback {
    width: 100%;
    margin-top: 0.25rem;
    font-size: 0.875em;
    color: #dc3545;
}

.form-text {
    margin-top: 0.25rem;
    font-size: 0.875em;
    color: #6c757d;
}

.spinner-border-sm {
    width: 1rem;
    height: 1rem;
}

@media (max-width: 576px) {
    .modal-dialog {
        margin: 1rem;
    }
    
    .modal-lg {
        max-width: none;
    }
}
</style>