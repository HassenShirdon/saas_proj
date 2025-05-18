<template>
  <div class="main-container">
    <!-- Top Navigation -->
    <TopNav />

    <!-- Main Content Area -->
    <div class="main-content">
      <router-view />
    </div>
  </div>
</template>

<script></script>

<style scoped>
.main-container {
  display: flex;
  flex-direction: column;
  margin-left: 260px; /* Match sidebar width */
  min-height: 100vh;
  background-color: #f9f9f9;
}

.main-content {
  padding: 24px;
  margin-top: 64px; /* Match top nav height */
  overflow-y: auto;
  flex-grow: 1;
}
</style>
