<template>
  <aside class="sidebar bg-white shadow-sm border-end" :class="{ 'sidebar-collapsed': isCollapsed }" :style="{
    width: isCollapsed ? '80px' : '280px',
    minHeight: '100vh',
    position: 'fixed',
    top: 0,
    left: 0,
    zIndex: 100,
    transition: 'width 0.3s cubic-bezier(0.4, 0, 0.2, 1)'
  }">
    <!-- Header -->
    <div class="sidebar-header d-flex align-items-center justify-content-between px-3 py-3 border-bottom">
      <div class="logo-section d-flex align-items-center gap-2">
        <span class="logo-icon d-flex align-items-center justify-content-center bg-primary text-white rounded"
          style="width:32px;height:32px;font-size:1.25rem;">
          <i class="bi bi-grid-3x3-gap-fill"></i>
        </span>
        <span class="logo-text fw-semibold"
          :style="{ opacity: isCollapsed ? 0 : 1, transition: 'opacity 0.3s' }">Dashboard</span>
      </div>
      <button
        class="collapse-btn btn btn-light d-flex align-items-center justify-content-center rounded-circle border-0"
        @click="toggleCollapse" aria-label="Toggle sidebar" style="width:32px;height:32px;">
        <i class="bi" :class="isCollapsed ? 'bi-chevron-right' : 'bi-chevron-left'"></i>
      </button>
    </div>

    <!-- Navigation -->
    <nav class="sidebar-nav flex-grow-1 overflow-auto px-2 py-2">
      <ul class="nav-list list-unstyled d-flex flex-column gap-1">
        <!-- Home -->
        <li>
          <RouterLink to="/dashboard"
            class="nav-link d-flex align-items-center gap-2 px-3 py-2 rounded text-decoration-none"
            active-class="active" exact-active-class="exact-active">
            <i class="nav-icon bi bi-house-door"></i>
            <span class="nav-text" v-show="!isCollapsed">Home</span>
          </RouterLink>
        </li>

        <!-- Inventory -->
        <li>
          <button
            class="nav-link nav-toggle d-flex align-items-center gap-2 px-3 py-2 rounded w-100 border-0 bg-transparent"
            :class="{ active: activeSection === 'inventory' }" @click="toggleSection('inventory')"
            :aria-expanded="activeSection === 'inventory'">
            <i class="nav-icon bi bi-box-seam"></i>
            <span class="nav-text" v-show="!isCollapsed">Inventory</span>
            <i class="bi bi-chevron-down chevron ms-auto" :class="{ rotated: activeSection === 'inventory' }"
              v-show="!isCollapsed"></i>
          </button>
          <Transition name="slide-down">
            <ul v-show="activeSection === 'inventory' && !isCollapsed" class="submenu list-unstyled ms-2">
              <li v-for="item in inventoryItems" :key="item.to">
                <RouterLink :to="item.to"
                  class="submenu-link d-flex align-items-center gap-2 px-3 py-2 rounded text-decoration-none"
                  active-class="active">
                  <i :class="item.icon"></i>
                  <span>{{ item.label }}</span>
                </RouterLink>
              </li>
            </ul>
          </Transition>
        </li>

        <!-- Finance -->
        <li>
          <button
            class="nav-link nav-toggle d-flex align-items-center gap-2 px-3 py-2 rounded w-100 border-0 bg-transparent"
            :class="{ active: activeSection === 'finance' }" @click="toggleSection('finance')"
            :aria-expanded="activeSection === 'finance'">
            <i class="nav-icon bi bi-cash-stack"></i>
            <span class="nav-text" v-show="!isCollapsed">Finance</span>
            <i class="bi bi-chevron-down chevron ms-auto" :class="{ rotated: activeSection === 'finance' }"
              v-show="!isCollapsed"></i>
          </button>
          <Transition name="slide-down">
            <ul v-show="activeSection === 'finance' && !isCollapsed" class="submenu list-unstyled ms-2">
              <!-- Chart of Accounts -->
              <li>
                <button
                  class="submenu-link submenu-toggle d-flex align-items-center gap-2 px-3 py-2 rounded w-100 border-0 bg-transparent"
                  :class="{ active: activeSubsection === 'chartOfAccounts' }"
                  @click="toggleSubsection('chartOfAccounts')">
                  <i class="bi bi-journal-bookmark"></i>
                  <span>Chart of Accounts</span>
                  <i class="bi bi-chevron-down chevron ms-auto"
                    :class="{ rotated: activeSubsection === 'chartOfAccounts' }"></i>
                </button>
                <Transition name="slide-down">
                  <ul v-show="activeSubsection === 'chartOfAccounts'" class="nested-submenu list-unstyled ms-3">
                    <li v-for="item in chartOfAccountsItems" :key="item.to">
                      <RouterLink :to="item.to"
                        class="nested-link d-flex align-items-center gap-2 px-3 py-2 rounded text-decoration-none"
                        active-class="active">
                        <i :class="item.icon"></i>
                        <span>{{ item.label }}</span>
                      </RouterLink>
                    </li>
                  </ul>
                </Transition>
              </li>
              <!-- Journal Entries -->
              <li>
                <button
                  class="submenu-link submenu-toggle d-flex align-items-center gap-2 px-3 py-2 rounded w-100 border-0 bg-transparent"
                  :class="{ active: activeSubsection === 'journalEntries' }"
                  @click="toggleSubsection('journalEntries')">
                  <i class="bi bi-journal-text"></i>
                  <span>Journal Entries</span>
                  <i class="bi bi-chevron-down chevron ms-auto"
                    :class="{ rotated: activeSubsection === 'journalEntries' }"></i>
                </button>
                <Transition name="slide-down">
                  <ul v-show="activeSubsection === 'journalEntries'" class="nested-submenu list-unstyled ms-3">
                    <li v-for="item in journalEntryItems" :key="item.to">
                      <RouterLink :to="item.to"
                        class="nested-link d-flex align-items-center gap-2 px-3 py-2 rounded text-decoration-none"
                        active-class="active">
                        <i :class="item.icon"></i>
                        <span>{{ item.label }}</span>
                      </RouterLink>
                    </li>
                  </ul>
                </Transition>
              </li>
              <!-- Supplier Transactions -->
              <li>
                <button
                  class="submenu-link submenu-toggle d-flex align-items-center gap-2 px-3 py-2 rounded w-100 border-0 bg-transparent"
                  :class="{ active: activeSubsection === 'supplierTransactions' }"
                  @click="toggleSubsection('supplierTransactions')">
                  <i class="bi bi-truck"></i>
                  <span>Supplier Transactions</span>
                  <i class="bi bi-chevron-down chevron ms-auto"
                    :class="{ rotated: activeSubsection === 'supplierTransactions' }"></i>
                </button>
                <Transition name="slide-down">
                  <ul v-show="activeSubsection === 'supplierTransactions'" class="nested-submenu list-unstyled ms-3">
                    <li v-for="item in supplierTransactionItems" :key="item.to">
                      <RouterLink :to="item.to"
                        class="nested-link d-flex align-items-center gap-2 px-3 py-2 rounded text-decoration-none"
                        active-class="active">
                        <i :class="item.icon"></i>
                        <span>{{ item.label }}</span>
                      </RouterLink>
                    </li>
                  </ul>
                </Transition>
              </li>
              <!-- Customer Transactions -->
              <li>
                <button
                  class="submenu-link submenu-toggle d-flex align-items-center gap-2 px-3 py-2 rounded w-100 border-0 bg-transparent"
                  :class="{ active: activeSubsection === 'customerTransactions' }"
                  @click="toggleSubsection('customerTransactions')">
                  <i class="bi bi-people"></i>
                  <span>Customer Transactions</span>
                  <i class="bi bi-chevron-down chevron ms-auto"
                    :class="{ rotated: activeSubsection === 'customerTransactions' }"></i>
                </button>
                <Transition name="slide-down">
                  <ul v-show="activeSubsection === 'customerTransactions'" class="nested-submenu list-unstyled ms-3">
                    <li v-for="item in customerTransactionItems" :key="item.to">
                      <RouterLink :to="item.to"
                        class="nested-link d-flex align-items-center gap-2 px-3 py-2 rounded text-decoration-none"
                        active-class="active">
                        <i :class="item.icon"></i>
                        <span>{{ item.label }}</span>
                      </RouterLink>
                    </li>
                  </ul>
                </Transition>
              </li>
              <!-- Other Finance Items -->
              <li v-for="item in otherFinanceItems" :key="item.to">
                <RouterLink :to="item.to"
                  class="submenu-link d-flex align-items-center gap-2 px-3 py-2 rounded text-decoration-none"
                  active-class="active">
                  <i :class="item.icon"></i>
                  <span>{{ item.label }}</span>
                </RouterLink>
              </li>
            </ul>
          </Transition>
        </li>

        <!-- HRM -->
        <li>
          <button
            class="nav-link nav-toggle d-flex align-items-center gap-2 px-3 py-2 rounded w-100 border-0 bg-transparent"
            :class="{ active: activeSection === 'Hrm' }" @click="toggleSection('Hrm')"
            :aria-expanded="activeSection === 'Hrm'">
            <i class="nav-icon bi bi-people"></i>
            <span class="nav-text" v-show="!isCollapsed">HRM</span>
            <i class="bi bi-chevron-down chevron ms-auto" :class="{ rotated: activeSection === 'Hrm' }"
              v-show="!isCollapsed"></i>
          </button>
          <Transition name="slide-down">
            <ul v-show="activeSection === 'Hrm' && !isCollapsed" class="submenu list-unstyled ms-2">
              <li v-for="item in Hrm" :key="item.to">
                <RouterLink :to="item.to"
                  class="submenu-link d-flex align-items-center gap-2 px-3 py-2 rounded text-decoration-none"
                  active-class="active">
                  <i :class="item.icon"></i>
                  <span>{{ item.label }}</span>
                </RouterLink>
              </li>
            </ul>
          </Transition>
        </li>

        <!-- Reports -->
        <li>
          <RouterLink to="/reports"
            class="nav-link d-flex align-items-center gap-2 px-3 py-2 rounded text-decoration-none"
            active-class="active">
            <i class="nav-icon bi bi-graph-up"></i>
            <span class="nav-text" v-show="!isCollapsed">Reports</span>
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
        { to: '/finance/AccountList', label: 'Account Types', icon: 'bi bi-journal-bookmark' },
        { to: '/finance/Account', label: 'Accounts', icon: 'bi bi-journal-text' }
      ],
      journalEntryItems: [
        { to: '/finance/JournalEntry', label: 'Journal Entries', icon: 'bi bi-journal' },
        { to: '/finance/JournalEntryLine', label: 'Journal Entry Lines', icon: 'bi bi-journal-plus' }
      ],
      supplierTransactionItems: [
        { to: '/finance/SupplierInvoice', label: 'Supplier Invoices', icon: 'bi bi-file-earmark-text' },
        { to: '/finance/SupplierInvoiceLine', label: 'Invoice Lines', icon: 'bi bi-list-ul' },
        { to: '/finance/SupplierPayment', label: 'Supplier Payments', icon: 'bi bi-cash-stack' }
      ],
      customerTransactionItems: [
        { to: '/finance/CustomerInvoice', label: 'Customer Invoices', icon: 'bi bi-receipt' },
        { to: '/finance/CustomerInvoiceLine', label: 'Invoice Lines', icon: 'bi bi-list-check' },
        { to: '/finance/CustomerPayment', label: 'Customer Payments', icon: 'bi bi-credit-card' }
      ],
      otherFinanceItems: [
        { to: '/finance/Expense', label: 'Expenses', icon: 'bi bi-wallet2' },
        { to: '/finance/FinancialPeriod', label: 'Financial Periods', icon: 'bi bi-calendar-range' }
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
* {
  box-sizing: border-box;
  margin: 0;
  font-size: 13px !important;
  text-decoration: none !important;
}

.sidebar {
  width: 280px;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  background-color: #ffffff;
  color: #495057;
  display: flex;
  flex-direction: column;
  z-index: 100;
  border-right: 1px solid #e5e7eb;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  box-shadow: 0 0 1px rgba(0, 0, 0, 0.1);
  text-decoration: none;
  list-style: none;
}

.sidebar-collapsed {
  width: 80px;
}

.sidebar-collapsed .logo-text,
.sidebar-collapsed .nav-text,
.sidebar-collapsed .chevron {
  display: none;
}

.sidebar-collapsed .nav-link,
.sidebar-collapsed .nav-toggle {
  justify-content: center;
  padding: 0.75rem;
}

.sidebar-collapsed .sidebar-nav {
  padding: 0.5rem;
}

.sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1.5rem 1.25rem;
  border-bottom: 1px solid #e5e7eb;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.logo-icon {
  width: 32px;
  height: 32px;
  background: #0d6efd;
  color: white;
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
}

.logo-text {
  font-size: 1.25rem;
  font-weight: 600;
  color: #495057;
  transition: opacity 0.3s;
}

.collapse-btn {
  background: transparent;
  border: none;
  color: #495057;
  width: 32px;
  height: 32px;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 6px;
  cursor: pointer;
  transition: all 0.2s;
}

.collapse-btn:hover {
  background: #f8f9fa;
}

.sidebar-nav {
  flex: 1;
  overflow-y: auto;
  padding: 1rem 0.75rem;
}

.nav-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  text-decoration: none;
}

.nav-link,
.nav-toggle {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  width: 100%;
  padding: 0.75rem 1rem;
  border-radius: 8px;
  background: transparent;
  color: #495057;
  font-size: 0.925rem;
  font-weight: 500;
  border: none;
  cursor: pointer;
  transition: all 0.2s;
  text-decoration: none;

}

.nav-link:hover,
.nav-toggle:hover {
  background: #f8f9fa;
  color: #495057;
}

.nav-link.active,
.nav-toggle.active {
  background: #e9ecef;
  color: #0d6efd;
}

.nav-icon {
  font-size: 1.1rem;
  width: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.chevron {
  margin-left: auto;
  font-size: 0.8rem;
  transition: transform 0.3s;
}

.chevron.rotated {
  transform: rotate(180deg);
}

.submenu {
  list-style: none;
  margin: 0.25rem 0 0 0;
  padding: 0 0 0 1rem;
  border-left: 1px solid #e5e7eb;
}

.submenu-link,
.submenu-toggle {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.65rem 1rem 0.65rem 2.25rem;
  color: #495057;
  border-radius: 6px;
  font-size: 0.875rem;
  font-weight: 500;
  background: transparent;
  border: none;
  width: 100%;
  cursor: pointer;
  transition: all 0.2s;
}

.submenu-link:hover,
.submenu-toggle:hover {
  background: #f8f9fa;
}

.submenu-link.active,
.submenu-toggle.active {
  background: #e9ecef;
  color: #0d6efd;
}

.nested-submenu {
  list-style: none;
  margin: 0.15rem 0 0 0;
  padding: 0 0 0 1rem;
  border-left: 1px solid #e5e7eb;
}

.nested-link {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.6rem 1rem 0.6rem 3.25rem;
  color: #495057;
  border-radius: 6px;
  font-size: 0.85rem;
  font-weight: 400;
  background: transparent;
  text-decoration: none;
  transition: all 0.2s;
}

.nested-link:hover {
  background: #f8f9fa;
}

.nested-link.active {
  background: #e9ecef;
  color: #0d6efd;
}

/* Transitions */
.slide-down-enter-active,
.slide-down-leave-active {
  transition: all 0.25s ease-out;
  overflow: hidden;
}

.slide-down-enter-from,
.slide-down-leave-to {
  max-height: 0;
  opacity: 0;
  transform: translateY(-10px);
}

.slide-down-enter-to,
.slide-down-leave-from {
  max-height: 500px;
  opacity: 1;
  transform: translateY(0);
}

/* Responsive */
@media (max-width: 992px) {
  .sidebar {
    transform: translateX(-100%);
  }

  .sidebar.show {
    transform: translateX(0);
  }

  .sidebar-collapsed {
    width: 280px;
  }

  .sidebar-collapsed .logo-text,
  .sidebar-collapsed .nav-text,
  .sidebar-collapsed .chevron {
    display: inline;
  }

  .sidebar-collapsed .nav-link,
  .sidebar-collapsed .nav-toggle {
    justify-content: flex-start;
    padding: 0.75rem 1rem;
  }
}
</style>