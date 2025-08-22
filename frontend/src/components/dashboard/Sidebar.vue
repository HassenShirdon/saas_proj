<template>
  <!-- Overlay for mobile -->
  <div
    v-if="open"
    class="fixed inset-0 bg-black bg-opacity-50 z-40 lg:hidden"
    @click="$emit('close')"
  ></div>

  <!-- Sidebar -->
  <aside
    class="fixed lg:static inset-y-0 left-0 z-50 w-64 transform bg-white dark:bg-gray-800 shadow-lg lg:translate-x-0 transition-transform"
    :class="open ? 'translate-x-0' : '-translate-x-full'"
  >
    <div class="p-6 text-2xl font-bold border-b border-gray-200 dark:border-gray-700">
      <span class="text-accent">Marjaan</span><span class="text-highlight">Solutions</span>
    </div>
    <nav class="mt-6 space-y-2">
      <a
        v-for="item in menuItems"
        :key="item.label"
        :href="item.href"
        class="flex items-center px-6 py-3 rounded-md text-gray-700 dark:text-gray-200 hover:bg-accent hover:text-white"
      >
        <i :class="item.icon" class="pi mr-3"></i>
        {{ item.label }}
      </a>
    </nav>
  </aside>
</template>

<script setup>
defineProps({
  open: Boolean
})

const menuItems = [
  { label: "Dashboard", href: "#", icon: "pi pi-home" },
  { label: "Users", href: "#", icon: "pi pi-users" },
  { label: "Reports", href: "#", icon: "pi pi-chart-line" },
  { label: "Settings", href: "#", icon: "pi pi-cog" }
]
</script>
