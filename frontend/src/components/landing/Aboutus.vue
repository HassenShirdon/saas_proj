<template>
  <!-- About Section: Introduces the company and highlights core services -->
  <section class="about-section">
    <div class="container">
      <div class="row align-items-center">
        <!-- Text Content -->
        <div class="col-lg-6 mb-4 mb-lg-0">
          <div class="about-content">
            <span class="badge bg-primary-soft mb-3">About Us</span>
            <h2 class="section-title">Empowering Businesses with Smart Solutions</h2>

            <p class="section-description">
              Marjaan Solutions is a forward-thinking logistics software company dedicated to helping
              businesses modernize and automate their operations through modular, easy-to-integrate
              SaaS solutions.
            </p>

            <div class="stats-grid">
              <div class="stat-item">
                <div class="stat-number">500+</div>
                <div class="stat-label">Active Clients</div>
              </div>
              <div class="stat-item">
                <div class="stat-number">98%</div>
                <div class="stat-label">Client Satisfaction</div>
              </div>
              <div class="stat-item">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Support</div>
              </div>
            </div>

            <div class="features-grid">
              <div class="feature-item">
                <div class="feature-icon bg-primary-soft">
                  <i class="bi bi-box-seam-fill"></i>
                </div>
                <div class="feature-content">
                  <h4>Inventory System</h4>
                  <p>Real-time tracking, automated restocking, and smart alerts</p>
                </div>
              </div>
              <div class="feature-item">
                <div class="feature-icon bg-success-soft">
                  <i class="bi bi-graph-up-arrow"></i>
                </div>
                <div class="feature-content">
                  <h4>Finance Module</h4>
                  <p>Comprehensive financial insights and reporting tools</p>
                </div>
              </div>
              <div class="feature-item">
                <div class="feature-icon bg-warning-soft">
                  <i class="bi bi-people-fill"></i>
                </div>
                <div class="feature-content">
                  <h4>HR Management</h4>
                  <p>Streamlined employee management and payroll</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Image Content -->
        <div class="col-lg-6">
          <div class="about-image-wrapper">
            <img src="@/assets/aboutus.png" alt="Marjaan Solutions Interface" class="about-image" />
            <div class="floating-card card-1">
              <i class="bi bi-shield-check"></i>
              <span>Enterprise Security</span>
            </div>
            <div class="floating-card card-2">
              <i class="bi bi-lightning-charge"></i>
              <span>Fast Performance</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
export default {
  name: 'AboutSection',
  // This is a presentational component and does not require reactive state or lifecycle hooks for now.
}
</script>

<style scoped>
.about-section {
  padding: 6rem 0;
  background: #ffffff;
  position: relative;
  overflow: hidden;
}

.about-content {
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

.section-title {
  font-size: 2.5rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.section-description {
  font-size: 1.125rem;
  color: #4a5568;
  line-height: 1.6;
  margin-bottom: 2rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 1.5rem;
  margin-bottom: 3rem;
}

.stat-item {
  text-align: center;
  padding: 1.5rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

.stat-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: #00aaff;
  margin-bottom: 0.5rem;
}

.stat-label {
  font-size: 0.875rem;
  color: #4a5568;
  font-weight: 500;
}

.features-grid {
  display: grid;
  gap: 1.5rem;
}

.feature-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1.5rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
}

.feature-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.1);
}

.feature-icon {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: #1a202c;
}

.bg-success-soft {
  background-color: rgba(16, 185, 129, 0.1);
  color: #10b981;
}

.bg-warning-soft {
  background-color: rgba(245, 158, 11, 0.1);
  color: #f59e0b;
}

.feature-content h4 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 0.5rem;
}

.feature-content p {
  font-size: 0.875rem;
  color: #4a5568;
  margin: 0;
}

.about-image-wrapper {
  position: relative;
  padding: 2rem;
}

.about-image {
  width: 100%;
  border-radius: 16px;
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.about-image:hover {
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

@media (max-width: 991px) {
  .about-section {
    padding: 4rem 0;
  }

  .section-title {
    font-size: 2rem;
  }

  .stats-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .about-image-wrapper {
    margin-top: 3rem;
  }

  .floating-card {
    display: none;
  }
}

@media (max-width: 576px) {
  .stats-grid {
    grid-template-columns: 1fr;
  }
}
</style>
