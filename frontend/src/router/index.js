import { createRouter, createWebHistory } from "vue-router";

import Home from "../pages/Home.vue";
import AdminDashboard from "../pages/AdminDashboard.vue";
import CustomerDashboard from "../pages/CustomerDashboard.vue";
import TenantAdminDashboard from "../pages/TenantAdminDashboard.vue";
import Login from "../pages/login.vue";

const routes = [
  { path: "/", component: Home },
  { path: "/AdminDashboard", component: AdminDashboard },
  { path: "/CustomerDashboard", component: CustomerDashboard },
  { path: "/TenantAdmin", component: TenantAdminDashboard },
  { path: "/login", component: Login },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
