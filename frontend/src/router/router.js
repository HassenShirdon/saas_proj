// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import customerslist from '@/components/customerslist.vue'
import LandingPage from '@/views/landing/LandingPage.vue'
import dashboard from '@/views/dashboard/dashboardPage.vue'
import login from '@/views/Auth/loginView.vue'

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
    path: '/dashboard',
    component: dashboard,
    children: [
      {
        path: 'customers',
        name: 'CustomerList',
        component: customerslist,
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
