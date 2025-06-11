<template>
  <section class="hero-section">
    <div class="container">
      <div class="row align-items-center">
        <!-- Text Column -->
        <div class="col-lg-6 text-center text-lg-start">
          <div class="hero-content">
            <span class="badge bg-primary-soft mb-3">Enterprise Solutions</span>
            <h1 class="display-4 fw-bold mb-4">
              Transform Your Business with <span class="text-gradient">Marjaan Solutions</span>
            </h1>
            <p class="lead mb-5">
              Streamline your operations with our all-in-one platform. From HR to finance,
              we've got everything you need to scale your business efficiently.
            </p>
            <div class="d-flex flex-column flex-sm-row justify-content-center justify-content-lg-start gap-3">
              <a href="#cta" class="btn btn-primary btn-lg">
                Start Free Trial <i class="bi bi-arrow-right ms-2"></i>
              </a>
              <a href="#features" class="btn btn-outline btn-lg">
                <i class="bi bi-play-circle me-2"></i>Watch Demo
              </a>
            </div>
            <div class="trust-badges mt-5">
              <p class="text-muted mb-3">Trusted by leading companies</p>
              <div class="d-flex flex-wrap justify-content-center justify-content-lg-start gap-4">
                <img src="@/assets/jeehgeneral.jpeg" alt="jeeh General Trading" class="company-logo">
                <img src="@/assets/logo.png" alt="Company 2" class="company-logo">
                <img src="@/assets/logo.png" alt="Company 3" class="company-logo">
              </div>
            </div>
          </div>
        </div>

        <!-- Image Column -->
        <div class="col-lg-6 mt-5 mt-lg-0">
          <div class="hero-image-wrapper">
            <img src="@/assets/hero-illustration.png" alt="Dashboard preview" class="img-fluid hero-image" />
            <div class="floating-card card-1">
              <i class="bi bi-graph-up-arrow"></i>
              <span>98% Uptime</span>
            </div>
            <div class="floating-card card-2">
              <i class="bi bi-shield-check"></i>
              <span>Enterprise Security</span>
            </div>
          </div>
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
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 6rem 0;
  background: linear-gradient(to bottom, #ffffff, #f8fafc);
  position: relative;
  overflow: hidden;
}

.hero-content {
  position: relative;
  z-index: 2;
}

.badge {
  padding: 0.5rem 1rem;
  font-weight: 500;
  font-size: 0.875rem;
  border-radius: 50px;
}

.bg-primary-soft {
  background-color: rgba(0, 170, 255, 0.1);
  color: #00aaff;
}

.text-gradient {
  background: linear-gradient(135deg, #00aaff, #0088cc);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

h1 {
  color: #1a202c;
  line-height: 1.2;
  font-size: 3.5rem;
}

.lead {
  color: #4a5568;
  font-size: 1.25rem;
  line-height: 1.6;
}

.btn-primary {
  background: #00aaff;
  border: none;
  color: white;
  padding: 1rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 170, 255, 0.2);
}

.btn-primary:hover {
  background: #0088cc;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0, 170, 255, 0.3);
}

.btn-outline {
  background: transparent;
  border: 2px solid #e2e8f0;
  color: #4a5568;
  padding: 1rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-outline:hover {
  background: #f8fafc;
  border-color: #cbd5e0;
  transform: translateY(-2px);
}

.hero-image-wrapper {
  position: relative;
  padding: 2rem;
}

.hero-image {
  border-radius: 24px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.hero-image:hover {
  transform: translateY(-5px);
  box-shadow: 0 25px 50px rgba(0, 0, 0, 0.15);
}

.floating-card {
  position: absolute;
  background: white;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-weight: 500;
  color: #2d3748;
  animation: float 3s ease-in-out infinite;
}

.card-1 {
  top: 10%;
  right: 0;
  animation-delay: 0s;
}

.card-2 {
  bottom: 10%;
  left: 0;
  animation-delay: 1.5s;
}

@keyframes float {

  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-10px);
  }
}

.company-logo {
  height: 24px;
  opacity: 0.7;
  transition: opacity 0.3s ease;
}

.company-logo:hover {
  opacity: 1;
}

@media (max-width: 991px) {
  .hero-section {
    padding: 4rem 0;
    text-align: center;
  }

  h1 {
    font-size: 2.5rem;
  }

  .hero-image-wrapper {
    margin-top: 3rem;
  }

  .floating-card {
    display: none;
  }
}
</style>