<template>
  <aside
    class="bg-white border-end shadow-sm transition-all duration-300 position-fixed top-0 start-0 h-100 z-50"
    :class="{ 'w-100px': isCollapsed && !isSidebarOpen, 'w-280px': !isCollapsed || isSidebarOpen, 'd-none': !isSidebarOpen && !isCollapsed, 'd-md-block': true }"
  >
    <!-- Header -->
    <div class="sidebar-header bg-white border-bottom d-flex align-items-center justify-content-between p-3 fixed-top">
      <div class="d-flex align-items-center gap-2">
        <div class="logo-icon bg-primary text-white rounded-3 d-flex align-items-center justify-content-center">
          <i class="bi bi-grid fs-5"></i>
        </div>
        <span class="logo-text fw-semibold text-primary" v-show="!isCollapsed || isSidebarOpen">Dashboard</span>
      </div>
      <button class="btn btn-outline-light rounded-circle p-2 d-md-block" @click="toggleCollapse" aria-label="Toggle sidebar">
        <i class="bi" :class="isCollapsed ? 'bi-chevron-right' : 'bi-chevron-left'"></i>
      </button>
      <button class="btn btn-outline-light rounded-circle p-2 d-block d-md-none" @click="toggleMobile" aria-label="Close sidebar">
        <i class="bi bi-x-lg"></i>
      </button>
    </div>

    <!-- Navigation -->
    <nav class="sidebar-nav mt-5 pt-3 px-2 overflow-y-auto">
      <ul class="nav flex-column gap-1">
        <!-- Home -->
        <li class="nav-item">
          <RouterLink to="/dashboard" class="nav-link text-primary" active-class="active" exact-active-class="exact-active">
            <div class="d-flex align-items-center gap-2">
              <i class="bi bi-house-door fs-5"></i>
              <span class="nav-text" v-show="!isCollapsed || isSidebarOpen">Home</span>
            </div>
            <div class="nav-indicator"></div>
          </RouterLink>
        </li>

        <!-- Inventory -->
        <li class="nav-item">
          <button
            class="nav-link text-primary d-flex align-items-center gap-2 w-100"
            :class="{ active: activeSection === 'inventory' }"
            @click="toggleSection('inventory')"
            :aria-expanded="activeSection === 'inventory'"
          >
            <i class="bi bi-box-seam fs-5"></i>
            <span class="nav-text flex-grow-1" v-show="!isCollapsed || isSidebarOpen">Inventory</span>
            <i class="bi bi-chevron-down" :class="{ 'rotate-180': activeSection === 'inventory' }" v-show="!isCollapsed || isSidebarOpen"></i>
            <div class="nav-indicator"></div>
          </button>
          <transition name="slide-down">
            <ul v-show="activeSection === 'inventory' && (!isCollapsed || isSidebarOpen)" class="nav flex-column ms-3 border-start">
              <li v-for="item in inventoryItems" :key="item.to" class="nav-item">
                <RouterLink :to="item.to" class="nav-link text-primary" active-class="active">
                  <div class="d-flex align-items-center gap-2">
                    <i :class="item.icon"></i>
                    <span>{{ item.label }}</span>
                  </div>
                  <div class="submenu-indicator"></div>
                </RouterLink>
              </li>
            </ul>
          </transition>
        </li>

        <!-- Finance -->
        <li class="nav-item">
          <button
            class="nav-link text-primary d-flex align-items-center gap-2 w-100"
            :class="{ active: activeSection === 'finance' }"
            @click="toggleSection('finance')"
            :aria-expanded="activeSection === 'finance'"
          >
            <i class="bi bi-cash-stack fs-5"></i>
            <span class="nav-text flex-grow-1" v-show="!isCollapsed || isSidebarOpen">Finance</span>
            <i class="bi bi-chevron-down" :class="{ 'rotate-180': activeSection === 'finance' }" v-show="!isCollapsed || isSidebarOpen"></i>
            <div class="nav-indicator"></div>
          </button>
          <transition name="slide-down">
            <ul v-show="activeSection === 'finance' && (!isCollapsed || isSidebarOpen)" class="nav flex-column ms-3 border-start">
              <!-- Chart of Accounts -->
              <li class="nav-item">
                <button
                  class="nav-link text-primary d-flex align-items-center gap-2 w-100"
                  :class="{ active: activeSubsection === 'chartOfAccounts' }"
                  @click="toggleSubsection('chartOfAccounts')"
                >
                  <i class="bi bi-journal-bookmark"></i>
                  <span class="flex-grow-1">Chart of Accounts</span>
                  <i class="bi bi-chevron-down" :class="{ 'rotate-180': activeSubsection === 'chartOfAccounts' }"></i>
                  <div class="submenu-indicator"></div>
                </button>
                <transition name="slide-down">
                  <ul v-show="activeSubsection === 'chartOfAccounts'" class="nav flex-column ms-3 border-start">
                    <li v-for="item in chartOfAccountsItems" :key="item.to" class="nav-item">
                      <RouterLink :to="item.to" class="nav-link text-primary" active-class="active">
                        <div class="d-flex align-items-center gap-2">
                          <i :class="item.icon"></i>
                          <span>{{ item.label }}</span>
                        </div>
                        <div class="nested-indicator"></div>
                      </RouterLink>
                    </li>
                  </ul>
                </transition>
              </li>

              <!-- Journal Entries -->
              <li class="nav-item">
                <button
                  class="nav-link text-primary d-flex align-items-center gap-2 w-100"
                  :class="{ active: activeSubsection === 'journalEntries' }"
                  @click="toggleSubsection('journalEntries')"
                >
                  <i class="bi bi-journal-text"></i>
                  <span class="flex-grow-1">Journal Entries</span>
                  <i class="bi bi-chevron-down" :class="{ 'rotate-180': activeSubsection === 'journalEntries' }"></i>
                  <div class="submenu-indicator"></div>
                </button>
                <transition name="slide-down">
                  <ul v-show="activeSubsection === 'journalEntries'" class="nav flex-column ms-3 border-start">
                    <li v-for="item in journalEntryItems" :key="item.to" class="nav-item">
                      <RouterLink :to="item.to" class="nav-link text-primary" active-class="active">
                        <div class="d-flex align-items-center gap-2">
                          <i :class="item.icon"></i>
                          <span>{{ item.label }}</span>
                        </div>
                        <div class="nested-indicator"></div>
                      </RouterLink>
                    </li>
                  </ul>
                </transition>
              </li>

              <!-- Invoices -->
              <li class="nav-item">
                <button
                  class="nav-link text-primary d-flex align-items-center gap-2 w-100"
                  :class="{ active: activeSubsection === 'invoices' }"
                  @click="toggleSubsection('invoices')"
                >
                  <i class="bi bi-file-earmark-text"></i>
                  <span class="flex-grow-1">Invoices</span>
                  <i class="bi bi-chevron-down" :class="{ 'rotate-180': activeSubsection === 'invoices' }"></i>
                  <div class="submenu-indicator"></div>
                </button>
                <transition name="slide-down">
                  <ul v-show="activeSubsection === 'invoices'" class="nav flex-column ms-3 border-start">
                    <li v-for="item in invoices" :key="item.to" class="nav-item">
                      <RouterLink :to="item.to" class="nav-link text-primary" active-class="active">
                        <div class="d-flex align-items-center gap-2">
                          <i :class="item.icon"></i>
                          <span>{{ item.label }}</span>
                        </div>
                        <div class="nested-indicator"></div>
                      </RouterLink>
                    </li>
                  </ul>
                </transition>
              </li>

              <!-- Other Finance Items -->
              <li v-for="item in otherFinanceItems" :key="item.to" class="nav-item">
                <RouterLink :to="item.to" class="nav-link text-primary" active-class="active">
                  <div class="d-flex align-items-center gap-2">
                    <i :class="item.icon"></i>
                    <span>{{ item.label }}</span>
                  </div>
                  <div class="submenu-indicator"></div>
                </RouterLink>
              </li>
            </ul>
          </transition>
        </li>

        <!-- HRM -->
        <li class="nav-item">
          <button
            class="nav-link text-primary d-flex align-items-center gap-2 w-100"
            :class="{ active: activeSection === 'hrm' }"
            @click="toggleSection('hrm')"
            :aria-expanded="activeSection === 'hrm'"
          >
            <i class="bi bi-people fs-5"></i>
            <span class="nav-text flex-grow-1" v-show="!isCollapsed || isSidebarOpen">HRM</span>
            <i class="bi bi-chevron-down" :class="{ 'rotate-180': activeSection === 'hrm' }" v-show="!isCollapsed || isSidebarOpen"></i>
            <div class="nav-indicator"></div>
          </button>
          <transition name="slide-down">
            <ul v-show="activeSection === 'hrm' && (!isCollapsed || isSidebarOpen)" class="nav flex-column ms-3 border-start">
              <li v-for="item in hrm" :key="item.to" class="nav-item">
                <RouterLink :to="item.to" class="nav-link text-primary" active-class="active">
                  <div class="d-flex align-items-center gap-2">
                    <i :class="item.icon"></i>
                    <span>{{ item.label }}</span>
                  </div>
                  <div class="submenu-indicator"></div>
                </RouterLink>
              </li>
            </ul>
          </transition>
        </li>

        <!-- Reports -->
        <li class="nav-item">
          <RouterLink to="/dashboard/reports" class="nav-link text-primary" active-class="active">
            <div class="d-flex align-items-center gap-2">
              <i class="bi bi-graph-up fs-5"></i>
              <span class="nav-text" v-show="!isCollapsed || isSidebarOpen">Reports</span>
            </div>
            <div class="nav-indicator"></div>
          </RouterLink>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script>
export default {
  name: 'SidebarArea',
  props: {
    isCollapsed: {
      type: Boolean,
      default: false,
    },
    isSidebarOpen: {
      type: Boolean,
      default: false,
    },
  },
  emits: ['toggle-collapse', 'toggle-mobile'],
  data() {
    return {
      activeSection: null,
      activeSubsection: null,
      inventoryItems: [
        { to: '/dashboard/categories', label: 'Categories', icon: 'bi bi-tags' },
        { to: '/dashboard/products', label: 'Products', icon: 'bi bi-box' },
        { to: '/dashboard/suppliers', label: 'Suppliers', icon: 'bi bi-truck' },
        { to: '/dashboard/purchase-orders', label: 'Purchase Orders', icon: 'bi bi-cart-plus' },
        { to: '/dashboard/inventory-items', label: 'Inventory Items', icon: 'bi bi-card-list' },
        { to: '/dashboard/stock-movement', label: 'Stock Movement', icon: 'bi bi-clipboard-data' },
        { to: '/dashboard/customers', label: 'Customers', icon: 'bi bi-people' },
        { to: '/dashboard/sales', label: 'Sales', icon: 'bi bi-cart-check' },
        { to: '/dashboard/returns', label: 'Returns', icon: 'bi bi-arrow-return-left' },
      ],
      hrm: [
        { to: '/dashboard/employees', label: 'Employees', icon: 'bi bi-person' },
        { to: '/dashboard/departments', label: 'Departments', icon: 'bi bi-building' },
        { to: '/dashboard/attendance', label: 'Attendance', icon: 'bi bi-calendar-check' },
        { to: '/dashboard/leaves', label: 'Leaves', icon: 'bi bi-calendar-minus' },
        { to: '/dashboard/salaries', label: 'Salaries', icon: 'bi bi-cash-stack' },
        { to: '/dashboard/performance-reviews', label: 'Performance Reviews', icon: 'bi bi-star' },
      ],
      chartOfAccountsItems: [
        { to: '/dashboard/account-types', label: 'Account Types', icon: 'bi bi-journal-bookmark' },
        { to: '/dashboard/Accounts', label: 'Accounts', icon: 'bi bi-journal-text' },
      ],
      journalEntryItems: [
        { to: '/dashboard/journal-entries', label: 'Journal Entries', icon: 'bi bi-journal' },
        { to: '/dashboard/journal-entry-lines', label: 'Journal Entry Lines', icon: 'bi bi-journal-plus' },
      ],
      invoices: [
        { to: '/dashboard/customer-invoices', label: 'Customer Invoices', icon: 'bi bi-file-earmark-text' },
        { to: '/dashboard/supplier-invoices', label: 'Supplier Invoices', icon: 'bi bi-file-earmark-text' },
      ],
      otherFinanceItems: [
        { to: '/dashboard/Expenses', label: 'Expenses', icon: 'bi bi-wallet2' },
        { to: '/dashboard/financial-periods', label: 'Financial Periods', icon: 'bi bi-calendar-range' },
      ],
    };
  },
  methods: {
    toggleCollapse() {
      this.$emit('toggle-collapse');
    },
    toggleMobile() {
      this.$emit('toggle-mobile');
    },
    toggleSection(section) {
      this.activeSection = this.activeSection === section ? null : section;
      if (this.activeSection !== section) {
        this.activeSubsection = null;
      }
    },
    toggleSubsection(subsection) {
      this.activeSubsection = this.activeSubsection === subsection ? null : subsection;
    },
  },
};
</script>

<style scoped>
.w-280px {
  width: 280px;
}
.w-100px {
  width: 100px;
}
.sidebar-header {
  height: 64px;
  width: inherit;
  z-index: 1030;
}
.sidebar-nav {
  height: calc(100vh - 64px);
  margin-top: 64px;
}
.logo-icon {
  width: 36px;
  height: 36px;
}
.nav-link, .nav-link:hover, .nav-link:focus {
  color: #3B82F6;
  background: transparent;
  border-radius: 8px;
  padding: 12px 16px;
  text-decoration: none;
}
.nav-link.active {
  background: #F0F0F0;
  font-weight: 600;
}
.nav-indicator, .submenu-indicator, .nested-indicator {
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 3px;
  height: 24px;
  background: #3B82F6;
  border-radius: 0 2px 2px 0;
  opacity: 0;
  transition: opacity 0.3s ease;
}
.nav-link.active .nav-indicator,
.nav-link.active .submenu-indicator,
.nav-link.active .nested-indicator {
  opacity: 1;
}
.nav-text, .logo-text {
  transition: opacity 0.3s ease;
}
.w-100px .nav-text,
.w-100px .logo-text,
.w-100px .bi-chevron-down {
  opacity: 0;
  pointer-events: none;
}
.w-100px .nav-link {
  justify-content: center;
  padding: 12px;
}
.bi-chevron-down {
  transition: transform 0.3s ease;
}
.bi-chevron-down.rotate-180 {
  transform: rotate(180deg);
}
.border-start {
  border-left: 2px solid #F0F0F0 !important;
}
.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.3s ease;
  overflow: hidden;
}
.slide-down-enter-from,
.slide-down-leave-to {
  max-height: 0;
  opacity: 0;
  transform: translateY(-8px);
}
.slide-down-enter-to,
.slide-down-leave-from {
  max-height: 800px;
  opacity: 1;
  transform: translateY(0);
}
@media (max-width: 768px) {
  aside {
    transform: translateX(-100%);
    transition: transform 0.3s ease;
  }
  aside.d-block {
    transform: translateX(0);
  }
}
</style>