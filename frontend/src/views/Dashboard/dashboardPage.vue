<template>
  <div class="dashboard-layout">
    <header class="top-nav-container">
      <!-- Your TopNav component will go here -->
      <TopNav />
    </header>
    <div class="content-body">
      <aside class="sidebar-container">
        <!-- Your Sidebar component will go here -->
        <Sidebar />
      </aside>
      <main class="main-area-container">
        <!-- Your MainArea component will go here -->
        <MainArea />
      </main>
    </div>
  </div>
</template>

<script>
// Make sure to adjust these paths if your components are located elsewhere!
// For example, if they are in 'src/components/dashboard/':
import TopNav from '@/components/dashboard/topNav.vue'
import Sidebar from '@/components/dashboard/sidebarArea.vue'
import MainArea from '@/components/dashboard/mainArea.vue'

export default {
  name: 'DashboardPage',
  components: {
    TopNav,
    Sidebar,
    MainArea,
  },
}
</script>

<style scoped>
/* Define some modern theme variables */
:root {
  --dashboard-font-family:
    system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell,
    'Open Sans', 'Helvetica Neue', sans-serif;
  --dashboard-primary-bg: #f4f7f9; /* Light gray for the overall page background */
  --dashboard-secondary-bg: #ffffff; /* White for content cards, top nav */
  --dashboard-sidebar-bg: #2c3e50; /* A classic dark sidebar */
  --dashboard-sidebar-text-color: #ecf0f1; /* Light text for sidebar */
  --dashboard-sidebar-hover-bg: #34495e; /* Hover color for sidebar items */
  --dashboard-text-color: #333333; /* Dark text for main content */
  --dashboard-border-color: #e0e0e0; /* Light border color */
  --dashboard-shadow-color: rgba(0, 0, 0, 0.08);
  --dashboard-top-nav-height: 60px; /* Example height for top nav */
  --dashboard-sidebar-width: 250px; /* Example width for sidebar */
}

.dashboard-layout {
  display: flex;
  flex-direction: column;
  height: 100vh; /* Full viewport height */
  background-color: var(--dashboard-primary-bg);
  font-family: var(--dashboard-font-family);
  color: var(--dashboard-text-color);
  overflow: hidden; /* Prevent scrollbars on the layout itself */
}

.top-nav-container {
  flex-shrink: 0; /* Prevent top nav from shrinking */
  width: 100%;
  height: var(--dashboard-top-nav-height);
  background-color: var(--dashboard-secondary-bg);
  box-shadow: 0 2px 5px var(--dashboard-shadow-color);
  z-index: 1000; /* Ensure top nav is above other content */
  /* Your TopNav.vue component should handle its internal padding and item alignment */
  display: flex; /* Added for potential direct children alignment */
  align-items: center; /* Vertically center content in top-nav */
  padding: 0 20px; /* Example padding */
}

.content-body {
  display: flex;
  flex-grow: 1; /* Takes up all remaining vertical space */
  overflow: hidden; /* Crucial for allowing children to scroll independently */
}

.sidebar-container {
  flex-shrink: 0; /* Prevent sidebar from shrinking */
  width: var(--dashboard-sidebar-width);
  background-color: var(--dashboard-sidebar-bg);
  color: var(--dashboard-sidebar-text-color);
  box-shadow: 2px 0 6px var(--dashboard-shadow-color);
  overflow-y: auto; /* Allow sidebar content to scroll if it's too long */
  transition: width 0.3s ease-in-out;
  padding-top: 20px; /* Space at the top of the sidebar */
  /* Your Sidebar.vue component will handle its internal list styling, padding for items etc. */
}

.main-area-container {
  flex-grow: 1; /* Takes up all remaining horizontal space */
  padding: 24px; /* Generous padding around the main content */
  overflow-y: auto; /* Allow main content area to scroll */
  background-color: var(--dashboard-primary-bg); /* Or keep it distinct if you prefer */
}

/* Basic responsive adjustments */
@media (max-width: 992px) {
  /* Medium devices (tablets) */
  .sidebar-container {
    width: 220px; /* Slightly narrower sidebar */
  }
}

@media (max-width: 768px) {
  /* Small devices (landscape phones, etc.) */
  /* On smaller screens, you might want to implement a toggle for the sidebar */
  /* For this example, let's make it significantly narrower, perhaps for icons only */
  .sidebar-container {
    width: 70px;
    /* Your Sidebar.vue would need to adapt its content for an icon-only view */
  }
  /* Alternatively, you could hide it and use a hamburger menu in TopNav to toggle its display */
  /* e.g.,
  .sidebar-container {
    position: absolute;
    left: -var(--dashboard-sidebar-width);
    height: calc(100vh - var(--dashboard-top-nav-height));
    top: var(--dashboard-top-nav-height);
    transition: left 0.3s ease-in-out;
  }
  .sidebar-container.is-open {
    left: 0;
  }
  */

  .main-area-container {
    padding: 16px; /* Reduce padding on smaller screens */
  }
}

/*
  Remember: The "beautiful, modern and latest trend" look and feel
  will heavily depend on the actual design and content of your
  TopNav.vue, Sidebar.vue, and MainArea.vue components.
  This dashboardPage.vue provides a solid, clean, and modern foundation for them.
  Consider things like:
  - Consistent iconography
  - Smooth transitions and micro-interactions
  - Clear typography hierarchy
  - Effective use of whitespace
  - Data visualization styles (if applicable)
  - Accessibility (ARIA attributes, keyboard navigation)
*/
</style>
