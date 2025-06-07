<template>
  <aside class="sidebar" :class="{ 'sidebar-collapsed': isCollapsed }">
    <!-- Header -->
    <div class="sidebar-header">
      <div class="header-content">
        <div class="logo-section">
          <div class="logo-icon">
            <i class="bi bi-grid-3x3-gap-fill"></i>
          </div>
          <h2 class="logo-text">Dashboard</h2>
        </div>
        <button class="collapse-btn d-lg-none" @click="$emit('toggle-collapse')" aria-label="Close sidebar">
          <i class="bi bi-x-lg"></i>
        </button>
      </div>
    </div>

    <!-- Navigation Menu -->
    <nav class="sidebar-nav">
      <div class="nav-section">
        <!-- Main Navigation -->
        <ul class="nav-list">
          <!-- Home -->
          <li class="nav-item">
            <RouterLink to="/dashboard" class="nav-link" active-class="active" exact-active-class="exact-active">
              <div class="nav-link-content">
                <i class="nav-icon bi bi-house-door"></i>
                <span class="nav-text">Home</span>
              </div>
            </RouterLink>
          </li>

          <!-- Inventory Section -->
          <li class="nav-item">
            <button class="nav-link nav-toggle" :class="{ 'active': activeSection === 'inventory' }"
              @click="toggleSection('inventory')" :aria-expanded="activeSection === 'inventory'">
              <div class="nav-link-content">
                <i class="nav-icon bi bi-box-seam"></i>
                <span class="nav-text">Inventory</span>
                <i class="nav-chevron bi bi-chevron-down" :class="{ 'rotated': activeSection === 'inventory' }"></i>
              </div>
            </button>

            <Transition name="submenu">
              <ul v-show="activeSection === 'inventory'" class="submenu">
                <li class="submenu-item" v-for="item in inventoryItems" :key="item.to">
                  <RouterLink :to="item.to" class="submenu-link" active-class="active">
                    <i class="submenu-icon" :class="item.icon"></i>
                    <span class="submenu-text">{{ item.label }}</span>
                  </RouterLink>
                </li>
              </ul>
            </Transition>
          </li>

          <!-- Finance Section -->
          <li class="nav-item">
            <button class="nav-link nav-toggle" :class="{ 'active': activeSection === 'finance' }"
              @click="toggleSection('finance')" :aria-expanded="activeSection === 'finance'">
              <div class="nav-link-content">
                <i class="nav-icon bi bi-cash-stack"></i>
                <span class="nav-text">Finance</span>
                <i class="nav-chevron bi bi-chevron-down" :class="{ 'rotated': activeSection === 'finance' }"></i>
              </div>
            </button>

            <Transition name="submenu">
              <ul v-show="activeSection === 'finance'" class="submenu">
                <!-- Chart of Accounts -->
                <li class="submenu-item">
                  <button class="submenu-link submenu-toggle"
                    :class="{ 'active': activeSubsection === 'chartOfAccounts' }"
                    @click="toggleSubsection('chartOfAccounts')">
                    <i class="submenu-icon bi bi-journal-bookmark"></i>
                    <span class="submenu-text">Chart of Accounts</span>
                    <i class="submenu-chevron bi bi-chevron-down"
                      :class="{ 'rotated': activeSubsection === 'chartOfAccounts' }"></i>
                  </button>

                  <Transition name="nested-submenu">
                    <ul v-show="activeSubsection === 'chartOfAccounts'" class="nested-submenu">
                      <li v-for="item in chartOfAccountsItems" :key="item.to">
                        <RouterLink :to="item.to" class="nested-link" active-class="active">
                          <i :class="item.icon"></i>
                          <span>{{ item.label }}</span>
                        </RouterLink>
                      </li>
                    </ul>
                  </Transition>
                </li>

                <!-- Journal Entries -->
                <li class="submenu-item">
                  <button class="submenu-link submenu-toggle"
                    :class="{ 'active': activeSubsection === 'journalEntries' }"
                    @click="toggleSubsection('journalEntries')">
                    <i class="submenu-icon bi bi-journal-text"></i>
                    <span class="submenu-text">Journal Entries</span>
                    <i class="submenu-chevron bi bi-chevron-down"
                      :class="{ 'rotated': activeSubsection === 'journalEntries' }"></i>
                  </button>

                  <Transition name="nested-submenu">
                    <ul v-show="activeSubsection === 'journalEntries'" class="nested-submenu">
                      <li v-for="item in journalEntryItems" :key="item.to">
                        <RouterLink :to="item.to" class="nested-link" active-class="active">
                          <i :class="item.icon"></i>
                          <span>{{ item.label }}</span>
                        </RouterLink>
                      </li>
                    </ul>
                  </Transition>
                </li>

                <!-- Supplier Transactions -->
                <li class="submenu-item">
                  <button class="submenu-link submenu-toggle"
                    :class="{ 'active': activeSubsection === 'supplierTransactions' }"
                    @click="toggleSubsection('supplierTransactions')">
                    <i class="submenu-icon bi bi-truck"></i>
                    <span class="submenu-text">Supplier Transactions</span>
                    <i class="submenu-chevron bi bi-chevron-down"
                      :class="{ 'rotated': activeSubsection === 'supplierTransactions' }"></i>
                  </button>

                  <Transition name="nested-submenu">
                    <ul v-show="activeSubsection === 'supplierTransactions'" class="nested-submenu">
                      <li v-for="item in supplierTransactionItems" :key="item.to">
                        <RouterLink :to="item.to" class="nested-link" active-class="active">
                          <i :class="item.icon"></i>
                          <span>{{ item.label }}</span>
                        </RouterLink>
                      </li>
                    </ul>
                  </Transition>
                </li>

                <!-- Customer Transactions -->
                <li class="submenu-item">
                  <button class="submenu-link submenu-toggle"
                    :class="{ 'active': activeSubsection === 'customerTransactions' }"
                    @click="toggleSubsection('customerTransactions')">
                    <i class="submenu-icon bi bi-people"></i>
                    <span class="submenu-text">Customer Transactions</span>
                    <i class="submenu-chevron bi bi-chevron-down"
                      :class="{ 'rotated': activeSubsection === 'customerTransactions' }"></i>
                  </button>

                  <Transition name="nested-submenu">
                    <ul v-show="activeSubsection === 'customerTransactions'" class="nested-submenu">
                      <li v-for="item in customerTransactionItems" :key="item.to">
                        <RouterLink :to="item.to" class="nested-link" active-class="active">
                          <i :class="item.icon"></i>
                          <span>{{ item.label }}</span>
                        </RouterLink>
                      </li>
                    </ul>
                  </Transition>
                </li>

                <!-- Other Finance Items -->
                <li class="submenu-item" v-for="item in otherFinanceItems" :key="item.to">
                  <RouterLink :to="item.to" class="submenu-link" active-class="active">
                    <i class="submenu-icon" :class="item.icon"></i>
                    <span class="submenu-text">{{ item.label }}</span>
                  </RouterLink>
                </li>
              </ul>
            </Transition>
          </li>

          <!-- Other Menu Items -->
          <li class="nav-item" v-for="item in menuItems" :key="item.to">
            <RouterLink :to="item.to" class="nav-link" active-class="active">
              <div class="nav-link-content">
                <i class="nav-icon" :class="item.icon"></i>
                <span class="nav-text">{{ item.label }}</span>
              </div>
            </RouterLink>
          </li>
        </ul>
      </div>
    </nav>

    <!-- User Profile Section -->
    <div class="user-section">
      <div class="user-profile">
        <div class="user-avatar">
          <img src="https://via.placeholder.com/40" alt="User Avatar" />
        </div>
        <div class="user-info">
          <div class="user-name">John Doe</div>
          <div class="user-role">Administrator</div>
        </div>
        <button class="user-menu-btn" aria-label="User menu">
          <i class="bi bi-three-dots-vertical"></i>
        </button>
      </div>
    </div>
  </aside>
</template>

<script>
export default {
  name: 'ModernSidebar',
  emits: ['toggle-collapse'],
  data() {
    return {
      isCollapsed: false,
      activeSection: null,
      activeSubsection: null,
      inventoryItems: [
        { to: '/dashboard/products', label: 'Products', icon: 'bi bi-box' },
        { to: '/dashboard/categories', label: 'Categories', icon: 'bi bi-tags' },
        { to: '/dashboard/brands', label: 'Brands', icon: 'bi bi-star' },
        { to: '/dashboard/suppliers', label: 'Suppliers', icon: 'bi bi-truck' },
        { to: '/dashboard/customers', label: 'Customers', icon: 'bi bi-people' },
        { to: '/dashboard/units', label: 'Units', icon: 'bi bi-rulers' },
        { to: '/dashboard/stock', label: 'Stock', icon: 'bi bi-clipboard-data' },
        { to: '/dashboard/purchases', label: 'Purchases', icon: 'bi bi-cart-plus' },
        { to: '/dashboard/sales', label: 'Sales', icon: 'bi bi-cart-check' },
        { to: '/dashboard/returns', label: 'Returns', icon: 'bi bi-arrow-return-left' }
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
      ],
      menuItems: [
        { to: '/reports', label: 'Reports', icon: 'bi bi-graph-up' },
        { to: '/settings', label: 'Settings', icon: 'bi bi-gear' }
      ]
    }
  },
  methods: {
    toggleSection(section) {
      this.activeSection = this.activeSection === section ? null : section
      // Reset subsection when changing main section
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
/* Main Sidebar */
.sidebar {
  width: 280px;
  height: 100vh;
  position: fixed;
  top: 8;
  left: 0;
  background: linear-gradient(135deg, #0d6efd 0%, #0b5ed7 100%);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
  display: flex;
  flex-direction: column;
  z-index: 1030;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: hidden;
}


/* Header Section */
.sidebar-header {
  padding: 1.5rem 1.25rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.1);
  flex-shrink: 0;
}

.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.logo-icon {
  width: 2.5rem;
  height: 2.5rem;
  background: rgba(255, 255, 255, 0.15);
  border-radius: 0.75rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  color: #ffffff;
}

.logo-text {
  font-size: 1.375rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0;
  letter-spacing: -0.025em;
}

.collapse-btn {
  width: 2rem;
  height: 2rem;
  border: 1px solid rgba(255, 255, 255, 0.1);
  background: transparent;
  color: #ffffff;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.collapse-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: rgba(255, 255, 255, 0.2);
}

/* Navigation */
.sidebar-nav {
  flex: 1;
  overflow-y: auto;
  overflow-x: hidden;
  padding: 1rem 0;
}

.sidebar-nav::-webkit-scrollbar {
  width: 4px;
}

.sidebar-nav::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.05);
}

.sidebar-nav::-webkit-scrollbar-thumb {
  background: rgba(255, 255, 255, 0.2);
  border-radius: 2px;
}

.nav-section {
  padding: 0 1.25rem;
}

.nav-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.nav-item {
  position: relative;
}

/* Navigation Links */
.nav-link,
.nav-toggle {
  display: block;
  width: 100%;
  text-decoration: none;
  color: rgba(255, 255, 255, 0.8);
  padding: 0.75rem 1rem;
  border-radius: 0.75rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: none;
  background: transparent;
  cursor: pointer;
  font-size: 0.875rem;
  font-weight: 500;
}

.nav-link-content {
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.nav-icon {
  font-size: 1.125rem;
  width: 1.25rem;
  text-align: center;
  flex-shrink: 0;
}

.nav-text {
  flex: 1;
  text-align: left;
}

.nav-chevron {
  font-size: 0.875rem;
  transition: transform 0.3s ease;
  flex-shrink: 0;
}

.nav-chevron.rotated {
  transform: rotate(180deg);
}

/* Hover and Active States */
.nav-link:hover:not(.active),
.nav-toggle:hover:not(.active) {
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
  transform: translateX(2px);
}

.nav-link.active,
.nav-toggle.active {
  background: rgba(255, 255, 255, 0.2);
  color: #ffffff;
  font-weight: 600;
}

/* Submenu Styles */
.submenu {
  list-style: none;
  margin: 0.5rem 0 0 0;
  padding: 0;
  overflow: hidden;
}

.submenu-item {
  margin-bottom: 0.125rem;
}

.submenu-link,
.submenu-toggle {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.625rem 1rem 0.625rem 2.75rem;
  color: rgba(255, 255, 255, 0.6);
  text-decoration: none;
  border-radius: 0.5rem;
  font-size: 0.813rem;
  font-weight: 500;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: none;
  background: transparent;
  width: 100%;
  cursor: pointer;
}

.submenu-icon {
  font-size: 1rem;
  width: 1rem;
  text-align: center;
  flex-shrink: 0;
}

.submenu-text {
  flex: 1;
  text-align: left;
}

.submenu-chevron {
  font-size: 0.75rem;
  transition: transform 0.3s ease;
  flex-shrink: 0;
}

.submenu-chevron.rotated {
  transform: rotate(180deg);
}

.submenu-link:hover:not(.active),
.submenu-toggle:hover:not(.active) {
  background: rgba(255, 255, 255, 0.08);
  color: rgba(255, 255, 255, 0.8);
}

.submenu-link.active,
.submenu-toggle.active {
  background: rgba(255, 255, 255, 0.15);
  color: #ffffff;
  font-weight: 600;
}

/* Nested Submenu */
.nested-submenu {
  list-style: none;
  margin: 0.25rem 0 0 0;
  padding: 0;
}

.nested-link {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem 0.5rem 4rem;
  color: rgba(255, 255, 255, 0.6);
  text-decoration: none;
  border-radius: 0.375rem;
  font-size: 0.75rem;
  font-weight: 500;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.nested-link i {
  font-size: 0.875rem;
  width: 0.875rem;
  text-align: center;
}

.nested-link:hover:not(.active) {
  background: rgba(255, 255, 255, 0.06);
  color: rgba(255, 255, 255, 0.8);
}

.nested-link.active {
  background: rgba(255, 255, 255, 0.12);
  color: #ffffff;
  font-weight: 600;
}

/* User Section */
.user-section {
  padding: 1.25rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  flex-shrink: 0;
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.75rem;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 0.75rem;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.user-profile:hover {
  background: rgba(255, 255, 255, 0.12);
}

.user-avatar {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
  border: 2px solid rgba(255, 255, 255, 0.2);
}

.user-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.user-info {
  flex: 1;
  min-width: 0;
}

.user-name {
  font-size: 0.875rem;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 0.125rem;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.user-role {
  font-size: 0.75rem;
  color: rgba(255, 255, 255, 0.6);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.user-menu-btn {
  width: 1.75rem;
  height: 1.75rem;
  border: none;
  background: transparent;
  color: rgba(255, 255, 255, 0.8);
  border-radius: 0.375rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  flex-shrink: 0;
}

.user-menu-btn:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
}

/* Transitions */
.submenu-enter-active,
.submenu-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: top;
}

.submenu-enter-from,
.submenu-leave-to {
  opacity: 0;
  transform: translateY(-8px) scaleY(0.8);
}

.nested-submenu-enter-active,
.nested-submenu-leave-active {
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: top;
}

.nested-submenu-enter-from,
.nested-submenu-leave-to {
  opacity: 0;
  transform: translateY(-4px) scaleY(0.9);
}

/* Responsive Design */
@media (max-width: 992px) {
  .sidebar {
    transform: translateX(-100%);
  }

  .sidebar.show {
    transform: translateX(0);
  }
}

@media (max-width: 576px) {
  .sidebar {
    width: 100vw;
  }

  .logo-text {
    font-size: 1.25rem;
  }

  .nav-section {
    padding: 0 1rem;
  }
}

/* Focus styles for accessibility */
.nav-link:focus-visible,
.nav-toggle:focus-visible,
.submenu-link:focus-visible,
.submenu-toggle:focus-visible,
.nested-link:focus-visible {
  outline: 2px solid rgba(255, 255, 255, 0.5);
  outline-offset: 2px;
}

/* High contrast mode support */
@media (prefers-contrast: high) {
  .sidebar {
    border-right: 2px solid rgba(255, 255, 255, 0.3);
  }

  .sidebar-header {
    border-bottom-color: rgba(255, 255, 255, 0.3);
  }

  .user-section {
    border-top-color: rgba(255, 255, 255, 0.3);
  }

  .nav-link:hover:not(.active),
  .nav-toggle:hover:not(.active) {
    background: rgba(255, 255, 255, 0.2);
  }

  .nav-link.active,
  .nav-toggle.active {
    background: rgba(255, 255, 255, 0.3);
  }
}

/* Reduced motion support */
@media (prefers-reduced-motion: reduce) {
  * {
    transition: none !important;
    animation: none !important;
  }
}
</style>