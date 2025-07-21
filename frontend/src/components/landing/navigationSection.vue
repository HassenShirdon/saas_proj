<template>
  <nav class="navbar navbar-expand-lg">
    <div class="container mx-auto">
      <a class="navbar-brand" href="#">
        <img src="@/assets/logo.png" alt="Logo">
      </a>
     <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
        aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
  <span class="navbar-toggler-icon"></span>
</button>
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav mx-auto item-center">
          <li class="nav-item">
            <a class="nav-link modern-link" href="">
              Home
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#features-section">Features</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#about-section">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#pricing-section">Pricing</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#contact">Contact</a>
          </li>
        </ul>
        <!-- Template -->
        <button class="theme-toggle p-2 m-2 border-0" @click="toggleTheme">
          <i class="bi" :class="isDarkMode ? 'bi-sun' : 'bi-moon'"></i>
        </button>

        <div class="nav-buttons">
          <!-- <router-link to="/login" class="btn btn-login">Log in</router-link> -->
          <router-link to="/login" class="btn btn-register">Log in</router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>


export default {
  name: 'NavigationSection',

  data() {
    return {
      themeStore: null,
    };
  },

  computed: {
    isDarkMode() {
      return this.themeStore?.theme === 'dark';
    }
  },

  mounted() {

    window.addEventListener('scroll', this.handleScroll);
  },

  beforeUnmount() {
    window.removeEventListener('scroll', this.handleScroll);
  },

  methods: {
    handleScroll() {
      const navbar = document.querySelector('.navbar');
      if (window.scrollY > 50) {
        navbar.classList.add('scrolled');
      } else {
        navbar.classList.remove('scrolled');
      }
    },

    toggleTheme() {
      if (this.themeStore) {
        this.themeStore.toggleTheme(); // ✅ call through method
      }
    }
  }
};
</script>


<style scoped>
body {
  margin: 0;
  padding: 0;
}

.navbar {
  background: #f0f0f0;
  padding: 1rem 0;
  transition: all 0.3s ease;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  backdrop-filter: blur(10px);
  font: "roboto"
}

.navbar.scrolled {
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  padding: 0.75rem 0;
}

.navbar-brand img {
  height: 35px;
  transition: transform 0.3s ease;
}

.navbar-brand img:hover {
  transform: scale(1.05);
}

.navbar-nav {
  display: flex;
  justify-content: center;
  flex-grow: 1;
}
 .navbar-toggler-icon {
    background-image: url("data:image/svg+xml;charset=utf8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(33, 37, 41, 1)' stroke-width='2' stroke-linecap='round' stroke-miterlimit='10' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E");
  } 
.nav-link {
  color: #2d3748 !important;
  font-weight: 500;
  padding: 0.5rem 1rem !important;
  margin: 0 0.25rem;
  font-size: 1rem;
  position: relative;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #00aaff !important;
}

.nav-link::after {
  content: '';
  position: absolute;
  width: 0;
  height: 2px;
  bottom: 0;
  left: 50%;
  background-color: #00aaff;
  transition: all 0.3s ease;
  transform: translateX(-50%);
}

.nav-link:hover::after {
  width: 80%;
}

.nav-buttons {
  display: flex;
  gap: 1rem;
  align-items: center;
}

.btn-login {
  color: #2d3748;
  background: transparent;
  border: none;
  font-weight: 500;
  padding: 0.5rem 1.25rem;
  transition: all 0.3s ease;
}

.btn-login:hover {
  color: #00aaff;
  transform: translateY(-1px);
}

.btn-register {
  background: #00aaff;
  color: white;
  border: none;
  font-weight: 500;
  padding: 0.5rem 1.5rem;
  border-radius: 8px;
  transition: all 0.3s ease;
}

.btn-register:hover {
  background: #0088cc;
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(0, 170, 255, 0.2);
}

@media (max-width: 991px) {
  .navbar-nav {
    margin: 1rem 0;
  }

  .nav-buttons {
    flex-direction: column;
    width: 100%;
    gap: 0.5rem;
  }

  .btn-login,
  .btn-register {
    width: 100%;
    text-align: center;
  }
}
</style>
