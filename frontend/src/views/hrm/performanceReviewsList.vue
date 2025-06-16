<template>
    <div class="inventory-table-container">
        <div class="table-header d-flex justify-content-between align-items-center mb-4">
            <h2 class="table-title">Reviews List</h2>
            <button class="btn btn-primary add-btn" @click="isEdit = false; selectedperformance = null;">
                <i class="bi bi-plus-lg"></i> Add Reviews
            </button>
        </div>
        <div class="table-responsive modern-table">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>S.No </th>
                        <th>Employee Name</th>
                        <th>Review_date</th>
                        <th>Reviewd By</th>
                        <th>Comments</th>
                        <th>Rating</th>
                        <th class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="performance in performances" :key="performance.id">
                        <td>{{ performance.id }}</td>
                        <td class="fw-semibold">{{ performance.employee }}</td>
                        <td>{{ performance.reviewer || '-' }}</td>
                        <td>{{ performance.comments || '-' }}</td>
                        <td>{{ performance.rating || '-' }}</td>

                        <td class="text-center">
                            <button class="btn btn-outline-primary btn-sm me-2" title="Edit">
                                <i class="bi bi-pencil"></i>
                            </button>
                            <button class="btn btn-outline-danger btn-sm" title="Delete">
                                <i class="bi bi-trash"></i>
                            </button>
                        </td>
                    </tr>
                    <!-- <tr v-if="performances.length === 0">
                        <td colspan="8" class="text-center text-muted py-4">No performances found.</td>
                    </tr> -->
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
import { ref, onMounted } from 'vue'
import { usePerformanceReviewsStore } from '@/stores/hrm/performanceReviewsStore'
// stores/hrm/performanceReviewsStore'
const store = usePerformanceReviewsStore()
const performances = ref([])
const selectedPerformance = ref(null)
const isEdit = ref(false);

onMounted(async () => {
    await store.fetchReviews
    performances.value = store.Reviews
});

const handleAdd = () => {
    store.setSelectedPerformance(null)
    store.isEdit = false
};
</script>
<style></style>