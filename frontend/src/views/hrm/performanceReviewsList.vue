<!-- src/views/PerformanceReviews/performanceReviewsList.vue -->
<template>
    <div class="container-fluid p-2">
        <div class="container d-flex justify-content-between align-items-center p-4 mb-4 shadow-sm">
            <h1 class="h2 mb-0">Performance Review List</h1>
            <button @click="addNewReview" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i>Add Review
            </button>
        </div>

        <!-- Loading State -->
        <div v-if="store.loading" class="text-center py-5">
            <div class="spinner-border text-primary" role="status">
                <span class="visually-hidden">Loading...</span>
            </div>
            <p class="mt-2 text-muted">Loading reviews...</p>
        </div>

        <!-- Performance Reviews Table -->
        <div v-else class="table-responsive">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th scope="col">#</th>
                        <th scope="col">Employee Name</th>
                        <th scope="col">Review Date</th>
                        <th scope="col">Reviewer</th>
                        <th scope="col">Comments</th>
                        <th scope="col">Rating</th>
                        <th scope="col">Created At</th>
                        <th scope="col">Updated At</th>
                        <th scope="col" class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="(review, index) in displayReviews" :key="review.id || `new-${index}`"
                        :class="{ 'table-warning': review.isEditing || review.isNew }">
                        <th scope="row">{{ review.isNew ? 'NEW' : index + 1 }}</th>

                        <!-- Employee Name Field -->
                        <td>
                            <input v-if="review.isEditing || review.isNew" v-model="review.employee" type="text"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.employee`] }" placeholder="Employee name"
                                @blur="validateField(index, 'employee')" />
                            <div v-if="errors[`${index}.employee`]" class="invalid-feedback">
                                {{ errors[`${index}.employee`] }}
                            </div>
                            <span v-else class="fw-semibold">{{ review.employee || '-' }}</span>
                        </td>

                        <!-- Review Date Field -->
                        <td>
                            <input v-if="review.isEditing || review.isNew" v-model="review.review_date" type="date"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.review_date`] }"
                                @blur="validateField(index, 'review_date')" />
                            <div v-if="errors[`${index}.review_date`]" class="invalid-feedback">
                                {{ errors[`${index}.review_date`] }}
                            </div>
                            <span v-else>{{ review.review_date || '-' }}</span>
                        </td>

                        <!-- Reviewer Field -->
                        <td>
                            <input v-if="review.isEditing || review.isNew" v-model="review.reviewer" type="text"
                                class="form-control form-control-sm" placeholder="Reviewer name" />
                            <span v-else>{{ review.reviewer || '-' }}</span>
                        </td>

                        <!-- Comments Field -->
                        <td>
                            <textarea v-if="review.isEditing || review.isNew" v-model="review.comments"
                                class="form-control form-control-sm" rows="2" placeholder="Comments"></textarea>
                            <span v-else-if="review.comments" class="d-inline-block text-truncate"
                                style="max-width: 200px;" :title="review.comments">
                                {{ review.comments }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>

                        <!-- Rating Field -->
                        <td>
                            <input v-if="review.isEditing || review.isNew" v-model="review.rating" type="number"
                                class="form-control form-control-sm"
                                :class="{ 'is-invalid': errors[`${index}.rating`] }" placeholder="Rating (1-5)" min="1"
                                max="5" @blur="validateField(index, 'rating')" />
                            <div v-if="errors[`${index}.rating`]" class="invalid-feedback">
                                {{ errors[`${index}.rating`] }}
                            </div>
                            <span v-else>{{ review.rating || '-' }}</span>
                        </td>

                        <!-- Created At -->
                        <td>
                            <span v-if="review.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(review.created_at) }}</span>
                        </td>

                        <!-- Updated At -->
                        <td>
                            <span v-if="review.isNew" class="text-muted">-</span>
                            <span v-else>{{ formatDate(review.updated_at) }}</span>
                        </td>

                        <!-- Actions -->
                        <td class="text-center">
                            <div v-if="review.isEditing || review.isNew" class="btn-group" role="group">
                                <button @click="handleSave(review, index)" class="btn btn-success btn-sm"
                                    :disabled="isSaving" title="Save Review">
                                    <i class="bi bi-check-lg"></i>
                                </button>
                                <button @click="cancelEdit(index)" class="btn btn-secondary btn-sm" title="Cancel">
                                    <i class="bi bi-x-lg"></i>
                                </button>
                            </div>
                            <div v-else class="btn-group" role="group">
                                <button @click="editReview(index)" class="btn btn-outline-primary btn-sm me-2"
                                    title="Edit Review">
                                    <i class="bi bi-pencil"></i>
                                </button>
                                <button @click="deleteReview(review.id, index)" class="btn btn-outline-danger btn-sm"
                                    title="Delete">
                                    <i class="bi bi-trash"></i>
                                </button>
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <!-- Empty State -->
            <div v-if="store.reviews.length === 0 && displayReviews.length === 0" class="text-center py-5">
                <div class="mb-3">
                    <i class="fas fa-users fa-3x text-muted"></i>
                </div>
                <h5 class="text-muted">No reviews found</h5>
                <p class="text-muted">Start by adding your first review</p>
                <button @click="addNewReview" class="btn btn-primary">
                    <i class="fas fa-plus me-2"></i>Add Review
                </button>
            </div>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref, computed } from 'vue'
import { usePerformanceReviewsStore } from '@/stores/hrm/performanceReviewsStore'

const store = usePerformanceReviewsStore()
const errors = ref({})
const isSaving = ref(false)
const originalData = ref({})

// Create a computed property that combines store reviews with any new/editing reviews
const displayReviews = computed(() => {
    return store.reviews.map(review => ({
        ...review,
        isEditing: review.isEditing || false,
        isNew: review.isNew || false
    }))
})

onMounted(async () => {
    await store.fetchReviews()
})

const addNewReview = () => {
    const newReview = {
        id: null,
        employee: '',
        review_date: '',
        reviewer: '',
        comments: '',
        rating: '',
        created_at: null,
        updated_at: null,
        isNew: true,
        isEditing: true
    }

    // Add to the beginning of the store's reviews array
    store.reviews.unshift(newReview)
}

const editReview = (index) => {
    // Store original data for cancel functionality
    originalData.value[index] = { ...store.reviews[index] }

    // Set editing mode
    store.reviews[index].isEditing = true
}

const cancelEdit = (index) => {
    const review = store.reviews[index]

    if (review.isNew) {
        // Remove new review
        store.reviews.splice(index, 1)
    } else {
        // Restore original data
        if (originalData.value[index]) {
            Object.assign(store.reviews[index], originalData.value[index])
            delete originalData.value[index]
        }
        store.reviews[index].isEditing = false
    }

    // Clear errors for this row
    clearRowErrors(index)
}

const handleSave = async (review, index) => {
    try {
        isSaving.value = true

        // Clear previous errors
        clearRowErrors(index)

        // Validate the review data
        if (!validateReview(review, index)) {
            isSaving.value = false
            return
        }

        // Prepare review data
        const reviewData = {
            employee: review.employee.trim(),
            review_date: review.review_date,
            reviewer: review.reviewer?.trim() || '',
            comments: review.comments?.trim() || '',
            rating: review.rating
        }

        if (review.isNew) {
            // Create new review
            await store.addReview(reviewData)
            // Remove the temporary review and refresh the list
            store.reviews.splice(index, 1)
            await store.fetchReviews()
        } else {
            // Update existing review
            await store.updateReview(review.id, reviewData)
            // Exit editing mode
            store.reviews[index].isEditing = false
            delete originalData.value[index]
        }

        // Show success message
        console.log(`Review ${review.isNew ? 'created' : 'updated'} successfully!`)

    } catch (error) {
        console.error('Error saving review:', error)

        // Handle validation errors from backend
        if (error.response?.status === 400 && error.response.data) {
            handleBackendErrors(error.response.data, index)
        } else {
            // Show error message
            alert('Failed to save review. Please try again.')
        }
    } finally {
        isSaving.value = false
    }
}

const validateReview = (review, index) => {
    let isValid = true

    // Required field validation
    if (!review.employee?.trim()) {
        errors.value[`${index}.employee`] = 'Employee name is required'
        isValid = false
    }

    if (!review.review_date) {
        errors.value[`${index}.review_date`] = 'Review date is required'
        isValid = false
    }

    if (review.rating && (review.rating < 1 || review.rating > 5)) {
        errors.value[`${index}.rating`] = 'Rating must be between 1 and 5'
        isValid = false
    }

    return isValid
}

const validateField = (index, field) => {
    const review = store.reviews[index]
    const errorKey = `${index}.${field}`

    // Clear existing error
    delete errors.value[errorKey]

    // Validate specific field
    switch (field) {
        case 'employee':
            if (!review.employee?.trim()) {
                errors.value[errorKey] = 'Employee name is required'
            }
            break
        case 'review_date':
            if (!review.review_date) {
                errors.value[errorKey] = 'Review date is required'
            }
            break
        case 'rating':
            if (review.rating && (review.rating < 1 || review.rating > 5)) {
                errors.value[errorKey] = 'Rating must be between 1 and 5'
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

const deleteReview = async (id, index) => {
    if (confirm('Are you sure you want to delete this review? This action cannot be undone.')) {
        try {
            await store.deleteReview(id)
        } catch (error) {
            console.error('Error deleting review:', error)
            alert('Failed to delete review. Please try again.')
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