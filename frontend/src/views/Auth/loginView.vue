<template>
  <div class="login-bg d-flex align-items-center justify-content-center min-vh-100">
    <div class="login-card shadow-lg p-4 rounded-4 bg-white" style="max-width: 400px; width: 100%;">
      <div class="text-center mb-4">
        <h2 class="fw-bold mb-1">Sign in to your account</h2>
        <p class="text-muted small">Welcome back! Please enter your details.</p>
      </div>

      <!-- Error message display -->
      <transition name="fade">
        <div v-if="errorMessage" class="alert alert-danger py-2 px-3" role="alert">
          {{ errorMessage }}
        </div>
      </transition>

      <!-- Loading state -->
      <transition name="fade">
        <div v-if="isLoading" class="alert alert-info py-2 px-3" role="alert">
          Logging in...
        </div>
      </transition>

      <form @submit.prevent="handleLogin" autocomplete="on">
        <div class="mb-3">
          <label for="username" class="form-label fw-semibold">Username</label>
          <input type="text" v-model="username" id="username" class="form-control modern-input" required
            :disabled="isLoading" autocomplete="username" placeholder="Enter your username" />
        </div>
        <div class="mb-3">
          <label for="password" class="form-label fw-semibold">Password</label>
          <input type="password" v-model="password" id="password" class="form-control modern-input" required
            :disabled="isLoading" autocomplete="current-password" placeholder="Enter your password" />
        </div>
        <button type="submit" class="btn btn-primary w-100 py-2 rounded-3 fw-semibold" :disabled="isLoading">
          <span v-if="isLoading">
            <span class="spinner-border spinner-border-sm me-2"></span>
            Logging in...
          </span>
          <span v-else>signin</span>
        </button>
      </form>
      <div class="mt-4 text-center">
        <span class="text-muted">Don't have an account?</span>
        <router-link to="/register" class="ms-1 fw-semibold text-decoration-none modern-link">
          Register here
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '@/stores/authStore';

const username = ref('');
const password = ref('');
const errorMessage = ref('');
const isLoading = ref(false);
const auth = useAuthStore();

async function handleLogin() {
  // Reset error message
  errorMessage.value = '';
  isLoading.value = true;

  try {
    // console.log('Attempting login with:', { username: username.value });
    await auth.login({ username: username.value, password: password.value });
    // Login successful - auth store will handle redirect
  } catch (error) {
    console.error('Login failed:', error);

    // More detailed error handling
    if (error.response) {
      // Server responded with error status
      const status = error.response.status;
      const data = error.response.data;

      if (status === 401) {
        errorMessage.value = 'Invalid username or password';
      } else if (status === 400) {
        // Handle validation errors
        if (data.username) {
          errorMessage.value = `Username: ${data.username.join(', ')}`;
        } else if (data.password) {
          errorMessage.value = `Password: ${data.password.join(', ')}`;
        } else if (data.detail) {
          errorMessage.value = data.detail;
        } else {
          errorMessage.value = 'Please check your input and try again';
        }
      } else if (status >= 500) {
        errorMessage.value = 'Server error. Please try again later.';
      } else {
        errorMessage.value = data.detail || 'Login failed. Please try again.';
      }
    } else if (error.request) {
      // Network error
      errorMessage.value = 'Network error. Please check your connection.';
    } else {
      // Other error
      errorMessage.value = 'An unexpected error occurred. Please try again.';
    }
  } finally {
    isLoading.value = false;
  }
}
</script>

<style scoped>
@media (min-width: 768px) {
  .gradient-form {
    height: 100vh !important;
  }
}

@media (min-width: 769px) {
  .gradient-custom-2 {
    border-top-right-radius: 0.3rem;
    border-bottom-right-radius: 0.3rem;
  }
}

.card-body {
  display: flex;
  align-items: center;
  justify-content: center;
}

.alert {
  margin-bottom: 1rem;
}
</style>