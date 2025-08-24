<template>
  <section
    class="relative min-h-screen w-full bg-gradient-to-br from-white via-gray-0 to-gray-50 flex items-center overflow-hidden">
    <!-- Decorative Background -->
    <div class="absolute inset-0 w-full h-full">
      <div class="absolute -top-24 -left-24 w-72 h-72 bg-accent/80 rounded-full blur-3xl"></div>
      <div class="absolute bottom-0 right-0 w-80 h-80 bg-highlight/80 rounded-full blur-3xl"></div>
    </div>

    <!-- Content Wrapper -->
    <div class="relative z-10 max-w-7xl mx-auto px-6 grid grid-cols-1 md:grid-cols-2 gap-12 items-center">
      <!-- Left Column: Text -->
      <div class="text-center md:text-left">
        <h1
          class="text-4xl md:text-6xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-accent to-highlight leading-tight">
          Build the Future, Faster
        </h1>
        <p class="mt-6 text-base md:text-lg text-gray-700 dark:text-gray-300 max-w-xl leading-relaxed">
          Empower your creativity with our cutting-edge platform. Design, develop, and deploy stunning web experiences
          with speed, scalability, and unmatched efficiency. Join us to transform your ideas into reality.
        </p>

        <!-- Call to Action Buttons -->
        <div
          class="mt-10 flex flex-col sm:flex-row sm:space-x-4 space-y-4 sm:space-y-0 justify-center md:justify-start">
          <a href="#pricing">
            <button
              class="px-6 py-3 bg-accent hover:bg-accent/90 text-white font-medium rounded-xl shadow-lg transition">
              Get Started <i class="pi pi-arrow-right ml-2"></i>
            </button>
          </a>
          <a href="#about">
            <button
              class="px-6 py-3 bg-white border border-gray-200 text-gray-800 font-medium rounded-xl shadow-sm hover:shadow-md transition">
              Learn More
            </button>
          </a>
        </div>
      </div>

      <!-- Right Column: Image + Badges -->
      <div class="relative flex justify-center md:justify-end">
        <div class="relative w-full max-w-md">
          <!-- Main Illustration -->
          <img src="../../assets/HeroImage2.jpg" alt="Platform Preview" class="w-full rounded-2xl shadow-lg" />

          <!-- Floating Badges -->
          <div class="absolute -top-6 -left-6 bg-white shadow-md rounded-xl px-4 py-2 flex items-center space-x-2">
            <i class="pi pi-check-circle text-green-500"></i>
            <span class="text-sm font-medium text-gray-700">Trusted by 1,000+ Teams</span>
          </div>

          <div class="absolute bottom-6 -right-6 bg-white shadow-md rounded-xl px-4 py-2 flex items-center space-x-2">
            <i class="pi pi-bolt text-yellow-500"></i>
            <span class="text-sm font-medium text-gray-700">Lightning Fast Deployment</span>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>
