<template>
  <aside class="sidebar" :class="{ 'sidebar-collapsed': isCollapsed }">
    <!-- Header -->
    <div class="sidebar-header">
      <div class="logo-section">
        <span class="logo-icon">
          <i class="bi bi-grid-3x3-gap-fill"></i>
        </span>
        <span class="logo-text">Dashboard</span>
      </div>
      <button class="collapse-btn d-lg-none" @click="$emit('toggle-collapse')" aria-label="Close sidebar">
        <i class="bi bi-x-lg"></i>
      </button>
    </div>

    <!-- Navigation -->
    <nav class="sidebar-nav">
      <ul class="nav-list">
        <!-- Home -->
        <li>
          <RouterLink to="/dashboard" class="nav-link" active-class="active" exact-active-class="exact-active">
            <i class="nav-icon bi bi-house-door"></i>
            <span>Home</span>
          </RouterLink>
        </li>

        <!-- Inventory -->
        <li>
          <button class="nav-link nav-toggle" :class="{ active: activeSection === 'inventory' }"
            @click="toggleSection('inventory')" :aria-expanded="activeSection === 'inventory'">
            <i class="nav-icon bi bi-box-seam"></i>
            <span>Inventory</span>
            <i class="bi bi-chevron-down chevron" :class="{ rotated: activeSection === 'inventory' }"></i>
          </button>
          <Transition name="submenu">
            <ul v-show="activeSection === 'inventory'" class="submenu">
              <li v-for="item in inventoryItems" :key="item.to">
                <RouterLink :to="item.to" class="submenu-link" active-class="active">
                  <i :class="item.icon"></i>
                  <span>{{ item.label }}</span>
                </RouterLink>
              </li>
            </ul>
          </Transition>
        </li>

        <!-- Finance -->
        <li>
          <button class="nav-link nav-toggle" :class="{ active: activeSection === 'finance' }"
            @click="toggleSection('finance')" :aria-expanded="activeSection === 'finance'">
            <i class="nav-icon bi bi-cash-stack"></i>
            <span>Finance</span>
            <i class="bi bi-chevron-down chevron" :class="{ rotated: activeSection === 'finance' }"></i>
          </button>
          <Transition name="submenu">
            <ul v-show="activeSection === 'finance'" class="submenu">
              <!-- Chart of Accounts -->
              <li>
                <button class="submenu-link submenu-toggle" :class="{ active: activeSubsection === 'chartOfAccounts' }"
                  @click="toggleSubsection('chartOfAccounts')">
                  <i class="bi bi-journal-bookmark"></i>
                  <span>Chart of Accounts</span>
                  <i class="bi bi-chevron-down chevron"
                    :class="{ rotated: activeSubsection === 'chartOfAccounts' }"></i>
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
              <li>
                <button class="submenu-link submenu-toggle" :class="{ active: activeSubsection === 'journalEntries' }"
                  @click="toggleSubsection('journalEntries')">
                  <i class="bi bi-journal-text"></i>
                  <span>Journal Entries</span>
                  <i class="bi bi-chevron-down chevron" :class="{ rotated: activeSubsection === 'journalEntries' }"></i>
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
              <li>
                <button class="submenu-link submenu-toggle"
                  :class="{ active: activeSubsection === 'supplierTransactions' }"
                  @click="toggleSubsection('supplierTransactions')">
                  <i class="bi bi-truck"></i>
                  <span>Supplier Transactions</span>
                  <i class="bi bi-chevron-down chevron"
                    :class="{ rotated: activeSubsection === 'supplierTransactions' }"></i>
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
              <li>
                <button class="submenu-link submenu-toggle"
                  :class="{ active: activeSubsection === 'customerTransactions' }"
                  @click="toggleSubsection('customerTransactions')">
                  <i class="bi bi-people"></i>
                  <span>Customer Transactions</span>
                  <i class="bi bi-chevron-down chevron"
                    :class="{ rotated: activeSubsection === 'customerTransactions' }"></i>
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
              <li v-for="item in otherFinanceItems" :key="item.to">
                <RouterLink :to="item.to" class="submenu-link" active-class="active">
                  <i :class="item.icon"></i>
                  <span>{{ item.label }}</span>
                </RouterLink>
              </li>
            </ul>
          </Transition>
        </li>

        <!-- Other Menu Items -->
        <li v-for="item in menuItems" :key="item.to">
          <RouterLink :to="item.to" class="nav-link" active-class="active">
            <i :class="item.icon"></i>
            <span>{{ item.label }}</span>
          </RouterLink>
        </li>
      </ul>
    </nav>

    <!-- User Profile -->
    <div class="user-section">
      <div class="user-profile">
        <img class="user-avatar" src="https://via.placeholder.com/40" alt="User Avatar" />
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
  width: 270px;
  height: 90vh;
  position: fixed;
  top: 7;
  left: 0;
  background: linear-gradient(135deg, #0d6efd 0%, #0b5ed7 100%);
  box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.25);
  display: flex;
  flex-direction: column;
  z-index: 1030;
  border-radius: 1.5rem 0 0 1.5rem;
  overflow: hidden;
  transition: width 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.sidebar-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 2rem 1.5rem 1.5rem 1.5rem;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(255, 255, 255, 0.01);
}

.logo-section {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.logo-icon {
  width: 2.8rem;
  height: 2.8rem;
  background: rgba(255, 255, 255, 0.13);
  border-radius: 1rem;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: #fff;
  box-shadow: 0 2px 8px rgba(13, 110, 253, 0.12);
}

.logo-text {
  font-size: 1.5rem;
  font-weight: 800;
  color: #fff;
  letter-spacing: -0.03em;
  text-shadow: 0 2px 8px rgba(13, 110, 253, 0.08);
}

.collapse-btn {
  background: rgba(255, 255, 255, 0.07);
  border: none;
  color: #fff;
  border-radius: 0.5rem;
  width: 2.2rem;
  height: 2.2rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.2s;
}

.collapse-btn:hover {
  background: rgba(255, 255, 255, 0.18);
}

.sidebar-nav {
  flex: 1;
  overflow-y: auto;
  padding: 1.5rem 0.5rem 1rem 0.5rem;
}

.nav-list {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.nav-link,
.nav-toggle {
  display: flex;
  align-items: center;
  gap: 1rem;
  width: 100%;
  padding: 0.85rem 1.5rem;
  border-radius: 0.9rem;
  background: transparent;
  color: rgba(255, 255, 255, 0.85);
  font-size: 1rem;
  font-weight: 600;
  border: none;
  cursor: pointer;
  transition: background 0.18s, color 0.18s, box-shadow 0.18s;
  box-shadow: none;
  position: relative;
}

.nav-link:hover,
.nav-toggle:hover {
  background: rgba(255, 255, 255, 0.10);
  color: #fff;
  box-shadow: 0 2px 8px rgba(13, 110, 253, 0.08);
}

.nav-link.active,
.nav-toggle.active {
  background: rgba(255, 255, 255, 0.22);
  color: #fff;
  box-shadow: 0 4px 16px rgba(13, 110, 253, 0.10);
}

.nav-icon {
  font-size: 1.25rem;
  width: 1.8rem;
  text-align: center;
  flex-shrink: 0;
}

.chevron {
  margin-left: auto;
  font-size: 1rem;
  transition: transform 0.3s;
}

.chevron.rotated {
  transform: rotate(180deg);
}

.submenu {
  list-style: none;
  margin: 0.25rem 0 0 0;
  padding: 0 0 0 0.5rem;
  border-left: 2px solid rgba(255, 255, 255, 0.08);
  background: transparent;
  border-radius: 0 0 1rem 1rem;
  overflow: hidden;
  transition: background 0.2s;
}

.submenu-link,
.submenu-toggle {
  display: flex;
  align-items: center;
  gap: 0.8rem;
  padding: 0.7rem 1.5rem 0.7rem 2.5rem;
  color: rgba(255, 255, 255, 0.7);
  border-radius: 0.7rem;
  font-size: 0.97rem;
  font-weight: 500;
  background: transparent;
  border: none;
  width: 100%;
  cursor: pointer;
  transition: background 0.18s, color 0.18s;
}

.submenu-link:hover,
.submenu-toggle:hover {
  background: rgba(255, 255, 255, 0.10);
  color: #fff;
}

.submenu-link.active,
.submenu-toggle.active {
  background: rgba(255, 255, 255, 0.18);
  color: #fff;
}

.nested-submenu {
  list-style: none;
  margin: 0.15rem 0 0 0;
  padding: 0 0 0 1.5rem;
  border-left: 2px solid rgba(255, 255, 255, 0.07);
}

.nested-link {
  display: flex;
  align-items: center;
  gap: 0.7rem;
  padding: 0.6rem 1.5rem 0.6rem 3.5rem;
  color: rgba(255, 255, 255, 0.65);
  border-radius: 0.6rem;
  font-size: 0.93rem;
  font-weight: 500;
  background: transparent;
  text-decoration: none;
  transition: background 0.18s, color 0.18s;
}

.nested-link:hover {
  background: rgba(255, 255, 255, 0.09);
  color: #fff;
}

.nested-link.active {
  background: rgba(255, 255, 255, 0.15);
  color: #fff;
}

.user-section {
  padding: 1.5rem 1.5rem 1.5rem 1.5rem;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(255, 255, 255, 0.01);
}

.user-profile {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 1rem;
  background: rgba(255, 255, 255, 0.10);
  border-radius: 1rem;
  box-shadow: 0 2px 8px rgba(13, 110, 253, 0.08);
  transition: background 0.18s;
}

.user-profile:hover {
  background: rgba(255, 255, 255, 0.16);
}

.user-avatar {
  width: 2.7rem;
  height: 2.7rem;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid rgba(255, 255, 255, 0.18);
  box-shadow: 0 2px 8px rgba(13, 110, 253, 0.10);
}

.user-info {
  flex: 1;
  min-width: 0;
}

.user-name {
  font-size: 1.05rem;
  font-weight: 700;
  color: #fff;
  margin-bottom: 0.1rem;
  letter-spacing: -0.01em;
  text-shadow: 0 1px 4px rgba(13, 110, 253, 0.08);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.user-role {
  font-size: 0.93rem;
  color: rgba(255, 255, 255, 0.7);
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.user-menu-btn {
  width: 2rem;
  height: 2rem;
  border: none;
  background: rgba(255, 255, 255, 0.08);
  color: #fff;
  border-radius: 0.5rem;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: background 0.18s;
}

.user-menu-btn:hover {
  background: rgba(255, 255, 255, 0.18);
}

/* Transitions */
.submenu-enter-active,
.submenu-leave-active {
  transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: top;
}

.submenu-enter-from,
.submenu-leave-to {
  opacity: 0;
  transform: translateY(-8px) scaleY(0.8);
}

.nested-submenu-enter-active,
.nested-submenu-leave-active {
  transition: all 0.18s cubic-bezier(0.4, 0, 0.2, 1);
  transform-origin: top;
}

.nested-submenu-enter-from,
.nested-submenu-leave-to {
  opacity: 0;
  transform: translateY(-4px) scaleY(0.9);
}

/* Responsive */
@media (max-width: 992px) {
  .sidebar {
    transform: translateX(-100%);
    border-radius: 0;
  }

  .sidebar.show {
    transform: translateX(0);
  }
}

@media (max-width: 576px) {
  .sidebar {
    width: 100vw;
    border-radius: 0;
  }

  .logo-text {
    font-size: 1.2rem;
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
</style>
