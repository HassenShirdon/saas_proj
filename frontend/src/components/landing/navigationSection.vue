<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">
        <img src="@/assets/logo.png" alt="Logo">
      </a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav">
          <li class="nav-item">
            <a class="nav-link" href="#">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Features</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Pricing</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#">Contact</a>
          </li>
        </ul>
        <div class="d-flex ms-auto ">

          <router-link to="/signin" class="btn btn-primary rounded-pill m-2">Log in</router-link>
          <router-link to="/sign-up" class="btn btn-primary rounded-pill m-2">Register</router-link>

        </div>
      </div>
    </div>
  </nav>
</template>

<script>

import { createRouter, createWebHistory } from 'vue-router'
import login from '@/views/Auth/loginView.vue';
import Register from '@/views/Auth/register.vue'
const routes = [
  {
    path: '/signin',
    name: 'login',
    component: login,
  },
  {
    path: '/sign-up',
    name: 'register',
    component: Register,
  },
]
const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router

// export default {
//   name: 'TopBarNav',
//   mounted() {
//     new bootstrap.ScrollSpy(document.body, {
//       target: '#navbar',
//       offset: 80,
//     })
//   },
// }
// window.addEventListener('scroll', () => {
//   const navbar = document.querySelector('.navbar');
//   if (window.scrollY > 50) {
//     navbar.classList.add('scrolled');
//   } else {
//     navbar.classList.remove('scrolled');
//   }
// });
</script>

<style scoped>
body {
  margin: 0;
  font-family: 'ubuntu', sans-serif;
}

.navbar {
  background: #efefef;
  padding: 0.5rem 1.5rem;
  transition: box-shadow 0.3s ease;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.navbar.scrolled {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  /* Bootstrap shadow-sm equivalent */
  background: #efefef;
}

.navbar-brand img {
  height: 40px;
  transition: transform 0.3s ease;
}

.navbar-brand img:hover {
  transform: scale(1.1);
}

.navbar-nav {
  display: flex;
  justify-content: center;
  flex-grow: 1;
}

.nav-link {
  color: #1178f5 !important;
  font-weight: 500;
  margin: 0 1rem;
  font-size: 1.1rem;
  position: relative;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #facc15 !important;
}

.nav-link::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: -5px;
  left: 0;
  background-color: #facc15;
  transition: width 0.3s ease;
}

.nav-link:hover::after {
  width: 100%;
}

.user-profile img {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #ffffff;
  transition: transform 0.3s ease;
}

.user-profile img:hover {
  transform: scale(1.1);
}

.dropdown-menu {
  background: #ffffff;
  border: none;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  min-width: 150px;
}

.dropdown-item {
  color: #6b21a8;
  font-weight: 500;
  padding: 0.5rem 1rem;
  transition: background 0.3s ease, color 0.3s ease;
}

.dropdown-item:hover {
  background: #06b6d4;
  color: #ffffff;
}

@media (max-width: 991px) {
  .navbar-nav {
    justify-content: flex-start;
    margin-top: 1rem;
  }
}

.nav-link {
  margin: 0.5rem 0;
}
</style>
