<template>
    <footer class="footer">
        <div class="footer-container">
            <!-- SaaS Links -->
            <div class="footer-column">
                <h3>SaaS Links</h3>
                <ul>
                    <li><a href="/features">Features</a></li>
                    <li><a href="/pricing">Pricing</a></li>
                    <li><a href="/about">About Us</a></li>
                    <li><a href="/faq">FAQ</a></li>
                </ul>
            </div>
            <!-- Social Icons -->
            <div class="footer-column">
                <h3>Follow Us</h3>
                <div class="social-icons">
                    <a href="https://twitter.com/" target="_blank" aria-label="Twitter">
                        <i class="fab fa-twitter"></i>
                    </a>
                    <a href="https://facebook.com/" target="_blank" aria-label="Facebook">
                        <i class="fab fa-facebook"></i>
                    </a>
                    <a href="https://linkedin.com/" target="_blank" aria-label="LinkedIn">
                        <i class="fab fa-linkedin"></i>
                    </a>
                </div>
            </div>
            <!-- Contacts -->
            <div class="footer-column">
                <h3>Contact Us</h3>
                <ul>
                    <li>Email: <a href="mailto:info@marjaan.com">info@marjaan.com</a></li>
                    <li>Phone: <a href="tel:+1234567890">+1 234 567 890</a></li>
                    <li>Address: 123 Main St, City, Country</li>
                </ul>
            </div>
        </div>
    </footer>
</template>

<script>
export default {
    name: "FooterSection"
};
</script>

<style scoped>
.footer {
    background: #222;
    color: #fff;
    padding: 40px 0;
}

.footer-container {
    display: flex;
    justify-content: space-between;
    max-width: 1100px;
    margin: 0 auto;
    flex-wrap: wrap;
}

.footer-column {
    flex: 1 1 250px;
    margin: 0 20px;
}

.footer-column h3 {
    margin-bottom: 16px;
    font-size: 18px;
    color: #ffd700;
}

.footer-column ul {
    list-style: none;
    padding: 0;
}

.footer-column ul li {
    margin-bottom: 10px;
}

.footer-column a {
    color: #fff;
    text-decoration: none;
}

.footer-column a:hover {
    text-decoration: underline;
}

.social-icons a {
    margin-right: 15px;
    font-size: 22px;
    color: #fff;
    transition: color 0.2s;
}

.social-icons a:hover {
    color: #ffd700;
}

@media (max-width: 768px) {
    .footer-container {
        flex-direction: column;
        align-items: center;
    }

    .footer-column {
        margin-bottom: 30px;
        text-align: center;
    }
}
</style>
