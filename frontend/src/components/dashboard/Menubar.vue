<template>
  <header class="flex items-center justify-between px-6 py-4 bg-white dark:bg-gray-800 shadow">
    <!-- Mobile Sidebar Toggle -->
    <button class="lg:hidden p-2" @click="$emit('toggle-sidebar')">
      <i class="pi pi-bars text-2xl text-gray-700 dark:text-gray-200"></i>
    </button>

    <!-- Page Title / Branding -->
    <h1 class="text-xl font-semibold text-gray-800 dark:text-gray-100">Dashboard</h1>

    <!-- Right-side actions -->
    <div class="flex items-center space-x-4">
      <button class="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-700">
        <i class="pi pi-bell text-xl"></i>
      </button>
      <button class="p-2 rounded-full hover:bg-gray-200 dark:hover:bg-gray-700">
        <i class="pi pi-user text-xl"></i>
      </button>
    </div>
  </header>
</template>
