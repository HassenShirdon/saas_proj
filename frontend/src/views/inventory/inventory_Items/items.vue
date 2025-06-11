<template>
    <div class="inventory-table-container">
        <div class="table-header">
            <h2 class="table-title">Inventory Products</h2>
            <button class="btn btn-primary add-btn" @click="isEdit = false; selectedItem = null;">
                <i class="bi bi-plus-lg"></i> Add Item
            </button>
        </div>
        <div class="table-responsive modern-table">
            <table class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>Sku</th>
                        <th>Name</th>
                        <th>Category</th>
                        <th>Description</th>
                        <th>Unit Cost</th>
                        <th>Selling Price</th>
                        <th>Current Stock</th>
                        <th class="text-center">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <tr v-for="item in store.items" :key="item.sku">
                        <td>{{ item.sku }}</td>
                        <td class="fw-semibold">{{ item.name }}</td>
                        <td>{{ item.category || '-' }}</td>
                        <td>
                            <span v-if="item.description" class="desc-truncate" :title="item.description">
                                {{ item.description }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td>
                            <span v-if="item.unit_cost">${{ item.unit_cost }}</span>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td>
                            <span v-if="item.selling_price">${{ item.selling_price }}</span>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td>
                            <span v-if="item.current_stock !== null && item.current_stock !== undefined">
                                {{ item.current_stock }}
                            </span>
                            <span v-else class="text-muted">-</span>
                        </td>
                        <td class="text-center">
                            <button @click="editItem(item)" class="btn btn-outline-primary btn-sm me-2" title="Edit">
                                <i class="bi bi-pencil"></i>
                            </button>
                            <button @click="deleteItem(item.id)" class="btn btn-outline-danger btn-sm" title="Delete">
                                <i class="bi bi-trash"></i>
                            </button>
                        </td>
                    </tr>
                    <tr v-if="store.items.length === 0">
                        <td colspan="8" class="text-center text-muted py-4">No Products found.</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import { useItemsStore } from '@/stores/inventory/itemsStore'

const store = useItemsStore()
const selectedItem = ref(null)
const isEdit = ref(false)

onMounted(async () => {
    await store.fetchItems()
})

const handleSave = async (itemData) => {
    try {
        if (isEdit.value) {
            await store.updateItem(selectedItem.value.id, itemData)
        } else {
            await store.addItem(itemData)
        }
    } catch (error) {
        console.error('Error saving item:', error)
    }
}

const deleteItem = async (id) => {
    if (confirm('Are you sure you want to delete this item? This action cannot be undone.')) {
        try {
            await store.removeItem(id)
        } catch (error) {
            console.error('Error deleting item:', error)
        }
    }
}
</script>

<style scoped>
.inventory-table-container {
    background: #fff;
    border-radius: 18px;
    box-shadow: 0 4px 24px 0 rgba(0, 0, 0, 0.07);
    padding: 32px 24px 24px 24px;
    max-width: 1100px;
    margin: 40px auto;
}

.table-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 18px;
}

.table-title {
    font-size: 1.7rem;
    font-weight: 700;
    color: #2d3748;
    margin: 0;
}

.add-btn {
    font-weight: 600;
    border-radius: 8px;
    padding: 8px 18px;
    font-size: 1rem;
    box-shadow: 0 2px 8px 0 rgba(0, 123, 255, 0.08);
    transition: background 0.2s;
}

.add-btn i {
    margin-right: 6px;
}

.table-responsive {
    margin-top: 20px;
}

.modern-inventory-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    background: #f9fafb;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 2px 8px 0 rgba(0, 0, 0, 0.04);
}

.modern-inventory-table thead tr {
    background: linear-gradient(90deg, #2563eb 0%, #1e40af 100%);
    color: #fff;
}

.modern-inventory-table th,
.modern-inventory-table td {
    padding: 14px 16px;
    text-align: left;
    font-size: 1rem;
}

.modern-inventory-table th {
    font-weight: 700;
    letter-spacing: 0.02em;
    border-bottom: 2px solid #e5e7eb;
}

.modern-inventory-table tbody tr {
    background: #fff;
    transition: background 0.2s;
}

.modern-inventory-table tbody tr:hover {
    background: #f1f5f9;
}

.modern-inventory-table td {
    border-bottom: 1px solid #e5e7eb;
    vertical-align: middle;
}

.modern-inventory-table td .btn {
    min-width: 36px;
    min-height: 36px;
    border-radius: 6px;
    font-size: 1.1rem;
    transition: box-shadow 0.2s;
}

.modern-inventory-table td .btn-outline-primary {
    border-color: #2563eb;
    color: #2563eb;
}

.modern-inventory-table td .btn-outline-primary:hover {
    background: #2563eb;
    color: #fff;
}

.modern-inventory-table td .btn-outline-danger {
    border-color: #ef4444;
    color: #ef4444;
}

.modern-inventory-table td .btn-outline-danger:hover {
    background: #ef4444;
    color: #fff;
}

.desc-truncate {
    display: inline-block;
    max-width: 180px;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
    vertical-align: bottom;
}

.text-muted {
    color: #9ca3af !important;
}

@media (max-width: 900px) {
    .inventory-table-container {
        padding: 16px 4px;
    }

    .modern-inventory-table th,
    .modern-inventory-table td {
        padding: 10px 8px;
        font-size: 0.95rem;
    }

    .table-title {
        font-size: 1.2rem;
    }
}
</style>