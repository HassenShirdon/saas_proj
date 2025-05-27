<template>
  <aside class="sidebar bg-primary">
    <div class="sidebar-header d-flex align-items-center justify-content-between px-3 py-4">
      <h2 class="mb-0 fs-4 fw-semibold text-white">Dashboard</h2>
      <button class="btn btn-sm btn-outline-light d-lg-none" @click="$emit('toggle-collapse')">
        <i class="bi bi-x-lg"></i>
      </button>
    </div>

    <nav class="menu px-2">
      <ul class="nav flex-column">
        <li class="nav-item">
          <RouterLink to="/dashboard" class="nav-link d-flex align-items-center text-white py-3 rounded-3"
            active-class="active">
            <i class="bi bi-house-door me-3"></i>
            <span>Home</span>
          </RouterLink>
        </li>

        <li class="nav-item">
          <div
            class="nav-link d-flex align-items-center justify-content-between text-white py-3 rounded-3 cursor-pointer"
            :class="{ 'active': showInventory }" @click="toggleInventory">
            <div class="d-flex align-items-center">
              <i class="bi bi-box-seam me-3"></i>
              <span>Inventory</span>
            </div>
            <i class="bi bi-chevron-down transition-all" :class="{ 'rotate-180': showInventory }"></i>
          </div>

          <ul v-if="showInventory" class="submenu nav flex-column ps-5 mt-1">
            <li class="nav-item" v-for="item in inventoryItems" :key="item.to">
              <RouterLink :to="item.to" class="nav-link d-flex align-items-center text-white py-2 rounded-3"
                active-class="active">
                <i :class="`bi ${item.icon} me-3`"></i>
                <span>{{ item.label }}</span>
              </RouterLink>
            </li>
          </ul>
        </li>

        <li class="nav-item" v-for="item in menuItems" :key="item.to">
          <RouterLink :to="item.to" class="nav-link d-flex align-items-center text-white py-3 rounded-3"
            active-class="active">
            <i :class="`bi ${item.icon} me-3`"></i>
            <span>{{ item.label }}</span>
          </RouterLink>
        </li>
      </ul>
    </nav>

    <div class="px-3 py-4 mt-auto">
      <div class="user-profile d-flex align-items-center">
        <div class="avatar me-3">
          <img src="https://via.placeholder.com/40" alt="User" class="rounded-circle" width="40" height="40">
        </div>
        <div class="user-info text-white">
          <div class="fw-medium">John Doe</div>
          <small class="text-white-50">Admin</small>
        </div>
      </div>
    </div>
  </aside>
</template>

<script>
export default {
  data() {
    return {
      showInventory: false,
      inventoryItems: [
        { to: 'dashboard/products', label: 'Products', icon: 'bi-box' },
        { to: 'dashboard/categories', label: 'Categories', icon: 'bi-tags' },
        { to: '/brands', label: 'Brands', icon: 'bi-star' },
        { to: 'dashboard/suppliers', label: 'Suppliers', icon: 'bi-truck' },
        { to: 'dashboard/customers', label: 'Customers', icon: 'bi-people' },
        { to: 'dashboard/units', label: 'Units', icon: 'bi-rulers' },
        { to: 'dashboard/stock', label: 'Stock', icon: 'bi-clipboard-data' },
        { to: 'dashboard/purchases', label: 'Purchases', icon: 'bi-cart-plus' },
        { to: 'dashboard/sales', label: 'Sales', icon: 'bi-cart-check' },
        { to: 'dashboard/returns', label: 'Returns', icon: 'bi-arrow-return-left' }
      ],
      menuItems: [
        { to: '/reports', label: 'Reports', icon: 'bi-graph-up' },
        { to: '/settings', label: 'Settings', icon: 'bi-gear' }
      ]
    }
  },
  methods: {
    toggleInventory() {
      this.showInventory = !this.showInventory
    },
  },
}
</script>

<style scoped>
.sidebar {
  width: 280px;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  display: flex;
  flex-direction: column;
  z-index: 1030;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
  transition: all 0.3s ease;
  background: linear-gradient(135deg, #0d6efd 0%, #0b5ed7 100%);
}

.sidebar-header {
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.nav-link {
  transition: all 0.2s ease;
  margin-bottom: 0.25rem;
}

.nav-link:hover:not(.active) {
  background-color: rgba(255, 255, 255, 0.1) !important;
}

.nav-link.active {
  background-color: rgba(255, 255, 255, 0.2) !important;
  font-weight: 500;
}

.submenu .nav-link {
  padding-top: 0.5rem;
  padding-bottom: 0.5rem;
  font-size: 0.875rem;
}

.submenu .nav-link.active {
  background-color: rgba(255, 255, 255, 0.15) !important;
}

.cursor-pointer {
  cursor: pointer;
}

.transition-all {
  transition: all 0.3s ease;
}

.rotate-180 {
  transform: rotate(180deg);
}

.user-profile {
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .sidebar {
    transform: translateX(-100%);
  }

  .sidebar.show {
    transform: translateX(0);
  }
}
</style>