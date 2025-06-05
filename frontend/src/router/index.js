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
    name: 'login',
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
        component: () => import('@/views/Customers/CustomerList.vue'),
        meta: { requiresAuth: true },
      },
      {
        path: '/dashboard/products',
        name: 'ProductList',
        component: () => import('@/views/Products/ProductList.vue'),
        meta: { requiresAuth: true },
      },
      // other dashboard routes can go here
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
