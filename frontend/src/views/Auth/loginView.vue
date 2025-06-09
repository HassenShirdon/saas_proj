<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-6">
        <h2 class="text-center mb-4">Login Form</h2>

        <!-- Error message display -->
        <div v-if="errorMessage" class="alert alert-danger" role="alert">
          {{ errorMessage }}
        </div>

        <!-- Loading state -->
        <div v-if="isLoading" class="alert alert-info" role="alert">
          Logging in...
        </div>

        <form @submit.prevent="handleLogin">
          <div class="mb-3">
            <label for="username" class="form-label">Username</label>
            <input type="text" v-model="username" id="username" class="form-control" required :disabled="isLoading" />
          </div>
          <div class="mb-3">
            <label for="password" class="form-label">Password</label>
            <input type="password" v-model="password" id="password" class="form-control" required
              :disabled="isLoading" />
          </div>
          <button type="submit" class="btn btn-primary w-100" :disabled="isLoading">
            {{ isLoading ? 'Logging in...' : 'Login' }}
          </button>
        </form>
        <p class="mt-3 text-center">
          Don't have an account? <router-link to="/register">Register here</router-link>
        </p>
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
    console.log('Attempting login with:', { username: username.value });
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
.gradient-custom-2 {
  /* fallback for old browsers */
  background: #fccb90;

  /* Chrome 10-25, Safari 5.1-6 */
  background: -webkit-linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);

  /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
  background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593);
}

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