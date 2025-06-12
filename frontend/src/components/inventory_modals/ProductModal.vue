<!-- src/components/products/ProductForm.vue -->
<template>
  <form @submit.prevent="onSubmit" class="bg-gray-100 p-4 mb-4 rounded">
    <input v-model="form.name" type="text" placeholder="Product Name" class="input" required />
    <input v-model="form.price" type="number" placeholder="Price" class="input" required />
    <button type="submit" class="btn bg-blue-500 text-white px-4 py-1 rounded">
      {{ initial ? 'Update' : 'Create' }}
    </button>
    <button v-if="initial" type="button" @click="$emit('cancel')" class="ml-2 text-red-500">
      Cancel
    </button>
  </form>
</template>

<script setup>
import { ref, watch } from 'vue'

const props = defineProps({
  initial: Object
})
const emit = defineEmits(['submit', 'cancel'])

const form = ref({
  name: '',
  price: ''
})

watch(
  () => props.initial,
  (value) => {
    form.value = value ? { ...value } : { name: '', price: '' }
  },
  { immediate: true }
)

const onSubmit = () => {
  emit('submit', form.value)
}
</script>

<style scoped>
.input {
  display: block;
  margin-bottom: 10px;
  padding: 6px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
}
</style>
