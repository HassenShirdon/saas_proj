<template>
    <div class="modal fade" :class="{ show: show }" :style="{ display: show ? 'block' : 'none' }" tabindex="-1"
        role="dialog" @click.self="handleBackdropClick">
        <div class="modal-dialog modal-lg" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">
                        <i class="fas fa-user me-2"></i>
                        {{ isEdit ? 'Edit Supplier' : 'Add New Supplier' }}
                    </h5>
                    <button type="button" class="btn-close" @click="closeModal" aria-label="Close"></button>
                </div>

                <form @submit.prevent="handleSubmit">
                    <div class="modal-body">
                        <div class="row">
                            <!-- Supplier Name -->
                            <div class="col-md-6 mb-3">
                                <label for="supplierName" class="form-label">
                                    Supplier Name <span class="text-danger">*</span>
                                </label>
                                <input id="supplierName" v-model="form.name" type="text" class="form-control"
                                    :class="{ 'is-invalid': errors.name }" placeholder="Enter supplier name" required>
                                <div v-if="errors.name" class="invalid-feedback">
                                    {{ errors.name }}
                                </div>
                            </div>

                            <!-- Contact Person -->
                            <div class="col-md-6 mb-3">
                                <label for="contactPerson" class="form-label">Contact Person</label>
                                <input id="contactPerson" v-model="form.contact_person" type="text" class="form-control"
                                    :class="{ 'is-invalid': errors.contact_person }"
                                    placeholder="Enter contact person name">
                                <div v-if="errors.contact_person" class="invalid-feedback">
                                    {{ errors.contact_person }}
                                </div>
                            </div>

                            <!-- Email -->
                            <div class="col-md-6 mb-3">
                                <label for="email" class="form-label">Email Address</label>
                                <input id="email" v-model="form.email" type="email" class="form-control"
                                    :class="{ 'is-invalid': errors.email }" placeholder="Enter email address">
                                <div v-if="errors.email" class="invalid-feedback">
                                    {{ errors.email }}
                                </div>
                            </div>

                            <!-- Phone Number -->
                            <div class="col-md-6 mb-3">
                                <label for="phoneNumber" class="form-label">Phone Number</label>
                                <input id="phoneNumber" v-model="form.phone_number" type="tel" class="form-control"
                                    :class="{ 'is-invalid': errors.phone_number }" placeholder="Enter phone number">
                                <div v-if="errors.phone_number" class="invalid-feedback">
                                    {{ errors.phone_number }}
                                </div>
                            </div>

                            <!-- Address -->
                            <div class="col-12 mb-3">
                                <label for="address" class="form-label">Address</label>
                                <textarea id="address" v-model="form.address" class="form-control"
                                    :class="{ 'is-invalid': errors.address }" rows="3"
                                    placeholder="Enter full address"></textarea>
                                <div v-if="errors.address" class="invalid-feedback">
                                    {{ errors.address }}
                                </div>
                            </div>
                        </div>

                        <!-- API Error Display -->
                        <div v-if="apiError" class="alert alert-danger" role="alert">
                            <h6 class="alert-heading mb-2">
                                <i class="fas fa-exclamation-triangle me-2"></i>Error occurred:
                            </h6>
                            <p class="mb-0">{{ apiError }}</p>
                        </div>

                        <!-- Form Validation Summary -->
                        <div v-if="Object.keys(errors).length > 0" class="alert alert-danger" role="alert">
                            <h6 class="alert-heading mb-2">
                                <i class="fas fa-exclamation-triangle me-2"></i>Please fix the following errors:
                            </h6>
                            <ul class="mb-0">
                                <li v-for="(error, field) in errors" :key="field">{{ error }}</li>
                            </ul>
                        </div>

                        <!-- Success Message -->
                        <div v-if="successMessage" class="alert alert-success" role="alert">
                            <i class="fas fa-check-circle me-2"></i>{{ successMessage }}
                        </div>
                    </div>

                    <div class="modal-footer">
                        <button type="button" class="btn btn-secondary" @click="closeModal" :disabled="isSubmitting">
                            <i class="fas fa-times me-2"></i>Cancel
                        </button>
                        <button type="submit" class="btn btn-primary" :disabled="isSubmitting || !isFormValid">
                            <span v-if="isSubmitting" class="spinner-border spinner-border-sm me-2"
                                role="status"></span>
                            <i v-else class="fas fa-save me-2"></i>
                            {{ isSubmitting ? 'Saving...' : (isEdit ? 'Update Supplier' : 'Add Supplier') }}
                        </button>
                    </div>
                </form>
            </div>
        </div>
    </div>

    <!-- Modal Backdrop -->
    <div v-if="show" class="modal-backdrop fade show" @click="handleBackdropClick"></div>
</template>

<script setup>
import { ref, watch, computed, onUnmounted } from 'vue'
import { createSupplier, updateSupplier } from '@/api/inventory'

const props = defineProps({
    show: {
        type: Boolean,
        default: false
    },
    supplier: {
        type: Object,
        default: null
    },
    isEdit: {
        type: Boolean,
        default: false
    }
})

const emit = defineEmits(['close', 'save', 'supplier-saved'])

const form = ref({
    name: '',
    contact_person: '',
    email: '',
    phone_number: '',
    address: ''
})

const errors = ref({})
const isSubmitting = ref(false)
const apiError = ref('')
const successMessage = ref('')

// Computed property to check if form is valid
const isFormValid = computed(() => {
    return form.value.name.trim() !== '' && Object.keys(errors.value).length === 0
})

// Watch for prop changes to populate form
watch([() => props.show, () => props.supplier], () => {
    if (props.show) {
        resetForm()
        if (props.isEdit && props.supplier) {
            populateForm(props.supplier)
        }
        // Add modal-open class to body to prevent scrolling
        document.body.classList.add('modal-open')
    } else {
        // Remove modal-open class from body
        document.body.classList.remove('modal-open')
    }
}, { immediate: true })

const resetForm = () => {
    form.value = {
        name: '',
        contact_person: '',
        email: '',
        phone_number: '',
        address: ''
    }
    errors.value = {}
    isSubmitting.value = false
    apiError.value = ''
    successMessage.value = ''
}

const populateForm = (supplier) => {
    form.value = {
        name: supplier.name || '',
        contact_person: supplier.contact_person || '',
        email: supplier.email || '',
        phone_number: supplier.phone_number || '',
        address: supplier.address || ''
    }
}

const validateForm = () => {
    errors.value = {}

    // Required field validation
    if (!form.value.name.trim()) {
        errors.value.name = 'Supplier name is required'
    }

    // Email validation
    if (form.value.email && !isValidEmail(form.value.email)) {
        errors.value.email = 'Please enter a valid email address'
    }

    // Phone number validation (basic)
    if (form.value.phone_number && form.value.phone_number.length < 10) {
        errors.value.phone_number = 'Phone number should be at least 10 digits'
    }

    return Object.keys(errors.value).length === 0
}

const isValidEmail = (email) => {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
    return emailRegex.test(email)
}

const handleSubmit = async () => {
    if (!validateForm()) {
        return
    }

    isSubmitting.value = true
    apiError.value = ''
    successMessage.value = ''

    try {
        // Prepare data for submission
        const supplierData = {
            name: form.value.name.trim(),
            contact_person: form.value.contact_person.trim() || null,
            email: form.value.email.trim() || null,
            phone_number: form.value.phone_number.trim() || null,
            address: form.value.address.trim() || null
        }

        let response
        if (props.isEdit && props.supplier) {
            // Update existing supplier
            response = await updateSupplier(props.supplier.id, supplierData)
            successMessage.value = 'Supplier updated successfully!'
        } else {
            // Create new supplier
            response = await createSupplier(supplierData)
            successMessage.value = 'Supplier created successfully!'
        }

        // Emit success event to parent component
        emit('supplier-saved', response.data)
        emit('save', response.data)

        // Close modal after a short delay to show success message
        setTimeout(() => {
            closeModal()
        }, 1500)

    } catch (error) {
        console.error('Error saving supplier:', error)

        // Handle different types of errors
        if (error.response) {
            // Server responded with error status
            const status = error.response.status
            const data = error.response.data

            if (status === 400 && data) {
                // Validation errors from server
                if (typeof data === 'object') {
                    // Handle field-specific errors
                    Object.keys(data).forEach(field => {
                        if (Array.isArray(data[field])) {
                            errors.value[field] = data[field][0]
                        } else {
                            errors.value[field] = data[field]
                        }
                    })
                } else {
                    apiError.value = data.message || 'Validation error occurred'
                }
            } else if (status === 401) {
                apiError.value = 'Unauthorized. Please log in again.'
            } else if (status === 403) {
                apiError.value = 'You do not have permission to perform this action.'
            } else if (status === 500) {
                apiError.value = 'Server error. Please try again later.'
            } else {
                apiError.value = data.message || `Error: ${status}`
            }
        } else if (error.request) {
            // Network error
            apiError.value = 'Network error. Please check your connection and try again.'
        } else {
            // Other error
            apiError.value = 'An unexpected error occurred. Please try again.'
        }
    } finally {
        isSubmitting.value = false
    }
}

const closeModal = () => {
    if (!isSubmitting.value) {
        emit('close')
    }
}

const handleBackdropClick = () => {
    closeModal()
}

// Clean up when component is unmounted
const cleanup = () => {
    document.body.classList.remove('modal-open')
}

// Cleanup on unmount
onUnmounted(cleanup)
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
    z-index: 1050;
    margin: 1.75rem auto;
    max-width: 800px;
}

.modal-content {
    border: none;
    border-radius: 0.5rem;
    box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
}

.modal-header {
    background-color: #f8f9fa;
    border-bottom: 1px solid #dee2e6;
    border-radius: 0.5rem 0.5rem 0 0;
}

.modal-title {
    color: #495057;
    font-weight: 600;
}

.form-label {
    font-weight: 500;
    color: #495057;
}

.form-control:focus {
    border-color: #86b7fe;
    box-shadow: 0 0 0 0.25rem rgba(13, 110, 253, 0.25);
}

.is-invalid {
    border-color: #dc3545;
}

.invalid-feedback {
    display: block;
}

.alert {
    border: none;
    border-radius: 0.375rem;
}

.btn {
    border-radius: 0.375rem;
    font-weight: 500;
}

.btn:disabled {
    opacity: 0.65;
}

.spinner-border-sm {
    width: 1rem;
    height: 1rem;
}

/* Mobile responsiveness */
@media (max-width: 576px) {
    .modal-dialog {
        margin: 0.5rem;
        max-width: none;
    }

    .modal-lg {
        max-width: none;
    }
}

/* Prevent body scroll when modal is open */
:global(body.modal-open) {
    overflow: hidden;
}
</style>