<template>
  <div class="flex h-screen bg-gray-100 dark:bg-gray-900">
    <!-- Sidebar -->
    <Sidebar :open="sidebarOpen" @close="sidebarOpen = false" />

    <!-- Main content area -->
    <div class="flex-1 flex flex-col">
      <!-- Menubar -->
      <Menubar @toggle-sidebar="sidebarOpen = !sidebarOpen" />

      <!-- Content -->
      <main class="flex-1 overflow-y-auto p-6">
        <slot />
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import Sidebar from '../components/dashboard/Sidebar.vue'
import Menubar from '../components/dashboard/Menubar.vue'

const sidebarOpen = ref(false)
</script>
