<template>
  <!-- Mobile Toggle Button -->
  <button class="lg:hidden fixed top-4 left-4 z-50 p-2 rounded-md bg-accent text-white shadow-md focus:outline-none"
    @click="$emit('toggle')">
    <i class="pi pi-bars text-xl"></i>
  </button>

  <!-- Overlay for mobile -->
  <div v-if="open" class="fixed inset-0 bg-black bg-opacity-50 z-40 lg:hidden" @click="$emit('close')"></div>

  <!-- Sidebar -->
  <aside
    class="fixed lg:static inset-y-0 left-0 z-50 transform bg-white dark:bg-gray-900 shadow-xl transition-all duration-300 ease-in-out flex flex-col"
    :class="[
      open ? 'translate-x-0 w-64' : '-translate-x-full',
      collapsed ? 'lg:w-20' : 'lg:w-64',
      'lg:translate-x-0'
    ]">
    <!-- Logo / Brand -->
    <div class="flex items-center justify-between p-6 border-b border-gray-200 dark:border-gray-700">
      <div v-if="!collapsed" class="text-2xl font-bold">
        <span class="text-accent">Marjaan</span>
        <span class="text-highlight">Solutions</span>
      </div>
      <div v-else class="text-xl font-bold text-accent">M</div>

      <!-- Collapse Toggle (Desktop Only) -->
      <button class="hidden lg:block p-2 rounded-md text-gray-500 hover:bg-gray-200 dark:hover:bg-gray-700"
        @click="$emit('toggle-collapse')">
        <i :class="collapsed ? 'pi pi-angle-double-right' : 'pi pi-angle-double-left'"></i>
      </button>
    </div>

    <!-- Navigation -->
    <nav class="flex-1 mt-6 space-y-1 overflow-y-auto">
      <a v-for="item in menuItems" :key="item.label" :href="item.href"
        class="flex items-center px-6 py-3 rounded-md text-gray-700 dark:text-gray-200 hover:bg-accent hover:text-white transition-colors">
        <i :class="item.icon" class="pi mr-3 text-lg"></i>
        <span v-if="!collapsed" class="font-medium">{{ item.label }}</span>
      </a>
    </nav>

    <!-- Footer -->
    <div class="p-4 border-t border-gray-200 dark:border-gray-700 text-sm text-gray-500 dark:text-gray-400">
      <span v-if="!collapsed">© 2025 Marjaan Solutions</span>
      <span v-else>©</span>
    </div>
  </aside>
</template>

<script setup>
defineProps({
  open: Boolean,
  collapsed: Boolean
})

const menuItems = [
  { label: "Dashboard", href: "#", icon: "pi pi-home" },
  { label: "Users", href: "#", icon: "pi pi-users" },
  { label: "Reports", href: "#", icon: "pi pi-chart-line" },
  { label: "Settings", href: "#", icon: "pi pi-cog" }
]
</script>
