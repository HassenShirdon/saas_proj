<template>
    <div>
        <button class="btn btn-primary" @click="openAddModal">Add Purchase Order</button>
        <div class="table-container table-responsive">
            <table class="table table-striped table-hover">
                <thead class="thead-dark">
                    <tr>
                        <th>PO Number</th>
                        <th>Supplier</th>
                        <th>Order Date</th>
                        <th>Delivery Date</th>
                        <th>Total Amount</th>
                        <th>Status</th>
                        <th>Created At</th>
                        <th>Updated At</th>
                        <th>Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="purchaseorder in store.purchaseOrders" :key="purchaseorder.po_number">
                        <td>{{ purchaseorder.po_number }}</td>
                        <td>{{ purchaseorder.supplier }}</td>
                        <td>{{ purchaseorder.order_date }}</td>
                        <td>{{ purchaseorder.delivery_date }}</td>
                        <td>{{ purchaseorder.total_amount }}</td>
                        <td>
                            <span :class="['status-badge', purchaseorder.status.toLowerCase()]">
                                {{ purchaseorder.status }}
                            </span>
                        </td>
                        <td>{{ purchaseorder.created_at }}</td>
                        <td>{{ purchaseorder.updated_at }}</td>
                        <td>

                            <button @click="openEditModal(purchaseorder)" class="btn btn-outline-primary btn-sm me-2"
                                title="Edit Customer">
                                <i class="bi bi-pencil"></i>
                            </button>
                            <button @click="deletePurchaseOrder(purchaseorder.id)" class="btn btn-outline-danger btn-sm"
                                title="Delete">
                                <i class="bi bi-trash"></i>
                            </button>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
        <PurchaseOrderModal v-if="showModal" :visible="showModal" :purchaseOrder="selectedPurchaseOrder"
            :isEdit="isEdit" @close="closeModal" @save="handleSave" />
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { usePurchaseOrderStore } from '@/stores/inventory/purchaseOrderStore'
import PurchaseOrderModal from '@/components/PurchaseOrder/purchaseOrderModal.vue'

const store = usePurchaseOrderStore()
const showModal = ref(false)
const selectedPurchaseOrder = ref(null)
const isEdit = ref(false)

onMounted(async () => {
    console.log('Component mounted, fetching purchase orders...')
    await store.fetchPurchaseOrders()
    console.log('Purchase orders fetched:', store.purchaseOrders)
})
const openAddModal = () => {
    selectedPurchaseOrder.value = null
    isEdit.value = false
    showModal.value = true
}

const openEditModal = (purchaseorder) => {
    selectedPurchaseOrder.value = { ...purchaseorder }
    isEdit.value = true
    showModal.value = true
}

const closeModal = () => {
    showModal.value = false
    selectedPurchaseOrder.value = null
    isEdit.value = false
}

const handleSave = async (purchaseOrderData) => {
    try {
        if (isEdit.value) {
            await store.updatePurchaseOrder(selectedPurchaseOrder.value.id, purchaseOrderData)
        } else {
            await store.addPurchaseOrder(purchaseOrderData)
        }
        closeModal()
    } catch (error) {
        console.error('Error saving purchase order:', error)
        // You might want to show an error message to the user here
    }
}
const deletePurchaseOrder = async (id) => {
    if (confirm('Are you sure you want to delete this purchase order? This action cannot be undone.')) {
        try {
            await store.removePurchaseOrder(id)
        } catch (error) {
            console.error('Error deleting purchase order:', error)
            // You might want to show an error message to the user here
        }
    }
}
</script>


<style scoped></style>