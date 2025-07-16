<template>
  <section id="about-section" class="about-section trendy-bg">
    <div class="container">
      <div class="row align-items-center flex-wrap-reverse">
        <!-- Image Content -->
        <div class="col-lg-6 mb-5 mb-lg-0">
          <div class="about-image-wrapper trendy-shadow">
            <img src="@/assets/aboutus.png" alt="Marjaan Solutions Interface" class="about-image" />
            <div class="floating-badge badge-gradient">
              <i class="bi bi-stars"></i>
              <span>Trusted by 500+ Clients</span>
            </div>
          </div>
        </div>
        <!-- Text Content -->
        <div class="col-lg-6">
          <div class="about-content">
            <span class="badge badge-gradient mb-3">About Us</span>
            <h2 class="section-title trendy-title">
              <span class="highlight">Empowering</span> Your Business with <span class="highlight">Smart
                Solutions</span>
            </h2>
            <p class="section-description">
              At Marjaan Solutions, we blend technology and innovation to deliver seamless logistics SaaS platforms. Our
              modular tools help you automate, scale, and thrive in a digital-first world.
            </p>
            <div class="stats-grid">
              <div class="stat-item trendy-shadow">
                <div class="stat-number">10+</div>
                <div class="stat-label">Active Clients</div>
              </div>
              <div class="stat-item trendy-shadow">
                <div class="stat-number">>90%</div>
                <div class="stat-label">Satisfaction</div>
              </div>
              <div class="stat-item trendy-shadow">
                <div class="stat-number">24/7</div>
                <div class="stat-label">Support</div>
              </div>
            </div>
            <div class="features-list">
              <div class="feature-item">
                <span class="feature-icon bg-gradient-inventory">
                  <i class="bi bi-box-seam-fill"></i>
                </span>
                <div>
                  <h4>Inventory System</h4>
                  <p>Live tracking, automated restocking, and smart alerts</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-icon bg-gradient-finance">
                  <i class="bi bi-graph-up-arrow"></i>
                </span>
                <div>
                  <h4>Finance Module</h4>
                  <p>Comprehensive insights and reporting tools</p>
                </div>
              </div>
              <div class="feature-item">
                <span class="feature-icon bg-gradient-hr">
                  <i class="bi bi-people-fill"></i>
                </span>
                <div>
                  <h4>HR Management</h4>
                  <p>Streamlined employee management and payroll</p>
                </div>
              </div>
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
}
</script>

<style scoped>
/* Trendy gradients and glassmorphism */
.trendy-bg {
  background: #f0f0f0;
  padding: 6rem 0;
  position: relative;
  overflow: hidden;
}

.trendy-title {
  font-size: 2.7rem;
  font-weight: 800;
  color: #1a202c;
  margin-bottom: 1.2rem;
  line-height: 1.15;
  letter-spacing: -1px;
}

.highlight {
  background: linear-gradient(90deg, #00aaff 0%, #10b981 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}

.badge-gradient {
  background: linear-gradient(90deg, #00aaff 0%, #10b981 100%);
  color: #fff;
  font-weight: 600;
  border-radius: 2rem;
  padding: 0.5rem 1.2rem;
  font-size: 0.95rem;
  box-shadow: 0 2px 12px rgba(16, 185, 129, 0.08);
  display: inline-block;
}

.section-description {
  font-size: 1.15rem;
  color: #374151;
  margin-bottom: 2.2rem;
  line-height: 1.7;
}

.stats-grid {
  display: flex;
  gap: 1.5rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}

.stat-item {
  flex: 1 1 120px;
  background: rgba(255, 255, 255, 0.7);
  border-radius: 1rem;
  text-align: center;
  padding: 1.2rem 0.8rem;
  transition: box-shadow 0.2s, transform 0.2s;
  backdrop-filter: blur(4px);
}

.stat-item:hover {
  box-shadow: 0 8px 24px rgba(0, 170, 255, 0.13);
  transform: translateY(-4px) scale(1.03);
}

.stat-number {
  font-size: 2.1rem;
  font-weight: 700;
  color: #00aaff;
  margin-bottom: 0.3rem;
  letter-spacing: -1px;
}

.stat-label {
  font-size: 0.95rem;
  color: #10b981;
  font-weight: 500;
}

.features-list {
  margin-top: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.1rem;
}

.feature-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  background: rgba(255, 255, 255, 0.8);
  border-radius: 1rem;
  padding: 1rem 1.2rem;
  box-shadow: 0 2px 8px rgba(0, 170, 255, 0.06);
  transition: box-shadow 0.2s, transform 0.2s;
}

.feature-item:hover {
  box-shadow: 0 8px 24px rgba(16, 185, 129, 0.10);
  transform: translateY(-2px) scale(1.01);
}

.feature-icon {
  width: 44px;
  height: 44px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  color: #fff;
  box-shadow: 0 2px 8px rgba(0, 170, 255, 0.10);
}

.bg-gradient-inventory {
  background: linear-gradient(135deg, #00aaff 0%, #38bdf8 100%);
}

.bg-gradient-finance {
  background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
}

.bg-gradient-hr {
  background: linear-gradient(135deg, #f59e0b 0%, #fbbf24 100%);
}

.feature-item h4 {
  font-size: 1.08rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 0.2rem;
}

.feature-item p {
  font-size: 0.93rem;
  color: #4b5563;
  margin: 0;
}

.about-image-wrapper {
  position: relative;
  padding: 2rem;
  border-radius: 2rem;
  background: #f0f0f0;
  box-shadow: 0 8px 32px rgba(0, 170, 255, 0.10);
  overflow: visible;
}

.about-image {
  width: 100%;
  border-radius: 1.5rem;
  box-shadow: 0 12px 32px rgba(16, 185, 129, 0.10);
  transition: transform 0.2s, box-shadow 0.2s;
}

.about-image:hover {
  transform: scale(1.03) translateY(-4px);
  box-shadow: 0 20px 48px rgba(0, 170, 255, 0.18);
}

.floating-badge {
  position: absolute;
  left: 1.5rem;
  bottom: -1.2rem;
  display: flex;
  align-items: center;
  gap: 0.7rem;
  padding: 0.7rem 1.3rem;
  font-size: 1rem;
  font-weight: 600;
  border-radius: 2rem;
  box-shadow: 0 4px 20px rgba(0, 170, 255, 0.12);
  animation: floatBadge 3s ease-in-out infinite;
  z-index: 2;
}

@keyframes floatBadge {

  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-10px);
  }
}

.trendy-shadow {
  box-shadow: 0 4px 24px rgba(0, 170, 255, 0.07);
}

@media (max-width: 991px) {
  .about-section {
    padding: 3rem 0;
  }

  .trendy-title {
    font-size: 2rem;
  }

  .about-image-wrapper {
    padding: 1rem;
  }

  .stats-grid {
    flex-direction: column;
    gap: 1rem;
  }
}

@media (max-width: 576px) {
  .about-section {
    padding: 2rem 0;
  }

  .about-image-wrapper {
    padding: 0.5rem;
  }

  .floating-badge {
    left: 0.5rem;
    bottom: -0.8rem;
    font-size: 0.9rem;
    padding: 0.5rem 1rem;
  }
}
</style>
