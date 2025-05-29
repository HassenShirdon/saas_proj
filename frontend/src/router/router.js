// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
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
  },
  {
    path: '/login',
    name: 'login',
    component: login,
  },
  {
    path: '/sign-up',
    name: 'signup',
    component: Register,
  },

  {
    path: '/dashboard',
    component: dashboard,
    children: [
      {
        path: 'customers',
        name: 'customerList',
        component: '',
      },
      {
        path: 'products',
        name: 'ProductList',
        component: '',
      },
      // other dashboard routes can go here
    ],
  },
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
