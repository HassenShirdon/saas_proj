// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import { useAuthStore } from '@/stores/authStore'
import LandingPage from '@/views/Landing/landingPage.vue'
import dashboard from '@/views/Dashboard/dashboardPage.vue'
import login from '@/views/Auth/loginView.vue'
import Register from '@/views/Auth/register.vue'

const routes = [
  {
    path: '/',
    name: 'landing',
    component: LandingPage,
  },
  {
    path: '/dashboard',
    name: 'dashboard',
    component: dashboard,
    meta: { requiresAuth: true },
  },
  {
    path: '/signin',
    name: 'signin',
    component: login,
    meta: { requiresGuest: true },
  },
  {
    path: '/sign-up',
    name: 'signup',
    component: Register,
    meta: { requiresGuest: true },
  },

  {
    path: '/dashboard',
    component: dashboard,
    children: [
      {
        path: '/dashboard/customers',
        name: 'customers',
        component: () => import('@/views/inventory/Customers/CustomerList.vue'),
        meta: { requiresAuth: true },
      },
      // {
      //   path: '/dashboard/products',
      //   name: 'ProductList',
      //   component: () => import('@/views/inventory/inentory_Items/items.vue'),
      //   meta: { requiresAuth: true },
      // },
      {
        path: '/dashboard/suppliers',
        name: 'suppliers',
        component: () => import('@/views/inventory/Suppliers/SupplierList.vue'),
        meta: { requiresAuth: true },
      },
      // other dashboard routes can go here
      {
        path: '/dashboard/categories',
        name: 'categories',
        component: () => import('@/views/inventory/productCategory/productCategory.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/products',
        name: 'productList',
        component: () => import('@/views/inventory/inventory_Items/items.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/purchases',
        name: 'purchaseOrders',
        component: () => import('@/views/inventory/purchaseOrder/purchaseOrderList.vue'),
        meta: { requiresAuth: true },
      },
    ],
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
