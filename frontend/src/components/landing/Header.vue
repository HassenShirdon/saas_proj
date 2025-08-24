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

      <!-- Action Buttons -->
      <div class="hidden md:flex items-center space-x-4">
        <a href="/login"> <button v-if="!isLoggedIn"
            class="px-4 py-2 bg-blue-500 hover:bg-blue-600 text-white rounded-lg">Login</button></a>
        <button v-if="!isLoggedIn"
          class="px-4 py-2 bg-green-500 hover:bg-green-600 text-white rounded-lg">Register</button>
        <button v-if="isLoggedIn" @click="logout"
          class="px-4 py-2 bg-red-500 hover:bg-red-600 text-white rounded-lg">Logout</button>
      </div>

      <button class="md:hidden p-2">
        <i class="pi pi-bars text-2xl"></i>
      </button>
    </div>
  </header>
</template>

<script setup>
import { ref } from 'vue';
import { RouterLink } from 'vue-router';

const isLoggedIn = ref(false); // replace with real auth state

function logout() {
  // implement your logout logic
  isLoggedIn.value = false;
}
</script>
