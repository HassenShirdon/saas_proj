<template>
    <div class="container">
        <div class="d-flex justify-content-between align-items-center mb-4">
            <h1 class="h2 mb-0 fw-14">Stock Movement</h1>
            <button class="btn btn-primary"> <i class="fas fa-plus me-2"></i> Add Stock Movement</button>


            <!-- <button" class="btn btn-primary" type="button">
                <i class="fas fa-plus me-2"></i> Add StockMovement
                </button> -->
        </div>
        <table class="table table-striped table-hover">
            <thead class="table-dark">
                <tr>
                    <th scope="col">S. No</th>
                    <th scope="col">Inventory Item</th>
                    <th scope="col">Movement_type</th>
                    <th scope="col">Quantity</th>
                    <th scope="col">Recorded at</th>
                    <th scope="col">Reason</th>
                    <th scope="col">Purchase Order Item</th>
                    <th scope="col">Sales Order Item</th>
                    <th scope="col">Actions</th>

                </tr>
            </thead>
            <tbody>
                <tr v-for="stock in store.StockMovement" :key="stock.id">
                    <th scope="row">{{ stock.id }}</th>
                    <th scope="row">{{ stock.inventory_item }}</th>
                    <th scope="row">{{ stock.movement_type }}</th>
                    <th scope="row">{{ stock.quantity }}</th>
                    <th scope="row">{{ stock.recorded_at }}</th>
                    <th scope="row">{{ stock.reason }}</th>
                    <th scope="row">{{ stock.purchase_order_item }}</th>
                    <th scope="row">{{ stock.purchase_order_item }}</th>
                    <td class="text-center">
                        <div class="btn-group" role="group">

                            <button class="btn btn-outline-primary btn-sm me-2" title="Edit">
                                <i class="bi bi-pencil"></i>
                            </button>
                            <button class="btn btn-outline-danger btn-sm" title="Delete">
                                <i class="bi bi-trash"></i>
                            </button>


                        </div>
                    </td>
                </tr>

            </tbody>
        </table>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useStockmovementStore } from '@/stores/inventory/stockMovementStore';

const store = useStockmovementStore()
const selectedStockMovement = ref(null)

onMounted(async () => {
    await store.fetchStockMovement()
})
</script>
<style scoped>
.table {
    margin-bottom: 0;
    font-size: 10 !important;
}

.btn-group .btn {
    margin: 0 1px;
}
</style>