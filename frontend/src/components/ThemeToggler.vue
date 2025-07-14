<template>
  <button class="btn-primary" @click="toggleTheme">
    {{ isDarkMode ? 'Switch to Light Mode' : 'Switch to Dark Mode' }}
  </button>
</template>

<script setup>
import { useThemeStore } from '@/stores/theme'

const themeStore = useThemeStore()
const isDarkMode = computed(() => themeStore.isDarkMode)

const toggleTheme = () => {
  themeStore.toggleTheme()
}
</script>

<style scoped>
.btn-primary {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}
</style>