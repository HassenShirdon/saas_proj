<template>
  <section id="cta" class="cta-section">
    <div class="container">
      <div class="cta-content">
        <div class="cta-text">
          <span class="badge bg-primary-soft mb-3">Start for Free</span>
          <h2 class="cta-title">Supercharge Your Workflow with Marjaan Solutions</h2>
          <p class="cta-description">
            Experience the all-in-one SaaS platform trusted by modern businesses. Automate, collaborate, and grow—risk
            free.
          </p>
          <form class="cta-form" @submit.prevent>
            <input type="email" placeholder="Enter your business email" class="cta-input" required>
            <button type="submit" class="btn btn-primary btn-lg">Start Free Trial</button>
          </form>
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
          <img src="@/assets/loginScreen.jpg" alt="SaaS Dashboard Preview" class="img-fluid">
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
  padding: 4rem 0;
  background: #f0f0f0;
  position: relative;
  overflow: hidden;
}

.cta-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 4rem;
}

.cta-text {
  flex: 1;
  color: #222;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.badge {
  padding: 0.5rem 1.25rem;
  font-weight: 600;
  font-size: 0.95rem;
  border-radius: 50px;
  letter-spacing: 0.03em;
  display: inline-block;
}

.bg-primary-soft {
  background-color: #e0f6ff;
  color: #00aaff;
}

.cta-title {
  font-size: 2.7rem;
  font-weight: 800;
  margin-bottom: 1.2rem;
  line-height: 1.15;
  color: #222;
}

.cta-description {
  font-size: 1.15rem;
  opacity: 0.95;
  margin-bottom: 2rem;
  max-width: 520px;
  color: #444;
}

.cta-form {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
  max-width: 430px;
}

.cta-input {
  flex: 1;
  padding: 0.9rem 1.2rem;
  border: 1.5px solid #d1eaff;
  border-radius: 10px;
  font-size: 1rem;
  outline: none;
  transition: border 0.2s;
  background: #fff;
}

.cta-input:focus {
  border-color: #00aaff;
}

.btn-primary {
  background: #00aaff;
  color: #fff;
  border: none;
  padding: 0.9rem 2rem;
  border-radius: 10px;
  font-weight: 700;
  font-size: 1rem;
  transition: background 0.2s, box-shadow 0.2s;
  box-shadow: 0 2px 8px rgba(0, 170, 255, 0.08);
}

.btn-primary:hover {
  background: #008ecc;
}

.cta-features {
  display: flex;
  flex-wrap: wrap;
  gap: 1.2rem;
  margin-top: 0.5rem;
}

.feature {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.98rem;
  color: #00aaff;
  background: #e0f6ff;
  border-radius: 8px;
  padding: 0.4rem 0.9rem;
}

.feature i {
  font-size: 1.1rem;
}

.cta-image {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}

.cta-image img {
  max-width: 95%;
  height: auto;
  border-radius: 18px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
  background: #fff;
  animation: float 6s ease-in-out infinite;
}

@keyframes float {

  0%,
  100% {
    transform: translateY(0);
  }

  50% {
    transform: translateY(-18px);
  }
}

@media (max-width: 991px) {
  .cta-content {
    flex-direction: column;
    text-align: center;
    gap: 2.5rem;
  }

  .cta-title {
    font-size: 2rem;
  }

  .cta-description {
    margin-left: auto;
    margin-right: auto;
  }

  .cta-form {
    flex-direction: column;
    max-width: 100%;
  }

  .cta-image img {
    max-width: 80%;
  }
}
</style>
