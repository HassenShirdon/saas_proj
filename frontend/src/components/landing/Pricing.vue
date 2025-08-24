<template>
  <section id="pricing"
    class="py-24 bg-gradient-to-br from-white via-gray-0 to-gray-50 dark:from-gray-900 dark:via-gray-800 dark:to-gray-900">
    <div class="max-w-7xl mx-auto px-6 text-center mb-16">
      <h2 class="text-2xl md:text-3xl font-bold text-gray-900 dark:text-white tracking-tight mb-4">
        Pricing Plans
      </h2>
      <p class="text-gray-600 dark:text-gray-300 max-w-3xl mx-auto text-base leading-relaxed">
        Choose a plan that fits your business needs. Our flexible pricing ensures you only pay for what you use.
      </p>
    </div>

    <div class="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-2 gap-12 px-6">
      <!-- Free Plan -->
      <div
        class="bg-white dark:bg-gray-800 rounded-2xl shadow-md hover:shadow-2xl transition p-10 text-center flex flex-col items-center">
        <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-4">Free</h3>
        <p class="text-gray-600 dark:text-gray-300 mb-6">Includes HRM only</p>
        <div class="text-2xl font-bold text-gray-900 dark:text-white mb-6">$0<span
            class="text-base font-normal">/month</span></div>
        <ul class="text-gray-600 dark:text-gray-300 mb-6 space-y-2 text-left">
          <li>✅ HRM module</li>
          <li>❌ Inventory, Finance, Reports</li>
        </ul>
        <button class="px-6 py-3 bg-accent hover:bg-accent/90 text-white font-medium rounded-xl shadow-lg transition">
          Get Started
        </button>
      </div>

      <!-- Premium Plan -->
      <div
        class="bg-white dark:bg-gray-800 rounded-2xl shadow-md hover:shadow-2xl transition p-10 text-center flex flex-col items-center">
        <h3 class="text-xl font-semibold text-gray-900 dark:text-white mb-4">Premium</h3>
        <p class="text-gray-600 dark:text-gray-300 mb-6">Includes all modules: HRM, Inventory, Finance, Report
          Generation</p>
        <div class="text-4xl font-bold text-gray-900 dark:text-white mb-6">$200<span
            class="text-base font-normal">/month</span></div>
        <ul class="text-gray-600 dark:text-gray-300 mb-6 space-y-2 text-left">
          <li>✅ HRM module</li>
          <li>✅ Inventory module</li>
          <li>✅ Finance module</li>
          <li>✅ Report Generation module</li>
        </ul>
        <button class="px-6 py-3 bg-blue-500 hover:bg-blue-600 text-white font-medium rounded-xl shadow-lg transition">
          Get Started
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
// Pricing section logic if needed
</script>
