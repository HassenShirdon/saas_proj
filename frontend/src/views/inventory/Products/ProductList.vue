<!-- src/views/Products/ProductList.vue -->
<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Product List</h1>

    <ProductForm @submit="handleCreate" />

    <ul v-if="!loading">
      <li v-for="product in products" :key="product.id" class="border p-2 my-2">
        <div class="flex justify-between">
          <div>
            <h2 class="font-semibold">{{ product.name }}</h2>
            <p>Price: {{ product.price }}</p>
          </div>
          <div class="space-x-2">
            <button @click="edit(product)">✏️</button>
            <button @click="remove(product.id)">🗑️</button>
          </div>
        </div>

        <ProductForm v-if="selected?.id === product.id" :initial="selected" @submit="handleUpdate"
          @cancel="selected = null" />
      </li>
    </ul>

    <p v-else>Loading...</p>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { useProductStore } from '@/stores/inventory/productStore'
import ProductForm from '@/components/products/ProductForm.vue'

const store = useProductStore()
const selected = ref(null)

const products = store.products
const loading = store.loading

onMounted(() => {
  store.fetchProducts()
})

const handleCreate = async (data) => {
  await store.addProduct(data)
}

const handleUpdate = async (data) => {
  await store.updateProduct(selected.value.id, data)
  selected.value = null
}

const edit = (product) => {
  selected.value = { ...product }
}

const remove = async (id) => {
  if (confirm('Delete this product?')) {
    await store.removeProduct(id)
  }
}
</script>
