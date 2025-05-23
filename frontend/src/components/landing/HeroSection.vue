<template>
  <section class="hero-section">
    <div class="container">
      <div class="row align-items-center">
        <!-- Text Column -->
        <div class="col-lg-6 text-center text-lg-start">
          <h1 class="display-3 fw-bold mb-4">Transform the Way You Work</h1>
          <p class="lead text-muted mb-4">
            Marjaan Solutions empowers your business with integrated tools for operations, HR,
            finance, and more—all in one powerful SaaS platform.
          </p>
          <div class="d-flex justify-content-center justify-content-lg-start gap-3">
            <a href="#cta" class="btn btn-primary btn-lg shadow-sm">Get Started</a>
            <a href="#features" class="btn btn-outline-primary btn-lg">Explore Features</a>
          </div>
        </div>

        <!-- Image Column -->
        <div class="col-lg-6 mt-5 mt-lg-0 text-center">
          <img src="@/assets/hero-illustration.png" alt="Dashboard preview" class="img-fluid hero-img rounded-4" />
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'HeroSection',
}
</script>

<style scoped>
.hero-section {
  min-height: 90vh;
  display: flex;
  align-items: center;
  padding-top: 5rem;
  padding-bottom: 5rem;
  background: #efefef;
}

h1 {
  color: #002b49;
}

.btn-primary {
  background-color: #00aaff;
  border-color: #00aaff;
}

.btn-primary:hover {
  background-color: #007acc;
  border-color: #007acc;
}

.btn-outline-primary {
  color: #00aaff;
  border-color: #00aaff;
}

.btn-outline-primary:hover {
  background-color: #00aaff;
  color: white;
  border-color: #00aaff;
}

.hero-img {
  max-height: 580px;
  object-fit: cover;
  margin-top: 2rem;
}
</style>
