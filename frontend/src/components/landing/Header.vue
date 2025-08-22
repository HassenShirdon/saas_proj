<template>
  <header class="w-full bg-white dark:bg-gray-900 shadow-md border-b">
    <div class="max-w-7xl mx-auto px-6 py-4 flex items-center justify-between">
      <div class="text-2xl font-bold">
        <RouterLink to="">
          <span class="text-accent">Marjaan</span>
          <span class="text-highlight">Solutions</span>
        </RouterLink>
      </div>
      <nav class="space-x-6 hidden md:flex">
        <a href="#features" class="hover:text-accent">Features</a>
        <a href="#about" class="hover:text-accent">About</a>
        <a href="#pricing" class="hover:text-accent">Pricing</a>
        <a href="#contact" class="hover:text-accent">Contact</a>
      </nav>
      <button class="md:hidden p-2">
        <i class="pi pi-bars text-2xl"></i>
      </button>
    </div>
  </header>
</template>
<script setup>
import { RouterLink } from 'vue-router';

</script>