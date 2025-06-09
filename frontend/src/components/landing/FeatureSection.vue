<template>
  <section class="features-section">
    <div class="container">
      <div class="section-header text-center">
        <span class="badge bg-primary-soft mb-3">Features</span>
        <h2 class="section-title">Everything You Need to Scale</h2>
        <p class="section-description">
          Powerful tools and features to help your business grow efficiently
        </p>
      </div>

      <div class="row g-4">
        <div v-for="(feature, index) in features" :key="index" class="col-md-6 col-lg-4" :data-aos="'fade-up'"
          :data-aos-delay="index * 100">
          <div class="feature-card">
            <div class="feature-icon" :class="feature.iconColor">
              <i :class="feature.icon"></i>
            </div>
            <h3 class="feature-title">{{ feature.title }}</h3>
            <p class="feature-description">{{ feature.description }}</p>
            <a href="#" class="feature-link">
              Learn more <i class="bi bi-arrow-right"></i>
            </a>
          </div>
        </div>
      </div>

      <div class="features-cta text-center mt-5">
        <a href="#pricing" class="btn btn-primary btn-lg">
          View All Features <i class="bi bi-arrow-right ms-2"></i>
        </a>
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
    AOS.init({
      duration: 800,
      once: true
    })
  },
  data() {
    return {
      features: [
        {
          icon: 'bi bi-people-fill',
          iconColor: 'bg-primary-soft',
          title: 'HR Management',
          description:
            'Streamline your HR processes with our comprehensive employee management system.',
        },
        {
          icon: 'bi bi-graph-up-arrow',
          iconColor: 'bg-success-soft',
          title: 'Finance Module',
          description:
            'Get real-time insights into your business finances with advanced analytics.',
        },
        {
          icon: 'bi bi-box-seam-fill',
          iconColor: 'bg-warning-soft',
          title: 'Inventory System',
          description:
            'Optimize your inventory with smart tracking and automated reordering.',
        },
        {
          icon: 'bi bi-kanban-fill',
          iconColor: 'bg-info-soft',
          title: 'Project Management',
          description:
            'Collaborate effectively with our intuitive project management tools.',
        },
        {
          icon: 'bi bi-shield-lock-fill',
          iconColor: 'bg-danger-soft',
          title: 'Security & Access',
          description:
            'Enterprise-grade security with granular access controls and encryption.',
        },
        {
          icon: 'bi bi-chat-dots-fill',
          iconColor: 'bg-purple-soft',
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
  padding: 6rem 0;
  background: linear-gradient(to bottom, #f8fafc, #ffffff);
}

.section-header {
  margin-bottom: 4rem;
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
  margin-bottom: 1rem;
}

.section-description {
  font-size: 1.125rem;
  color: #4a5568;
  max-width: 600px;
  margin: 0 auto;
}

.feature-card {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  height: 100%;
  transition: all 0.3s ease;
  border: 1px solid #e2e8f0;
  position: relative;
  overflow: hidden;
}

.feature-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
  border-color: transparent;
}

.feature-icon {
  width: 56px;
  height: 56px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  color: #1a202c;
}

.bg-primary-soft {
  background-color: rgba(0, 170, 255, 0.1);
}

.bg-success-soft {
  background-color: rgba(16, 185, 129, 0.1);
}

.bg-warning-soft {
  background-color: rgba(245, 158, 11, 0.1);
}

.bg-info-soft {
  background-color: rgba(6, 182, 212, 0.1);
}

.bg-danger-soft {
  background-color: rgba(239, 68, 68, 0.1);
}

.bg-purple-soft {
  background-color: rgba(139, 92, 246, 0.1);
}

.feature-title {
  font-size: 1.25rem;
  font-weight: 600;
  color: #1a202c;
  margin-bottom: 1rem;
}

.feature-description {
  color: #4a5568;
  font-size: 0.875rem;
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.feature-link {
  color: #00aaff;
  text-decoration: none;
  font-weight: 500;
  font-size: 0.875rem;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
}

.feature-link:hover {
  color: #0088cc;
  gap: 0.75rem;
}

.features-cta {
  margin-top: 4rem;
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

@media (max-width: 991px) {
  .features-section {
    padding: 4rem 0;
  }

  .section-title {
    font-size: 2rem;
  }

  .feature-card {
    padding: 1.5rem;
  }
}
</style>
