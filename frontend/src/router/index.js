// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'

const routes = [
  {
    path: '/',
    name: 'landing',
    component: import('@/views/Landing/landingPage.vue'),
  },
  {
    path: '/superDashboard',
    name: 'superDashboard',
    component: import('@/views/Dashboard/superDashboard.vue'),
  },
  {
    path: '/tenantAdmin',
    name: 'tenantAdmin',
    component: import('@/views/Dashboard/tenantAdmin.vue'),
  },

  {
    path: '/dashboard',
    name: 'dashboard',
    component: import('@/views/Dashboard/dashboardPage.vue'),
    meta: { requiresAuth: true },
    children: [
      {
        path: '/dashboard/customers',
        name: 'customers',
        component: () => import('@/views/inventory/CustomerList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/departments',
        name: 'departments',
        component: () => import('@/views/hrm/departmentList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/products',
        name: 'products',
        component: () => import('@/views/inventory/ProductList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/inventory-items',
        name: 'inventory-items',
        component: () => import('@/views/inventory/ItemList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/reports',
        name: 'reports',
        component: () => import('@/views/reports.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/sales',
        name: 'sales',
        component: () => import('@/views/inventory/sales.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/returns',
        name: 'returns',
        component: () => import('@/views/inventory/returnList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/suppliers',
        name: 'suppliers',
        component: () => import('@/views/inventory/SupplierList.vue'),
        meta: { requiresAuth: true },
      },
      // other dashboard routes can go here
      {
        path: '/dashboard/categories',
        name: 'categories',
        component: () => import('@/views/inventory/productCategory.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/purchase-orders',
        name: 'purchase-orders',
        component: () => import('@/views/inventory/purchaseOrderList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/stock-movement',
        name: 'stockMovement',
        component: () => import('@/views/inventory/stockMovement.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/employees',
        name: 'employees',
        component: () => import('@/views/hrm/employeeList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/attendance',
        name: 'attendance',
        component: () => import('@/views/hrm/attendanceList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/leaves',
        name: 'leaves',
        component: () => import('@/views/hrm/leavesList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/salaries',
        name: 'salaries',
        component: () => import('@/views/hrm/salariesList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/performance-reviews',
        name: 'performanceReviews',
        component: () => import('@/views/hrm/performanceReviewsList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/accounts',
        name: 'accounts',
        component: () => import('@/views/finance/accountList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/expenses',
        name: 'expenses',
        component: () => import('@/views/finance/expenseList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/journal-entries',
        name: 'journalEntries',
        component: () => import('@/views/finance/journalEntryList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/financial-periods',
        name: 'FinancialPeriod',
        component: () => import('@/views/finance/financialPeriods.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/journal-entry-lines',
        name: 'journalEntryLines',
        component: () => import('@/views/finance/journalEntryLineList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/account-types',
        name: 'AccountTypes',
        component: () => import('@/views/finance/accountTypesList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/supplier-invoices',
        name: 'supplierInvoices',
        component: () => import('@/views/finance/supplierInvoiceList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/customer-invoices',
        name: 'customerInvoices',
        component: () => import('@/views/finance/customerInvoiceList.vue'),
        meta: { requiresAuth: true },
      },
    ],
  },
  {
    path: '/login',
    name: 'login',
    component: import('@/views/Auth/loginView.vue'),
    meta: { requiresGuest: true },
  },
  {
    path: '/register',
    name: 'register',
    component: import('@/views/Auth/register.vue'),
    meta: { requiresGuest: true },
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})
router.beforeEach((to, from, next) => {
  const auth = useAuthStore()

  if (to.meta.requiresAuth && !auth.isAuthenticated) {
    next('/login')
  } else if (to.meta.requiresGuest && auth.isAuthenticated) {
    next('/dashboard')
  } else {
    next()
  }
})
export default router
