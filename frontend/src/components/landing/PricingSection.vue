<template>
    <!-- Pricing Section -->
    <section class="pricing-section">
        <div class="container">
            <div class="row justify-content-center">
                <!-- Basic Plan -->
                <div class="col-lg-5 col-md-6 mb-4">
                    <div class="pricing-card h-100">
                        <div class="pricing-header">
                            <h4>Business Suite</h4>
                            <div class="price">$100<span>/month</span></div>
                            <p>Inventory + HR Management</p>
                        </div>
                        <div class="pricing-body">
                            <ul class="features-list">
                                <li>Unlimited Inventory Items</li>
                                <li>Supplier Management</li>
                                <li>Purchase Order Tracking</li>
                                <li>Employee Database</li>
                                <li>Time & Attendance</li>
                                <li>Payroll Integration</li>
                                <li>Basic Reporting</li>
                                <li>24/7 Email Support</li>
                            </ul>
                            <button class="btn btn-primary">Get Started</button>
                        </div>
                    </div>
                </div>

                <!-- Premium Plan -->
                <div class="col-lg-5 col-md-6 mb-4">
                    <div class="pricing-card h-100">
                        <div class="popular-badge">MOST POPULAR</div>
                        <div class="pricing-header">
                            <h4>Enterprise Suite</h4>
                            <div class="price">$200<span>/month</span></div>
                            <p>Everything in Business + Finance</p>
                        </div>
                        <div class="pricing-body">
                            <ul class="features-list">
                                <li>All Business Suite Features</li>
                                <li>Accounting Dashboard</li>
                                <li>Accounts Payable/Receivable</li>
                                <li>Financial Reporting</li>
                                <li>Tax Management</li>
                                <li>Budgeting Tools</li>
                                <li>Multi-Currency Support</li>
                                <li>Priority Phone Support</li>
                            </ul>
                            <button class="btn btn-primary">Get Started</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>


</template>
<script></script>
<style>
.pricing-section {
    padding: 80px 0;
    background-color: #f5f7ff;
}

.pricing-card {
    border: none;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
    transition: all 0.3s ease;
    background: white;
    position: relative;
}

.pricing-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(67, 97, 238, 0.15);
}

.pricing-header {
    padding: 30px;
    background: linear-gradient(135deg, #4361ee, #3f37c9);
    color: white;
    text-align: center;
}

.pricing-header h4 {
    font-weight: 600;
    margin-bottom: 10px;
    font-size: 1.5rem;
}

.pricing-header .price {
    font-size: 3rem;
    font-weight: 700;
    margin: 20px 0;
}

.pricing-header .price span {
    font-size: 1rem;
    font-weight: 400;
}

.pricing-body {
    padding: 30px;
}

.features-list {
    list-style: none;
    padding: 0;
    margin-bottom: 30px;
}

.features-list li {
    padding: 8px 0;
    position: relative;
    padding-left: 30px;
}

.features-list li:before {
    content: "\f00c";
    font-family: "Font Awesome 6 Free";
    font-weight: 900;
    color: #4bb543;
    position: absolute;
    left: 0;
}

.popular-badge {
    position: absolute;
    top: -15px;
    right: 20px;
    background-color: #4cc9f0;
    color: white;
    padding: 5px 15px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    box-shadow: 0 4px 10px rgba(76, 201, 240, 0.3);
}

.btn-primary {
    background-color: #4361ee;
    border-color: #4361ee;
    padding: 10px 25px;
    border-radius: 8px;
    font-weight: 500;
    width: 100%;
}

.btn-primary:hover {
    background-color: #3f37c9;
    border-color: #3f37c9;
}
</style>
