<template>
    <section class="py-12 px-6 bg-gray-50">
        <div class="max-w-7xl mx-auto text-center mb-10">
            <h2 class="text-2xl font-bold text-blue-500 mb-2">Our Solutions</h2>
            <p class="text-gray-600">Marjaan Solutions provides powerful tools for logistics management.</p>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <!-- Inventory -->
            <Card class="shadow-lg rounded-2xl p-6 hover:shadow-xl transition">
                <div class="flex flex-col items-center text-center">
                    <i class="pi pi-box text-blue-500 text-4xl mb-4"></i>
                    <h3 class="text-lg font-semibold text-blue-500 mb-2">Inventory</h3>
                    <p class="text-gray-600 text-sm">Track, manage, and optimize your inventory efficiently to reduce
                        costs and improve logistics operations.</p>
                </div>
            </Card>

            <!-- HRM -->
            <Card class="shadow-lg rounded-2xl p-6 hover:shadow-xl transition">
                <div class="flex flex-col items-center text-center">
                    <i class="pi pi-users text-green-500 text-4xl mb-4"></i>
                    <h3 class="text-lg font-semibold text-blue-500 mb-2">HRM</h3>
                    <p class="text-gray-800 text-sm">Manage workforce, attendance, payroll, and employee performance
                        seamlessly with our HRM tools.</p>
                </div>
            </Card>

            <!-- Finance -->
            <Card class="shadow-lg rounded-2xl p-6 hover:shadow-xl transition">
                <div class="flex flex-col items-center text-center">
                    <i class="pi pi-wallet text-blue-500 text-4xl mb-4"></i>
                    <h3 class="text-lg font-semibold text-blue-500 mb-2">Finance</h3>
                    <p class="text-gray-600 text-sm">Simplify financial transactions, budgeting, invoicing, and cost
                        analysis for better decision-making.</p>
                </div>
            </Card>

            <!-- Report Generation -->
            <Card class="shadow-lg rounded-2xl p-6 hover:shadow-xl transition">
                <div class="flex flex-col items-center text-center">
                    <i class="pi pi-chart-bar text-blue-500 text-4xl mb-4"></i>
                    <h3 class="text-lg font-semibold text-blue-500 mb-2">Report Generation</h3>
                    <p class="text-gray-600 text-sm">Generate insightful reports and analytics to monitor logistics
                        performance and make informed decisions.</p>
                </div>
            </Card>
        </div>
    </section>
</template>

<script setup>
</script>
