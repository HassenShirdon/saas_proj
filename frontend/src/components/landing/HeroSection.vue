  <template>
    <section id="hero-section" class="pt-5 mt-5" style="min-height: 100vh;  background: #f0f0f0;">
      <div class="container">
        <div class="row align-items-center">
          <!-- Hero Content -->
          <div class="col-lg-6 mb-4 mb-lg-0">
            <div class="mb-3">
              <span class="badge bg-primary-subtle text-primary px-3 py-2 rounded-pill">
                <i class="bi bi-bell-fill me-2"></i> Inventory & Logistics Reinvented
              </span>
            </div>

            <h1 class="display-7 fw-bold mb-5">Unified Platform for Smarter Inventory & Logistics</h1>

            <p class="lead text-dark mb-4">
              Marjaan empowers your business with real-time control of inventory, seamless logistics, and data-driven
              decisions — all from one intuitive dashboard.
            </p>

            <a href="#" class="btn btn-primary btn-lg px-4">Get Started Now</a>
          </div>

          <!-- Hero Image -->
          <div class="col-lg-6 text-center">
            <img src="@/assets/hero-illustration.png" alt="Platform Illustration" class="img-fluid"
              style="max-height: 450px;" loading="lazy">
          </div>
        </div>

        <!-- Features Section -->
        <div class="row text-center mt-5">
          <div class="col-md-4 mb-4">
            <div class="p-3">
              <h5 class="fw-semibold text-primary">📦 Real-Time Inventory</h5>
              <p class="text-dark">Track stock levels, locations, and movements instantly — avoid stockouts and
                overstock.</p>
            </div>
          </div>
          <div class="col-md-4 mb-4">
            <div class="p-3">
              <h5 class="fw-semibold text-primary">🚚 Smart Logistics Automation</h5>
              <p class="text-dark">Streamline procurement to delivery with intelligent workflows and route
                optimization.</p>
            </div>
          </div>
          <div class="col-md-4 mb-4">
            <div class="p-3">
              <h5 class="fw-semibold text-primary">📊 Data-Driven Insights</h5>
              <p class="text-dark">Make informed decisions with powerful analytics on stock movement, suppliers, and
                cost.</p>
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
#hero-section {
  min-height: 100vh;
  top: 50px;
  display: flex;
  align-items: center;
  padding: 8rem 0 2rem 0;
  background: #f0f0f0;
  position: relative;
  overflow: hidden;
  color: #1a2233;
}

.hero-content {
  position: relative;
  z-index: 2;
  color: #1a2233;
}

.display-2 {
  font-size: 2.5rem;
  line-height: 1.15;
  color: #1a2233;
}

@media (min-width: 768px) {
  .display-2 {
    font-size: 3rem;
  }
}

@media (min-width: 1200px) {
  .display-2 {
    font-size: 3.5rem;
  }
}

.text-primary-gradient {
  background: linear-gradient(90deg, #3a8dde 0%, #00aaff 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.lead {
  color: #2d3a4a;
  font-size: 1.15rem;
  line-height: 1.6;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
}

.btn-primary {
  background: linear-gradient(90deg, #3a8dde 0%, #00aaff 100%);
  border: none;
  color: #fff;
  padding: 1rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  transition: all 0.3s ease;
  box-shadow: 0 4px 16px rgba(58, 141, 222, 0.08);
}

.btn-primary:hover {
  background: linear-gradient(90deg, #2b6cb0 0%, #0088cc 100%);
  transform: translateY(-2px) scale(1.03);
  box-shadow: 0 8px 24px rgba(58, 141, 222, 0.15);
}

.btn-outline-primary {
  background: transparent;
  border: 2px solid #3a8dde;
  color: #3a8dde;
  padding: 1rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.btn-outline-primary:hover {
  background: #e0f7fa;
  border-color: #00aaff;
  color: #2b6cb0;
  transform: translateY(-2px) scale(1.03);
}

.hero-image-wrapper {
  position: relative;
  padding: 0.5rem;
  width: 100%;
  max-width: 420px;
  margin: 0 auto;
}

.hero-image {
  border-radius: 24px;
  width: 100%;
  transition: all 0.3s ease;
}

.hero-image:hover {
  transform: translateY(-5px) scale(1.01);
  box-shadow: 0 25px 50px rgba(58, 141, 222, 0.15);
}

.floating-card {
  position: absolute;
  background: #fff;
  padding: 0.75rem 1.25rem;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(58, 141, 222, 0.08);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  font-weight: 500;
  color: #1a2233;
  animation: float 3s ease-in-out infinite;
  font-size: 1rem;
}

.card-1 {
  top: 10%;
  right: -30px;
  animation-delay: 0s;
}

.card-2 {
  bottom: 10%;
  left: -30px;
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

/* Trust Badges */
.trust-badges {
  margin-top: 2.5rem;
  background: #fff;
  border-radius: 1.5rem;
  box-shadow: 0 2px 16px rgba(58, 141, 222, 0.06);
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.trust-title {
  font-size: 1.1rem;
  color: #3a8dde;
  letter-spacing: 0.02em;
}

.company-logo {
  height: 38px;
  width: auto;
  opacity: 0.8;
  filter: grayscale(0.2);
  transition: opacity 0.3s, filter 0.3s;
  background: #f8fafc;
  border-radius: 0.5rem;
  padding: 0.25rem 0.5rem;
}

.company-logo:hover {
  opacity: 1;
  filter: none;
  background: #e0f7fa;
}

@media (max-width: 991px) {
  .hero-section {
    padding: 2.5rem 0 1.5rem 0;
    text-align: center;
  }

  .hero-image-wrapper {
    margin-top: 2rem;
    max-width: 340px;
  }

  .floating-card {
    display: none !important;
  }

  .trust-badges {
    margin-top: 2rem;
    padding: 1.25rem 0.5rem;
  }
}

@media (max-width: 575px) {
  .display-2 {
    font-size: 2rem;
  }

  .lead {
    font-size: 1rem;
    padding-left: 0.25rem;
    padding-right: 0.25rem;
  }

  .hero-section {
    padding: 1.5rem 0 1rem 0;
  }

  .trust-badges {
    padding: 1rem 0.25rem;
    border-radius: 1rem;
  }

  .company-logo {
    height: 28px;
    padding: 0.15rem 0.3rem;
  }
}
</style>