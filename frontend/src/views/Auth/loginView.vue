<template>
  <div class="login-bg d-flex align-items-center justify-content-center min-vh-100">
    <div class="login-card shadow-lg p-4 rounded-4 bg-white" style="max-width: 400px; width: 100%;">
      <div class="text-center mb-4">
        <h2 class="fw-bold mb-1">Sign in to your account</h2>
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

      <form @submit.prevent="login" autocomplete="on">
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
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { loginUser } from '@/api/auth'

const router = useRouter()
const username = ref('')
const password = ref('')
const errorMessage = ref('')
const isLoading = ref(false)

async function login() {
  errorMessage.value = ''
  isLoading.value = true
  try {
    const response = await loginUser({ username: username.value, password: password.value })
    // Save tokens and user info
    localStorage.setItem('access_token', response.access)
    localStorage.setItem('user', JSON.stringify(response.user))
    // Redirect based on user role
    const user = response.user
    if (user.is_superuser) {
      router.push('/superDashboard')
    } else if (user.is_tenant_admin) {
      window.location.href = `http://${user.domain}/tenantAdmin`
    } else {
      window.location.href = `http://${user.domain}/dashboard`
    }
  } catch (error) {
    errorMessage.value = error?.message || 'Login failed. Please try again.'
  } finally {
    isLoading.value = false
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