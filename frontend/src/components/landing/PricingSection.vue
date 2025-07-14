<template>
    <!-- Pricing Section -->
    <section class="pricing-section">
        <div class="container">
            <div class="section-header text-center">
                <span class="badge bg-primary-soft mb-3">Pricing</span>
                <h2 class="section-title">Simple, Transparent Pricing</h2>
                <p class="section-description">
                    Choose the perfect plan for your business needs
                </p>
            </div>

            <div class="row justify-content-center g-4">
                <!-- Standard Plan -->
                <div class="col-lg-5 col-md-6">
                    <div class="pricing-card">
                        <div class="pricing-header">
                            <h3>Standard Suite</h3>
                            <div class="price">
                                <span class="currency">$</span>
                                <span class="amount">200</span>
                                <span class="period">/month</span>
                            </div>
                            <p class="pricing-subtitle">Inventory, HRM &amp; Accounting</p>
                        </div>
                        <div class="pricing-body">
                            <ul class="features-list">
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Inventory Management</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Human Resource Management</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Accounting Dashboard</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Basic Reporting &amp; Analytics</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Email Support</span>
                                </li>
                            </ul>
                            <a href="#contact" class="btn btn-outline-primary w-100">Get Started</a>
                        </div>
                    </div>
                </div>

                <!-- Premium Plan -->
                <div class="col-lg-5 col-md-6">
                    <div class="pricing-card premium">
                        <div class="premium-badge">Premium</div>
                        <div class="pricing-header">
                            <h3>Premium Suite</h3>
                            <div class="price">
                                <span class="currency">$</span>
                                <span class="amount">350</span>
                                <span class="period">/month</span>
                            </div>
                            <p class="pricing-subtitle">All Standard Features + AI Document Storage</p>
                        </div>
                        <div class="pricing-body">
                            <ul class="features-list">
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>All Standard Suite Features</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Document Storage &amp; Retrieval</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>AI-powered Informational Prompts</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Advanced Analytics</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Priority Support</span>
                                </li>
                            </ul>
                            <a href="#contact" class="btn btn-primary w-100">Get Started</a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="pricing-footer text-center mt-5">
                <p class="text-dark">
                    Need a custom plan?
                    <a href="#contact" class="text-primary">Contact us</a> for a tailored solution.
                </p>
            </div>
        </div>
    </section>
</template>

<script>
export default {
    name: 'PricingSection'
}
</script>

<style scoped>
.pricing-section {
    padding: 6rem 0;
    background: #F0F0F0;
}

.section-header {
    margin-bottom: 3rem;
}

.badge {
    padding: 0.5rem 1rem;
    font-weight: 600;
    font-size: 0.95rem;
    border-radius: 50px;
    background: #e0e0e0;
    color: #005fa3;
    letter-spacing: 0.5px;
}

.bg-primary-soft {
    background-color: #e0e0e0 !important;
    color: #005fa3 !important;
}

.section-title {
    font-size: 2.7rem;
    font-weight: 800;
    color: #222;
    margin-bottom: 1rem;
    letter-spacing: -1px;
}

.section-description {
    font-size: 1.15rem;
    color: #333;
    max-width: 600px;
    margin: 0 auto;
}

.row {
    gap: 2rem 0;
}

.pricing-card {
    background: #fff;
    border-radius: 20px;
    overflow: hidden;
    transition: box-shadow 0.3s, transform 0.3s;
    border: 2px solid #F0F0F0;
    box-shadow: 0 6px 32px rgba(0, 0, 0, 0.07);
    position: relative;
    height: 100%;
    display: flex;
    flex-direction: column;
    min-height: 520px;
    color: #222;
}

.pricing-card:hover {
    transform: translateY(-8px) scale(1.02);
    box-shadow: 0 16px 48px rgba(0, 0, 0, 0.13);
}

.pricing-card.premium {
    border: 2px solid #005fa3;
    background: #f7fbff;
}

.premium-badge {
    position: absolute;
    top: 1.5rem;
    right: 1.5rem;
    background: #005fa3;
    color: #fff;
    padding: 0.5rem 1.2rem;
    border-radius: 50px;
    font-size: 1rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    box-shadow: 0 2px 8px rgba(0, 95, 163, 0.12);
    z-index: 2;
}

.pricing-header {
    padding: 2.5rem 2rem 1.5rem 2rem;
    text-align: center;
    background: #F0F0F0;
    border-bottom: 1px solid #e2e8f0;
    color: #222;
}

.pricing-header h3 {
    font-size: 1.6rem;
    font-weight: 700;
    color: #005fa3;
    margin-bottom: 1.2rem;
    letter-spacing: -0.5px;
}

.price {
    margin: 1.2rem 0 0.7rem 0;
    display: flex;
    align-items: baseline;
    justify-content: center;
    gap: 0.3rem;
}

.currency {
    font-size: 1.3rem;
    font-weight: 600;
    color: #005fa3;
    vertical-align: top;
}

.amount {
    font-size: 3.2rem;
    font-weight: 800;
    color: #005fa3;
    line-height: 1;
    letter-spacing: -1px;
    text-shadow: none;
}

.period {
    font-size: 1.1rem;
    color: #333;
    margin-left: 0.2rem;
}

.pricing-subtitle {
    color: #444;
    font-size: 1rem;
    margin: 0;
    font-weight: 500;
}

.pricing-body {
    padding: 2rem 2rem 2.5rem 2rem;
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.features-list {
    list-style: none;
    padding: 0;
    margin: 0 0 2rem 0;
}

.features-list li {
    display: flex;
    align-items: center;
    padding: 0.7rem 0;
    color: #222;
    font-size: 1.07rem;
    font-weight: 600;
    background: #F0F0F0;
    border-radius: 8px;
    margin-bottom: 0.5rem;
    padding: 0.5rem 0.8rem;
}

.features-list li i {
    color: #005fa3;
    margin-right: 0.8rem;
    font-size: 1.2rem;
}

.btn-primary {
    background: #005fa3;
    border: none;
    color: #fff;
    padding: 1rem;
    border-radius: 14px;
    font-weight: 700;
    font-size: 1.1rem;
    transition: all 0.3s;
    box-shadow: 0 4px 16px rgba(0, 95, 163, 0.13);
}

.btn-primary:hover {
    background: #003366;
    color: #fff;
    transform: translateY(-2px) scale(1.03);
    box-shadow: 0 8px 24px rgba(0, 95, 163, 0.18);
}

.btn-outline-primary {
    background: #fff;
    border: 2px solid #005fa3;
    color: #005fa3;
    padding: 1rem;
    border-radius: 14px;
    font-weight: 700;
    font-size: 1.1rem;
    transition: all 0.3s;
}

.btn-outline-primary:hover {
    background: #005fa3;
    color: #fff;
    transform: translateY(-2px) scale(1.03);
}

.pricing-footer {
    margin-top: 3rem;
    color: #222;
    background: #F0F0F0;
    padding: 1.5rem 0;
    border-radius: 12px;
    box-shadow: 0 2px 12px rgba(0, 95, 163, 0.07);
}

.pricing-footer a {
    color: #005fa3;
    text-decoration: none;
    font-weight: 700;
    transition: color 0.2s;
}

.pricing-footer a:hover {
    text-decoration: underline;
    color: #003366;
}

@media (max-width: 991px) {
    .pricing-section {
        padding: 4rem 0;
    }

    .section-title {
        font-size: 2rem;
    }

    .pricing-card {
        margin-bottom: 2rem;
        min-height: unset;
    }
}
</style>
