<template>
  <!-- About Section: Introduces the company and highlights core services -->
  <section class="py-5 bg-white about-section">
    <div class="container">
      <div class="row align-items-center">
        <!-- ===== TEXTUAL CONTENT ===== -->
        <div class="col-lg-6 mb-4 mb-lg-0">
          <!-- Main Heading -->
          <h2 class="display-5 fw-bold mb-3">About Marjaan Solutions</h2>

          <!-- Intro Description -->
          <p class="lead text-muted">
            Marjaan Solutions is a forward-thinking logistics software company dedicated to helping
            businesses modernize and automate their operations through modular, easy-to-integrate
            SaaS solutions.
          </p>

          <!-- Key Focus Statement -->
          <p class="text-muted">
            Our primary focus lies in delivering intelligent <strong>Inventory</strong> and
            <strong>Finance</strong> tools tailored for growing businesses. We unify complex
            operational processes into a single, elegant interface.
          </p>

          <!-- Highlighted Features List -->
          <ul class="list-unstyled mt-4">
            <li class="d-flex align-items-start mb-2">
              <i class="bi bi-check-circle-fill text-primary me-2"></i>
              <span
                ><strong>Inventory System</strong>: Real-time tracking, automated restocking,
                supplier integrations, and stock-level alerts to keep your products flowing
                efficiently.</span
              >
            </li>
            <li class="d-flex align-items-start mb-2">
              <i class="bi bi-check-circle-fill text-success me-2"></i>
              <span
                ><strong>Finance Module</strong>: Powerful insights on your revenue, expenses, and
                profitability. Built-in reporting, invoice tracking, and cost forecasting
                included.</span
              >
            </li>
            <li class="d-flex align-items-start mb-2">
              <i class="bi bi-check-circle-fill text-dark me-2"></i>
              <span
                >HR, Project Management, and Access Control modules to complement the core
                systems.</span
              >
            </li>
          </ul>
        </div>

        <!-- ===== IMAGE/ILLUSTRATION SECTION ===== -->
        <div class="col-lg-6 text-center">
          <!-- Replace placeholder with custom illustration or dashboard screenshot -->
          <img
            src="@/assets/aboutus.png"
            alt="Marjaan Solutions Interface"
            class="img-fluid rounded shadow"
          />
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
/* Section Background Enhancement */
.about-section {
  background: linear-gradient(to right, #f8f9fa, #ffffff);
}

/* Headline Styling */
.about-section h2 {
  color: #0d6efd;
}

/* Hover Scale Effect for Image */
.about-section img {
  transition: transform 0.3s ease;
}
.about-section img:hover {
  transform: scale(1.03);
}

/* Optional: Highlight text within lists */
.about-section ul li strong {
  color: #212529;
}
</style>
