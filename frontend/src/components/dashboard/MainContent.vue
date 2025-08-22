<template>
  <div class="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
    <h2 class="text-2xl font-bold mb-4 text-gray-800 dark:text-gray-100">{{ title }}</h2>
    <slot />
  </div>
</template>

<script setup>
defineProps({
  title: String
})
</script>
