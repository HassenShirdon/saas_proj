<template>
  <form @submit.prevent="handleSubmit">
    <input v-model="form.email" type="email">
    <input v-model="form.password" type="password">
    <button type="submit">Sign In</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const emit = defineEmits(['success'])
const authStore = useAuthStore()

const form = ref({
  email: '',
  password: ''
})

const handleSubmit = async () => {
  try {
    await authStore.login(form.value)
    emit('success')
  } catch (error) {
    console.error('Login failed', error)
  }
}
</script>