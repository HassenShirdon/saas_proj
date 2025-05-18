<template>
  <nav
    id="navbar"
    class="navbar navbar-expand-lg fixed-top custom-navbar shadow-sm"
    data-bs-spy="scroll"
    data-bs-target="#navbar"
    data-bs-offset="80"
    tabindex="0"
  >
    <div class="container-fluid d-flex justify-content-between align-items-center">
      <!-- Logo -->
      <a class="navbar-brand d-flex align-items-center" href="#home">
        <img
          src="@/assets/logo.png"
          alt="Marjaan Solutions Logo"
          height="40"
          width="auto"
          class="me-2"
        />
      </a>

      <!-- Toggler -->
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
        aria-controls="navbarNav"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- Navigation Links + Auth Buttons -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-lg-center">
          <li class="nav-item">
            <a class="nav-link" href="#home">Home</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#features">Features</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#about">About Us</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#testimonials">Testimonials</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#pricing">Pricing</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="#contact">Contact</a>
          </li>
        </ul>

        <!-- Auth Buttons -->
        <div class="d-flex ms-lg-3 mt-3 mt-lg-0">
          <a href="/signin" class="btn btn-outline-primary me-2">Sign In</a>
          <a href="/signup" class="btn btn-primary">Sign Up</a>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'TopBarNav',
  mounted() {
    new bootstrap.ScrollSpy(document.body, {
      target: '#navbar',
      offset: 80,
    })
  },
}
</script>

<style scoped>
.custom-navbar {
  background-color: white;
  /* transition: background-color 0.3s ease; */
  padding: 1rem 2rem;
  z-index: 1000;
}

.navbar-nav .nav-link {
  color: #5d7a96;
  font-weight: 500;
  margin-left: 1rem;
  transition: color 0.3s ease;
}

.navbar-nav .nav-link:hover,
.navbar-nav .nav-link.active {
  color: #007acc;
}

.navbar-brand img {
  max-height: 40px;
  width: auto;
}

/* Auth Buttons */
.btn-outline-primary {
  border-color: #00aaff;
  color: #00aaff;
}

.btn-outline-primary:hover {
  background-color: #00aaff;
  color: #fff;
}

.btn-primary {
  background-color: #00aaff;
  border-color: #00aaff;
}

.btn-primary:hover {
  background-color: #007acc;
  border-color: #007acc;
}
</style>
