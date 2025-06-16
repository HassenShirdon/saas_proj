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
        component: () => import('@/views/inventory/items.vue'),
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
        path: '/dashboard/products',
        name: 'productList',
        component: () => import('@/views/inventory/items.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/purchaseOrders',
        name: 'purchaseOrders',
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
    ],
  },
  {
    path: '/signin',
    name: 'signin',
    component: import('@/views/Auth/loginView.vue'),
    meta: { requiresGuest: true },
  },
  {
    path: '/sign-up',
    name: 'signup',
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
    next('/signin')
  } else if (to.meta.requiresGuest && auth.isAuthenticated) {
    next('/dashboard')
  } else {
    next()
  }
})
export default router
