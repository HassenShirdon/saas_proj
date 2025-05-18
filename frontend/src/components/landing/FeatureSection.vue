<template>
  <section class="py-5 bg-light position-relative overflow-hidden">
    <div class="container text-center">
      <h2 class="fw-bold mb-3 display-5">Supercharge Your Business</h2>
      <p class="text-muted mb-5 lead">
        A powerful suite of tools designed to help your operations thrive.
      </p>

      <div class="row g-4">
        <div
          v-for="(feature, index) in features"
          :key="index"
          class="col-md-6 col-lg-4"
          :data-aos="'fade-up'"
          :data-aos-delay="index * 100"
        >
          <div class="card h-100 border-0 shadow-sm bg-white rounded-4 p-4">
            <div :class="['icon mb-3 fs-1', feature.iconColor]">
              <i :class="feature.icon"></i>
            </div>
            <h5 class="fw-semibold">{{ feature.title }}</h5>
            <p class="text-muted">{{ feature.description }}</p>
          </div>
        </div>
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
    AOS.init()
  },
  data() {
    return {
      features: [
        {
          icon: 'bi bi-people',
          iconColor: 'text-primary',
          title: 'HR Management',
          description:
            'Smart tools to manage employee data, payroll, and attendance in one dashboard.',
        },
        {
          icon: 'bi bi-cash-stack',
          iconColor: 'text-success',
          title: 'Finance Module',
          description:
            'Track income & expenses, generate smart insights and financial reports with ease.',
        },
        {
          icon: 'bi bi-box-seam',
          iconColor: 'text-warning',
          title: 'Inventory System',
          description:
            'Track stock, reorder products, and stay updated with real-time inventory levels.',
        },

        {
          icon: 'bi bi-kanban',
          iconColor: 'text-info',
          title: 'Project Management',
          description: 'Organize tasks, timelines, and teams in a sleek drag-and-drop interface.',
        },
        {
          icon: 'bi bi-shield-lock',
          iconColor: 'text-dark',
          title: 'Security & Access',
          description:
            'Set roles, control permissions, and secure your data with advanced features.',
        },
      ],
    }
  },
}
</script>

<style scoped>
.card:hover {
  transform: translateY(-5px);
  transition: all 0.3s ease;
}
.card .icon {
  transition: transform 0.3s;
}
.card:hover .icon {
  transform: scale(1.2);
}
</style>
