<template>
  <section id="cta" class="cta-section">
    <div class="container">
      <div class="cta-content">
        <div class="cta-text">
          <span class="badge bg-white-soft mb-3">Get Started</span>
          <h2 class="cta-title">Ready to Transform Your Business?</h2>
          <p class="cta-description">
            Join thousands of businesses that trust Marjaan Solutions for their operations.
            Start your journey today with our 14-day free trial.
          </p>
          <div class="cta-buttons">
            <a href="#contact" class="btn btn-primary btn-lg">
              Start Free Trial <i class="bi bi-arrow-right ms-2"></i>
            </a>
            <a href="#demo" class="btn btn-outline-light btn-lg">
              <i class="bi bi-play-circle me-2"></i>Watch Demo
            </a>
          </div>
          <div class="cta-features">
            <div class="feature">
              <i class="bi bi-check-circle-fill"></i>
              <span>No credit card required</span>
            </div>
            <div class="feature">
              <i class="bi bi-check-circle-fill"></i>
              <span>14-day free trial</span>
            </div>
            <div class="feature">
              <i class="bi bi-check-circle-fill"></i>
              <span>Cancel anytime</span>
            </div>
          </div>
        </div>
        <div class="cta-image">
          <img src="@/assets/loginScreen.jpg" alt="Get Started" class="img-fluid ">
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'CtaSection',
}
</script>

<style scoped>
.cta-section {
  padding: 3rem 0;
  background: #00aaff;
  position: relative;
  overflow: hidden;
}

.cta-section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;

  opacity: 0.1;
}

.cta-content {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 4rem;
}

.cta-text {
  flex: 1;
  color: white;
}

.badge {
  padding: 0.5rem 1rem;
  font-weight: 500;
  font-size: 0.875rem;
  border-radius: 50px;
}

.bg-white-soft {
  background-color: rgba(255, 255, 255, 0.2);
  color: white;
}

.cta-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.cta-description {
  font-size: 1.125rem;
  opacity: 0.9;
  margin-bottom: 2rem;
  max-width: 600px;
}

.cta-buttons {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.btn-primary {
  background: white;
  color: #00aaff;
  border: none;
  padding: 1rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

.btn-primary:hover {
  background: #f8fafc;
  transform: translateY(-2px);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.15);
}

.btn-outline-light {
  background: transparent;
  border: 2px solid rgba(255, 255, 255, 0.5);
  color: white;
  padding: 1rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-outline-light:hover {
  background: rgba(255, 255, 255, 0.1);
  border-color: white;
  transform: translateY(-2px);
}

.cta-features {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
}

.feature {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.875rem;
  opacity: 0.9;
}

.feature i {
  font-size: 1rem;
}

.cta-image {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.cta-image img {
  max-width: 100%;
  height: auto;
  animation: float 6s ease-in-out infinite;
}

@keyframes float {

  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-20px);
  }
}

@media (max-width: 991px) {
  .cta-section {
    padding: 4rem 0;
  }

  .cta-content {
    flex-direction: column;
    text-align: center;
    gap: 2rem;
  }

  .cta-title {
    font-size: 2.5rem;
  }

  .cta-description {
    margin-left: auto;
    margin-right: auto;
  }

  .cta-buttons {
    justify-content: center;
  }

  .cta-features {
    justify-content: center;
  }

  .cta-image {
    order: -1;
  }

  .cta-image img {
    max-width: 80%;
  }
}
</style>
