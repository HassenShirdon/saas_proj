<template>
  <section id="features-section" class="features-section">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge badge-pill badge-gradient">Features</span>
        <h2 class="section-title">Everything You Need to Scale</h2>
        <p class="section-description">
          Powerful tools and features to help your business grow efficiently.
        </p>
      </div>
      <div class="row features-grid">
        <div v-for="(feature, index) in features" :key="index" class="col-12 col-md-6 col-lg-4 d-flex"
          :data-aos="'fade-up'" :data-aos-delay="index * 100">
          <div class="feature-card flex-fill">
            <div class="feature-icon" :class="feature.iconColor">
              <i :class="feature.icon"></i>
            </div>
            <h3 class="feature-title">{{ feature.title }}</h3>
            <p class="feature-description">{{ feature.description }}</p>
          </div>
        </div>
      </div>
      <div class="features-cta text-center">
        <button class="btn btn-primary btn-lg">Get Started</button>
      </div>
    </div>
  </section>
</template>

<script>
import AOS from 'aos'
import 'aos/dist/aos.css'

export default {
  name: 'FeaturesSection',
  mounted() {
    AOS.init({ duration: 800, once: true })
  },
  data() {
    return {
      features: [
        {
          icon: 'bi bi-people-fill',
          iconColor: 'icon-primary',
          title: 'HR Management',
          description:
            'Streamline your HR processes with our comprehensive employee management system.',
        },
        {
          icon: 'bi bi-graph-up-arrow',
          iconColor: 'icon-success',
          title: 'Finance Module',
          description:
            'Get real-time insights into your business finances with advanced analytics.',
        },
        {
          icon: 'bi bi-box-seam-fill',
          iconColor: 'icon-warning',
          title: 'Inventory System',
          description:
            'Optimize your inventory with smart tracking and automated reordering.',
        },
        {
          icon: 'bi bi-kanban-fill',
          iconColor: 'icon-info',
          title: 'Project Management',
          description:
            'Collaborate effectively with our intuitive project management tools.',
        },
        {
          icon: 'bi bi-shield-lock-fill',
          iconColor: 'icon-danger',
          title: 'Security & Access',
          description:
            'Enterprise-grade security with granular access controls and encryption.',
        },
        {
          icon: 'bi bi-chat-dots-fill',
          iconColor: 'icon-purple',
          title: 'Customer Support',
          description:
            'Deliver exceptional customer service with our integrated support system.',
        },
      ],
    }
  },
}
</script>

<style scoped>
.features-section {
  padding: 5rem 0 3rem 0;
  background: #f0f0f0;
}

.section-header {
  margin-bottom: 3rem;
}

.badge-gradient {
  background: linear-gradient(90deg, #00aaff 0%, #6f6fff 100%);
  color: #fff;
  font-weight: 600;
  font-size: 1rem;
  padding: 0.5rem 1.25rem;
  border-radius: 999px;
  letter-spacing: 0.05em;
  margin-bottom: 1rem;
  display: inline-block;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1a202c;
  margin-bottom: 0.5rem;
}

.section-description {
  font-size: 1.15rem;
  color: #64748b;
  max-width: 540px;
  margin: 0 auto 2rem auto;
}

.features-grid {
  row-gap: 2.5rem;
  column-gap: 0;
}

.feature-card {
  background: #fff;
  border-radius: 1.25rem;
  padding: 2.25rem 1.5rem 2rem 1.5rem;
  box-shadow: 0 2px 24px 0 rgba(0, 42, 120, 0.07);
  border: none;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  transition: box-shadow 0.2s, transform 0.2s;
  margin-bottom: 1.5rem;
  min-height: 320px;
}

.feature-card:hover {
  box-shadow: 0 8px 32px 0 rgba(0, 42, 120, 0.13);
  transform: translateY(-4px) scale(1.02);
}

.feature-icon {
  width: 64px;
  height: 64px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
  margin-bottom: 1.5rem;
  box-shadow: 0 2px 12px 0 rgba(0, 170, 255, 0.08);
}

.icon-primary {
  background: rgba(0, 170, 255, 0.12);
  color: #00aaff;
}

.icon-success {
  background: rgba(16, 185, 129, 0.12);
  color: #10b981;
}

.icon-warning {
  background: rgba(245, 158, 11, 0.12);
  color: #f59e0b;
}

.icon-info {
  background: rgba(6, 182, 212, 0.12);
  color: #06b6d4;
}

.icon-danger {
  background: rgba(239, 68, 68, 0.12);
  color: #ef4444;
}

.icon-purple {
  background: rgba(139, 92, 246, 0.12);
  color: #8b5cf6;
}

.feature-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 0.75rem;
}

.feature-description {
  color: #64748b;
  font-size: 1rem;
  line-height: 1.7;
  margin-bottom: 0;
}

.features-cta {
  margin-top: 3rem;
}

.btn-primary {
  background: linear-gradient(90deg, #00aaff 0%, #6f6fff 100%);
  border: none;
  color: #fff;
  padding: 0.9rem 2.5rem;
  border-radius: 999px;
  font-weight: 700;
  font-size: 1.1rem;
  box-shadow: 0 4px 16px rgba(0, 170, 255, 0.13);
  transition: background 0.2s, transform 0.2s;
}

.btn-primary:hover {
  background: linear-gradient(90deg, #0088cc 0%, #4f4fff 100%);
  transform: translateY(-2px) scale(1.03);
}

@media (max-width: 991px) {
  .features-section {
    padding: 3rem 0 2rem 0;
  }

  .section-title {
    font-size: 2rem;
  }

  .feature-card {
    padding: 1.5rem 1rem 1.5rem 1rem;
    min-height: 260px;
  }
}
</style>
