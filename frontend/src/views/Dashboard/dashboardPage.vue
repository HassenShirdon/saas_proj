<template>
  <div class="d-flex min-vh-100 bg-white">
    <SidebarArea :isCollapsed="isSidebarCollapsed" :isSidebarOpen="isSidebarOpen" @toggle-collapse="toggleSidebar"
      @toggle-mobile="toggleMobileSidebar" />
    <div class="flex-grow-1 d-flex flex-column">
      <TopNav @toggle-sidebar="toggleMobileSidebar" />
      <MainArea :sidebar-collapsed="isSidebarCollapsed" />
    </div>
  </div>
</template>

<script>
import SidebarArea from '@/components/dashboard/sidebarArea.vue';
import TopNav from '@/components/dashboard/topNav.vue';
import MainArea from '@/components/dashboard/mainArea.vue';

export default {
  name: 'DashboardPage',
  components: {
    SidebarArea,
    TopNav,
    MainArea,
  },
  data() {
    return {
      isSidebarCollapsed: false,
      isSidebarOpen: false, // Controls mobile sidebar visibility
    };
  },
  methods: {
    toggleSidebar() {
      this.isSidebarCollapsed = !this.isSidebarCollapsed;
      if (this.isSidebarCollapsed) {
        this.isSidebarOpen = false; // Close mobile sidebar when collapsing
      }
    },
    toggleMobileSidebar() {
      this.isSidebarOpen = !this.isSidebarOpen;
      if (this.isSidebarOpen) {
        this.isSidebarCollapsed = false; // Ensure sidebar is not collapsed when opened on mobile
      }
    },
  },
};
</script>