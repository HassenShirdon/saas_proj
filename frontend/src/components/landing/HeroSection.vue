<template>
  <section class="hero-section">
    <div class="container">
      <div class="row align-items-center">
        <!-- Text Column -->
        <div class="col-lg-6 text-center text-lg-start">
          <h1 class="display-4 fw-bold mb-4">Transform the Way You Work</h1>
          <p class="lead mb-5 text-muted">
            Marjaan Solutions empowers your business with integrated tools for operations, HR,
            finance, and more—all in one powerful SaaS platform.
          </p>
          <div class="d-flex justify-content-center justify-content-lg-start gap-3">
            <a href="#cta" class="btn btn-modern-primary btn-lg px-4 py-3">
              Get Started <i class="bi bi-arrow-right ms-2"></i>
            </a>
            <a href="#features" class="btn btn-modern-outline btn-lg px-4 py-3">
              <i class="bi bi-grid-fill me-2"></i>Explore Features
            </a>
          </div>
        </div>

        <!-- Image Column with Hover Effect -->
        <div class="col-lg-6 mt-4 mt-lg-0 text-center">
          <div class="image-hover-wrapper">
            <img src="@/assets/hero-illustration.png" alt="Dashboard preview" class="img-fluid rounded-4 shadow-md" />
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
  min-height: 90vh;
  display: flex;
  align-items: center;
  padding: 4rem 0;
  background: #efefef;
}

h1 {
  color: #002b49;
  line-height: 1.2;
}

/* Modern Button Styles */
.btn-modern-primary {
  background-color: #00aaff;
  border: none;
  color: white;
  border-radius: 8px;
  font-weight: 600;
  position: relative;
  overflow: hidden;
  transition: all 0.4s ease;
  box-shadow: 0 4px 6px rgba(0, 170, 255, 0.2);
}

.btn-modern-primary:hover {
  background-color: #0088cc;
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 170, 255, 0.3);
}

.btn-modern-primary::after {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: 0.5s;
}

.btn-modern-primary:hover::after {
  left: 100%;
}

.btn-modern-outline {
  background-color: transparent;
  border: 2px solid #00aaff;
  color: #00aaff;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-modern-outline:hover {
  background-color: #00aaff;
  color: white;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0, 170, 255, 0.2);
}

/* Image Hover Effects */
.image-hover-wrapper {
  position: relative;
  display: inline-block;
  transition: all 0.4s ease;
}

.image-hover-wrapper:hover {
  transform: translateY(-5px);
}

.image-hover-wrapper::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 170, 255, 0.05);
  border-radius: 16px;
  transition: all 0.3s ease;
  opacity: 0;
}

.image-hover-wrapper:hover::before {
  opacity: 1;
}

.image-hover-wrapper img {
  transition: all 0.4s ease;
  border-radius: 12px;
}

.image-hover-wrapper:hover img {
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.1);
}

@media (max-width: 992px) {
  .hero-section {
    text-align: center;
    padding: 3rem 0;
  }

  .display-4 {
    font-size: 2.5rem;
  }

  .image-hover-wrapper {
    margin-top: 2rem;
  }
}
</style>