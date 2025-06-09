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

            <div class="pricing-toggle text-center mb-5">
                <div class="form-check form-switch d-inline-block">
                    <input class="form-check-input" type="checkbox" id="billingToggle">
                    <label class="form-check-label" for="billingToggle">
                        <span class="billing-label">Monthly</span>
                        <span class="billing-label">Yearly</span>
                        <span class="billing-save">Save 20%</span>
                    </label>
                </div>
            </div>

            <div class="row justify-content-center g-4">
                <!-- Basic Plan -->
                <div class="col-lg-4 col-md-6">
                    <div class="pricing-card">
                        <div class="pricing-header">
                            <h3>Business Suite</h3>
                            <div class="price">
                                <span class="currency">$</span>
                                <span class="amount">100</span>
                                <span class="period">/month</span>
                            </div>
                            <p class="pricing-subtitle">Perfect for growing businesses</p>
                        </div>
                        <div class="pricing-body">
                            <ul class="features-list">
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Unlimited Inventory Items</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Supplier Management</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Purchase Order Tracking</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Employee Database</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Time & Attendance</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Payroll Integration</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Basic Reporting</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>24/7 Email Support</span>
                                </li>
                            </ul>
                            <a href="#contact" class="btn btn-outline-primary w-100">Get Started</a>
                        </div>
                    </div>
                </div>

                <!-- Premium Plan -->
                <div class="col-lg-4 col-md-6">
                    <div class="pricing-card popular">
                        <div class="popular-badge">Most Popular</div>
                        <div class="pricing-header">
                            <h3>Enterprise Suite</h3>
                            <div class="price">
                                <span class="currency">$</span>
                                <span class="amount">200</span>
                                <span class="period">/month</span>
                            </div>
                            <p class="pricing-subtitle">For established enterprises</p>
                        </div>
                        <div class="pricing-body">
                            <ul class="features-list">
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>All Business Suite Features</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Accounting Dashboard</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Accounts Payable/Receivable</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Financial Reporting</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Tax Management</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Budgeting Tools</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Multi-Currency Support</span>
                                </li>
                                <li>
                                    <i class="bi bi-check-circle-fill"></i>
                                    <span>Priority Phone Support</span>
                                </li>
                            </ul>
                            <a href="#contact" class="btn btn-primary w-100">Get Started</a>
                        </div>
                    </div>
                </div>
            </div>

            <div class="pricing-footer text-center mt-5">
                <p class="text-muted">Need a custom plan? <a href="#contact" class="text-primary">Contact us</a> for a
                    tailored solution.</p>
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
    background: linear-gradient(to bottom, #ffffff, #f8fafc);
}

.section-header {
    margin-bottom: 3rem;
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

.pricing-toggle {
    margin-bottom: 3rem;
}

.form-switch {
    padding-left: 3rem;
}

.form-check-input {
    width: 3rem;
    height: 1.5rem;
    margin-left: -3rem;
    background-color: #e2e8f0;
    border-color: #e2e8f0;
}

.form-check-input:checked {
    background-color: #00aaff;
    border-color: #00aaff;
}

.billing-label {
    font-weight: 500;
    color: #4a5568;
    margin: 0 0.5rem;
}

.billing-save {
    background: #00aaff;
    color: white;
    padding: 0.25rem 0.75rem;
    border-radius: 50px;
    font-size: 0.75rem;
    font-weight: 600;
    margin-left: 0.5rem;
}

.pricing-card {
    background: white;
    border-radius: 16px;
    overflow: hidden;
    transition: all 0.3s ease;
    border: 1px solid #e2e8f0;
    position: relative;
    height: 100%;
}

.pricing-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08);
}

.pricing-card.popular {
    border: 2px solid #00aaff;
}

.popular-badge {
    position: absolute;
    top: 1rem;
    right: 1rem;
    background: #00aaff;
    color: white;
    padding: 0.5rem 1rem;
    border-radius: 50px;
    font-size: 0.875rem;
    font-weight: 600;
}

.pricing-header {
    padding: 2rem;
    text-align: center;
    background: linear-gradient(135deg, #f8fafc, #ffffff);
    border-bottom: 1px solid #e2e8f0;
}

.pricing-header h3 {
    font-size: 1.5rem;
    font-weight: 600;
    color: #1a202c;
    margin-bottom: 1rem;
}

.price {
    margin: 1.5rem 0;
}

.currency {
    font-size: 1.5rem;
    font-weight: 600;
    color: #1a202c;
    vertical-align: top;
}

.amount {
    font-size: 3.5rem;
    font-weight: 700;
    color: #1a202c;
    line-height: 1;
}

.period {
    font-size: 1rem;
    color: #4a5568;
}

.pricing-subtitle {
    color: #4a5568;
    font-size: 0.875rem;
    margin: 0;
}

.pricing-body {
    padding: 2rem;
}

.features-list {
    list-style: none;
    padding: 0;
    margin: 0 0 2rem 0;
}

.features-list li {
    display: flex;
    align-items: center;
    padding: 0.75rem 0;
    color: #4a5568;
}

.features-list li i {
    color: #00aaff;
    margin-right: 0.75rem;
    font-size: 1.125rem;
}

.btn-primary {
    background: #00aaff;
    border: none;
    color: white;
    padding: 1rem;
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

.btn-outline-primary {
    background: transparent;
    border: 2px solid #00aaff;
    color: #00aaff;
    padding: 1rem;
    border-radius: 12px;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-outline-primary:hover {
    background: #00aaff;
    color: white;
    transform: translateY(-2px);
}

.pricing-footer {
    margin-top: 3rem;
}

.pricing-footer a {
    color: #00aaff;
    text-decoration: none;
    font-weight: 500;
}

.pricing-footer a:hover {
    text-decoration: underline;
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
    }
}
</style>
