<template>
  <section class="hero-section bg-light py-5">
    <div class="container">
      <div class="row align-items-center">
        <div class="col-lg-6 text-center text-lg-start">
          <h1 class="display-4 fw-bold mb-4">Welcome to Your Future</h1>
          <p class="lead mb-4">
            Discover a modern, innovative platform built for success. Join thousands of users today.
          </p>
          <a href="#cta" class="btn btn-primary btn-lg">Get Started</a>
        </div>
        <div class="col-lg-6">
          <img src="" alt="Hero Image" class="img-fluid rounded shadow" />
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
  min-height: 80vh;
  display: flex;
  align-items: center;
  background: linear-gradient(135deg, rgba(0, 0, 0, 0.1), rgba(0, 0, 0, 0.3));
}
</style>
