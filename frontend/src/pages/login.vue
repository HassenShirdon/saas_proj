<template>
    <div class="min-h-screen flex items-center justify-center bg-gray-100 dark:bg-gray-900 px-4">
        <div class="w-full max-w-md bg-white dark:bg-gray-800 shadow-lg rounded-2xl p-8">
            <!-- Logo / Title -->
            <div class="text-center mb-6">
                <h1 class="text-3xl font-bold text-gray-900 dark:text-white">
                    Welcome Back
                </h1>
                <p class="text-gray-500 dark:text-gray-400 text-sm mt-2">
                    Sign in to your account
                </p>
            </div>

            <!-- Error Alert -->
            <div v-if="authStore.error" class="mb-4 p-3 rounded-lg bg-red-100 text-red-700 text-sm">
                {{ authStore.error }}
            </div>

            <!-- Login Form -->
            <form @submit.prevent="handleLogin" class="space-y-4">
                <!-- Username -->
                <div>
                    <label for="username" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                        Username
                    </label>
                    <input v-model="credentials.username" type="text" id="username"
                        class="mt-1 block w-full rounded-lg border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-accent focus:ring-accent sm:text-sm"
                        required />
                </div>

                <!-- Password -->
                <div>
                    <label for="password" class="block text-sm font-medium text-gray-700 dark:text-gray-300">
                        Password
                    </label>
                    <input v-model="credentials.password" type="password" id="password"
                        class="mt-1 block w-full rounded-lg border-gray-300 dark:border-gray-600 dark:bg-gray-700 dark:text-white shadow-sm focus:border-accent focus:ring-accent sm:text-sm"
                        required />
                </div>

                <!-- Submit Button -->
                <button type="submit" :disabled="authStore.isLoading"
                    class="w-full py-2 px-4 rounded-lg bg-accent text-white font-medium hover:bg-accent-dark focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-accent transition">
                    <span v-if="authStore.isLoading" class="pi pi-spin pi-spinner mr-2"></span>
                    {{ authStore.isLoading ? "Signing in..." : "Sign In" }}
                </button>
            </form>

            <!-- Footer -->
            <p class="mt-6 text-center text-sm text-gray-500 dark:text-gray-400">
                Don’t have an account?
                <router-link to="/register" class="text-accent font-medium hover:underline">
                    Register
                </router-link>
            </p>
        </div>
    </div>
</template>

<script setup>
import { reactive } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/authStore"; // Pinia store

const router = useRouter();
const authStore = useAuthStore();

// Form state
const credentials = reactive({
    username: "",
    password: "",
});

// Login handler
const handleLogin = async () => {
    try {
        const role = await authStore.login(credentials);

        // Redirect based on role
        if (role === "admin") {
            router.push("/adminDashboard");
        } else if (role === "tenant") {
            router.push("/TenantAdminDashboard");
        } else if (role === "customer") {
            router.push("/CustomerDashboard");
        } else {
            router.push("/"); // fallback
        }
    } catch (err) {
        console.error(err);
    }
};
</script>
