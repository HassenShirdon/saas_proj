<template>
  <aside class="sidebar" :class="{ 'sidebar-collapsed': isCollapsed }">
    <!-- Header -->
    <div class="sidebar-header">
      <div class="logo-section">
        <div class="logo-icon">
          <i class="bi bi-grid"></i>
        </div>
        <span class="logo-text" v-show="!isCollapsed">Dashboard</span>
      </div>
      <button class="collapse-btn" @click="toggleCollapse" aria-label="Toggle sidebar">
        <i class="bi" :class="isCollapsed ? 'bi-chevron-right' : 'bi-chevron-left'"></i>
      </button>
    </div>

    <!-- Navigation -->
    <nav class="sidebar-nav">
      <ul class="nav-list">
        <!-- Home -->
        <li>
          <RouterLink to="/dashboard" class="nav-link" active-class="active" exact-active-class="exact-active">
            <div class="nav-icon-wrapper">
              <i class="nav-icon bi bi-house-door"></i>
            </div>
            <span class="nav-text" v-show="!isCollapsed">Home</span>
            <div class="nav-indicator"></div>
          </RouterLink>
        </li>

        <!-- Inventory -->
        <li>
          <button class="nav-link nav-toggle" :class="{ active: activeSection === 'inventory' }"
            @click="toggleSection('inventory')" :aria-expanded="activeSection === 'inventory'">
            <div class="nav-icon-wrapper">
              <i class="nav-icon bi bi-box-seam"></i>
            </div>
            <span class="nav-text" v-show="!isCollapsed">Inventory</span>
            <i class="chevron bi bi-chevron-down" :class="{ rotated: activeSection === 'inventory' }"
              v-show="!isCollapsed"></i>
            <div class="nav-indicator"></div>
          </button>
          <Transition name="slide-down">
            <ul v-show="activeSection === 'inventory' && !isCollapsed" class="submenu">
              <li v-for="item in inventoryItems" :key="item.to">
                <RouterLink :to="item.to" class="submenu-link" active-class="active">
                  <div class="submenu-icon-wrapper">
                    <i :class="item.icon"></i>
                  </div>
                  <span>{{ item.label }}</span>
                  <div class="submenu-indicator"></div>
                </RouterLink>
              </li>
            </ul>
          </Transition>
        </li>

        <!-- Finance -->
        <li>
          <button class="nav-link nav-toggle" :class="{ active: activeSection === 'finance' }"
            @click="toggleSection('finance')" :aria-expanded="activeSection === 'finance'">
            <div class="nav-icon-wrapper">
              <i class="nav-icon bi bi-cash-stack"></i>
            </div>
            <span class="nav-text" v-show="!isCollapsed">Finance</span>
            <i class="chevron bi bi-chevron-down" :class="{ rotated: activeSection === 'finance' }"
              v-show="!isCollapsed"></i>
            <div class="nav-indicator"></div>
          </button>
          <Transition name="slide-down">
            <ul v-show="activeSection === 'finance' && !isCollapsed" class="submenu">
              <!-- Chart of Accounts -->
              <li>
                <button class="submenu-link submenu-toggle" :class="{ active: activeSubsection === 'chartOfAccounts' }"
                  @click="toggleSubsection('chartOfAccounts')">
                  <div class="submenu-icon-wrapper">
                    <i class="bi bi-journal-bookmark"></i>
                  </div>
                  <span>Chart of Accounts</span>
                  <i class="chevron bi bi-chevron-down"
                    :class="{ rotated: activeSubsection === 'chartOfAccounts' }"></i>
                  <div class="submenu-indicator"></div>
                </button>
                <Transition name="slide-down">
                  <ul v-show="activeSubsection === 'chartOfAccounts'" class="nested-submenu">
                    <li v-for="item in chartOfAccountsItems" :key="item.to">
                      <RouterLink :to="item.to" class="nested-link" active-class="active">
                        <div class="nested-icon-wrapper">
                          <i :class="item.icon"></i>
                        </div>
                        <span>{{ item.label }}</span>
                        <div class="nested-indicator"></div>
                      </RouterLink>
                    </li>
                  </ul>
                </Transition>
              </li>

              <!-- Journal Entries -->
              <li>
                <button class="submenu-link submenu-toggle" :class="{ active: activeSubsection === 'journalEntries' }"
                  @click="toggleSubsection('journalEntries')">
                  <div class="submenu-icon-wrapper">
                    <i class="bi bi-journal-text"></i>
                  </div>
                  <span>Journal Entries</span>
                  <i class="chevron bi bi-chevron-down" :class="{ rotated: activeSubsection === 'journalEntries' }"></i>
                  <div class="submenu-indicator"></div>
                </button>
                <Transition name="slide-down">
                  <ul v-show="activeSubsection === 'journalEntries'" class="nested-submenu">
                    <li v-for="item in journalEntryItems" :key="item.to">
                      <RouterLink :to="item.to" class="nested-link" active-class="active">
                        <div class="nested-icon-wrapper">
                          <i :class="item.icon"></i>
                        </div>
                        <span>{{ item.label }}</span>
                        <div class="nested-indicator"></div>
                      </RouterLink>
                    </li>
                  </ul>
                </Transition>
              </li>

              <!-- Other Finance Items -->
              <li v-for="item in otherFinanceItems" :key="item.to">
                <RouterLink :to="item.to" class="submenu-link" active-class="active">
                  <div class="submenu-icon-wrapper">
                    <i :class="item.icon"></i>
                  </div>
                  <span>{{ item.label }}</span>
                  <div class="submenu-indicator"></div>
                </RouterLink>
              </li>
            </ul>
          </Transition>
        </li>

        <!-- HRM -->
        <li>
          <button class="nav-link nav-toggle" :class="{ active: activeSection === 'Hrm' }" @click="toggleSection('Hrm')"
            :aria-expanded="activeSection === 'Hrm'">
            <div class="nav-icon-wrapper">
              <i class="nav-icon bi bi-people"></i>
            </div>
            <span class="nav-text" v-show="!isCollapsed">HRM</span>
            <i class="chevron bi bi-chevron-down" :class="{ rotated: activeSection === 'Hrm' }"
              v-show="!isCollapsed"></i>
            <div class="nav-indicator"></div>
          </button>
          <Transition name="slide-down">
            <ul v-show="activeSection === 'Hrm' && !isCollapsed" class="submenu">
              <li v-for="item in Hrm" :key="item.to">
                <RouterLink :to="item.to" class="submenu-link" active-class="active">
                  <div class="submenu-icon-wrapper">
                    <i :class="item.icon"></i>
                  </div>
                  <span>{{ item.label }}</span>
                  <div class="submenu-indicator"></div>
                </RouterLink>
              </li>
            </ul>
          </Transition>
        </li>

        <!-- Reports -->
        <li>
          <RouterLink to="/reports" class="nav-link" active-class="active">
            <div class="nav-icon-wrapper">
              <i class="nav-icon bi bi-graph-up"></i>
            </div>
            <span class="nav-text" v-show="!isCollapsed">Reports</span>
            <div class="nav-indicator"></div>
          </RouterLink>
        </li>
      </ul>
    </nav>
  </aside>
</template>

<script>
export default {
  name: 'Sidebar',
  emits: ['toggle-collapse'],
  props: {
    isCollapsed: {
      type: Boolean,
      default: false
    }
  },
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
        { to: '/dashboard/returns', label: 'Returns', icon: 'bi bi-arrow-return-left' }
      ],
      Hrm: [
        { to: '/dashboard/employees', label: 'Employees', icon: 'bi bi-person' },
        { to: '/dashboard/departments', label: 'Departments', icon: 'bi bi-building' },
        { to: '/dashboard/attendance', label: 'Attendance', icon: 'bi bi-calendar-check' },
        { to: '/dashboard/leaves', label: 'Leaves', icon: 'bi bi-calendar-minus' },
        { to: '/dashboard/salaries', label: 'Salaries', icon: 'bi bi-cash-stack' },
        { to: '/dashboard/performance-reviews', label: 'Performance Reviews', icon: 'bi bi-star' }
      ],
      chartOfAccountsItems: [
        { to: '/dashboard/AccountList', label: 'Account Types', icon: 'bi bi-journal-bookmark' },
        { to: '/dashboard/Accounts', label: 'Accounts', icon: 'bi bi-journal-text' }
      ],
      journalEntryItems: [
        { to: '/dashboard/JournalEntry', label: 'Journal Entries', icon: 'bi bi-journal' },
        { to: '/dashboard/JournalEntryLine', label: 'Journal Entry Lines', icon: 'bi bi-journal-plus' }
      ],
      otherFinanceItems: [
        { to: '/dashboard/Expense', label: 'Expenses', icon: 'bi bi-wallet2' },
        { to: '/dashboard/FinancialPeriod', label: 'Financial Periods', icon: 'bi bi-calendar-range' }
      ]
    }
  },
  methods: {
    toggleCollapse() {
      this.$emit('toggle-collapse');
    },
    toggleSection(section) {
      this.activeSection = this.activeSection === section ? null : section
      if (this.activeSection !== section) {
        this.activeSubsection = null
      }
    },
    toggleSubsection(subsection) {
      this.activeSubsection = this.activeSubsection === subsection ? null : subsection
    }
  }
}
</script>

<style scoped>
.sidebar {
  width: 280px;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  background: #ffffff;
  border-right: 1px solid rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  z-index: 1010;
  /* Increased from 100 to 1010 */
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 4px 0 24px rgba(0, 0, 0, 0.06);
  padding-top: 64px;
  /* Added to account for topnav height */
}

.sidebar-collapsed {
  width: 80px;
}

.sidebar-header {
  position: fixed;
  top: 0;
  left: 0;
  width: inherit;
  z-index: 1030;
  /* Higher than topnav */
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 20px;
  height: 64px;
  /* Match topnav height */
  background: #ffffff;
  border-bottom: 1px solid rgba(0, 0, 0, 0.1);
  transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.sidebar-collapsed .sidebar-header {
  width: 80px;
}

.sidebar-nav {
  flex: 1;
  overflow-y: auto;
  padding: 16px 12px;
  height: calc(100vh - 64px);
  /* Account for header */
  margin-top: 64px;
  /* Push content below fixed header */
}

/* Rest of your existing styles remain the same */
.sidebar-collapsed .logo-text,
.sidebar-collapsed .nav-text,
.sidebar-collapsed .chevron {
  opacity: 0;
  pointer-events: none;
}

.sidebar-collapsed .nav-link,
.sidebar-collapsed .nav-toggle {
  justify-content: center;
  padding: 12px;
}

.sidebar-collapsed .nav-icon-wrapper {
  margin: 0;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-icon {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
  color: white;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
  box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
}

.logo-text {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1e293b;
  transition: opacity 0.3s ease;
}

.collapse-btn {
  background: rgba(255, 255, 255, 0.6);
  border: 1px solid rgba(0, 0, 0, 0.1);
  color: #64748b;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
}

.collapse-btn:hover {
  background: rgba(0, 0, 0, 0.05);
  color: #4f46e5;
}

.nav-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.nav-link,
.nav-toggle {
  display: flex;
  align-items: center;
  gap: 12px;
  width: 100%;
  padding: 12px 16px;
  border-radius: 8px;
  background: transparent;
  color: #64748b;
  font-size: 0.875rem;
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  position: relative;
}

.nav-link:hover,
.nav-toggle:hover {
  background: rgba(79, 70, 229, 0.05);
  color: #4f46e5;
}

.nav-link.active,
.nav-toggle.active {
  background: rgba(79, 70, 229, 0.1);
  color: #4f46e5;
  font-weight: 600;
}

.nav-link.active .nav-indicator,
.nav-toggle.active .nav-indicator {
  opacity: 1;
}

.nav-icon-wrapper {
  width: 24px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nav-icon {
  font-size: 1.1rem;
  transition: all 0.3s ease;
}

.nav-text {
  flex: 1;
  transition: opacity 0.3s ease;
}

.nav-indicator {
  position: absolute;
  left: 0;
  top: 50%;
  transform: translateY(-50%);
  width: 3px;
  height: 24px;
  background: #4f46e5;
  border-radius: 0 2px 2px 0;
  opacity: 0;
  transition: all 0.3s ease;
}

.chevron {
  margin-left: auto;
  font-size: 12px;
  transition: all 0.3s ease;
  opacity: 0.6;
}

.chevron.rotated {
  transform: rotate(180deg);
  opacity: 1;
}

.submenu {
  list-style: none;
  margin: 8px 0 0 0;
  padding: 0;
  border-left: 2px solid rgba(79, 70, 229, 0.1);
  margin-left: 20px;
  overflow: hidden;
}

.submenu-link,
.submenu-toggle {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px 16px;
  color: #64748b;
  border-radius: 8px;
  font-size: 0.8125rem;
  font-weight: 500;
  background: transparent;
  border: none;
  width: 100%;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  position: relative;
}

.submenu-link:hover,
.submenu-toggle:hover {
  background: rgba(79, 70, 229, 0.05);
  color: #4f46e5;
}

.submenu-link.active,
.submenu-toggle.active {
  background: rgba(79, 70, 229, 0.08);
  color: #4f46e5;
  font-weight: 600;
}

.submenu-link.active .submenu-indicator,
.submenu-toggle.active .submenu-indicator {
  opacity: 1;
}

.submenu-icon-wrapper {
  width: 20px;
  height: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.submenu-indicator {
  position: absolute;
  left: -2px;
  top: 50%;
  transform: translateY(-50%);
  width: 2px;
  height: 16px;
  background: #4f46e5;
  border-radius: 1px;
  opacity: 0;
  transition: all 0.3s ease;
}

.nested-submenu {
  list-style: none;
  margin: 6px 0 0 0;
  padding: 0;
  border-left: 2px solid rgba(79, 70, 229, 0.08);
  margin-left: 16px;
}

.nested-link {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 8px 14px;
  color: #64748b;
  border-radius: 6px;
  font-size: 0.8125rem;
  font-weight: 500;
  background: transparent;
  text-decoration: none;
  transition: all 0.3s ease;
  position: relative;
}

.nested-link:hover {
  background: rgba(79, 70, 229, 0.05);
  color: #4f46e5;
}

.nested-link.active {
  background: rgba(79, 70, 229, 0.06);
  color: #4f46e5;
  font-weight: 600;
}

.nested-link.active .nested-indicator {
  opacity: 1;
}

.nested-icon-wrapper {
  width: 16px;
  height: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.nested-indicator {
  position: absolute;
  left: -2px;
  top: 50%;
  transform: translateY(-50%);
  width: 2px;
  height: 12px;
  background: #4f46e5;
  border-radius: 1px;
  opacity: 0;
  transition: all 0.3s ease;
}

.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
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

.dark-mode .sidebar {
  background: #1e293b;
  border-right-color: rgba(255, 255, 255, 0.1);
}

.dark-mode .sidebar-header {
  border-bottom-color: rgba(255, 255, 255, 0.1);
}

.dark-mode .logo-text {
  color: #f8fafc;
}

.dark-mode .nav-link,
.dark-mode .nav-toggle,
.dark-mode .submenu-link,
.dark-mode .submenu-toggle,
.dark-mode .nested-link {
  color: #94a3b8;
}

.dark-mode .nav-link:hover,
.dark-mode .nav-toggle:hover,
.dark-mode .submenu-link:hover,
.dark-mode .submenu-toggle:hover,
.dark-mode .nested-link:hover {
  background: rgba(255, 255, 255, 0.05);
  color: #a5b4fc;
}

.dark-mode .collapse-btn {
  background: rgba(15, 23, 42, 0.8);
  border-color: rgba(148, 163, 184, 0.1);
  color: #94a3b8;
}

.dark-mode .collapse-btn:hover {
  background: rgba(15, 23, 42, 0.9);
  color: #e2e8f0;
}

@media (max-width: 1024px) {
  .sidebar {
    transform: translateX(-100%);
    z-index: 1050;
    /* Higher on mobile */
    padding-top: 0;
  }

  .sidebar.show {
    transform: translateX(0);
  }

  .sidebar-header {
    top: 0;
  }

  .sidebar-nav {
    height: 100vh;
    margin-top: 0;
  }

  .sidebar-collapsed {
    width: 280px;
  }

  .sidebar-collapsed .logo-text,
  .sidebar-collapsed .nav-text,
  .sidebar-collapsed .chevron {
    opacity: 1;
    pointer-events: auto;
  }

  .sidebar-collapsed .nav-link,
  .sidebar-collapsed .nav-toggle {
    justify-content: flex-start;
    padding: 12px 16px;
  }

  .sidebar-collapsed .nav-icon-wrapper {
    margin-right: 12px;
  }
}

@media (max-width: 768px) {
  .sidebar {
    width: 280px;
  }

  .sidebar-header {
    padding: 0 16px;
  }

  .sidebar-nav {
    padding: 12px 8px;
  }
}
</style>