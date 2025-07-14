<template>
  <div class="main-container" :class="{ 'ms-100px': sidebarCollapsed, 'ms-280px': !sidebarCollapsed }">
    <!-- Top Navigation -->
    <TopNav @toggle-sidebar="$emit('toggle-sidebar')" />

    <!-- Main Content Area -->
    <div class="main-content container-fluid px-2 px-md-4">
      <div class="table-responsive">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
import TopNav from './topNav.vue';

export default {
  name: 'MainArea',
  components: { TopNav },
  props: {
    sidebarCollapsed: {
      type: Boolean,
      default: false,
    },
  },
};
</script>

<style scoped>
.main-container {
  background-color: #FFFFFF;
  min-height: 100vh;
  transition: margin-left 0.3s ease;
}

.ms-280px {
  margin-left: 280px;
}

.ms-100px {
  margin-left: 100px;
}

.main-content {
  padding-top: 24px;
  margin-top: 64px;
  flex-grow: 1;
  height: calc(100vh - 64px);
  overflow: hidden;
}

.table-responsive {
  width: 100%;
  height: 100%;
  overflow: auto;
  border: 1px solid #F0F0F0;
  border-radius: 8px;
  background: #FFFFFF;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.table-responsive table {
  width: 100%;
  min-width: max-content;
  border-collapse: separate;
  border-spacing: 0;
}

.table-responsive th {
  background: #1F2937;
  color: #FFFFFF;
  position: sticky;
  top: 0;
  z-index: 10;
  font-weight: 600;
  border-bottom: 2px solid #F0F0F0;
}

.table-responsive td {
  border-bottom: 1px solid #F0F0F0;
  white-space: nowrap;
  min-width: 100px;
  max-width: 250px;
  padding: 8px 12px;
}

.table-responsive tbody tr:hover {
  background-color: #F0F0F0;
}

.table-responsive .text-truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 200px;
}

.table-responsive .form-control {
  font-size: 12px !important;
  padding: 4px 8px;
}

@media (max-width: 991px) {
  .main-container {
    margin-left: 0;
  }

  .main-content {
    padding-left: 8px;
    padding-right: 8px;
  }
}

@media (max-width: 768px) {
  .main-content {
    padding-top: 16px;
  }

  .table-responsive th,
  .table-responsive td {
    padding: 6px 8px;
    min-width: 80px;
  }
}
</style>