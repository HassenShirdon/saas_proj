<template>
  <header class="topnav">
    <!-- Logo -->
    <div class="logo">
      <img src="@/assets/logo.png" alt="Logo" />
    </div>

    <!-- Search input center -->
    <div class="search-container">
      <input type="text" placeholder="Search products, orders..." class="search-input" />
    </div>

    <!-- User profile image & dropdown -->
    <div class="profile" @mouseenter="showDropdown = true" @mouseleave="showDropdown = false">
      <img src="@/assets/iconLogo.png" alt="User" class="avatar" />
      <transition name="fade">
        <div v-if="showDropdown" class="dropdown">
          <div class="username">
            {{ authStore.user && (authStore.user.name || authStore.user.username) ? (authStore.user.name ||
              authStore.user.username) : 'User' }}

          </div>
          <button @click="handleLogout" class="logout-btn" :disabled="isLoggingOut">
            {{ isLoggingOut ? 'Logging out...' : 'Logout' }}
          </button>
        </div>
      </transition>
    </div>
  </header>
</template>
<script setup>
import { ref } from 'vue'
import { storeToRefs } from 'pinia'
import { useAuthStore } from '@/stores/authStore'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()

// Use storeToRefs to keep user reactive
const { user } = storeToRefs(authStore)

const showDropdown = ref(false)
const isLoggingOut = ref(false)

async function handleLogout() {
  try {
    isLoggingOut.value = true
    showDropdown.value = false

    // Call the logout method from your auth store
    await authStore.logout()

    // Redirect to login page or home page after logout
    router.push('/signin')

    // Optional: Show success message
    // this.$toast.success('Logged out successfully')
  } catch (error) {
    console.error('Logout failed:', error)
    // Optional: Show error message
    // this.$toast.error('Logout failed. Please try again.')
  } finally {
    isLoggingOut.value = false
  }
}
</script>
<!-- }
</script> -->

<style scoped>
.topnav {
  width: 100vw;
  /* Force full viewport width */
  left: 0;
  right: 0;
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
  background-color: #ffffff;
  border-bottom: 1px solid #eaeaea;
  padding: 10px 24px;
  position: sticky;
  top: 0;
  z-index: 100;
  font-family: 'Inter', sans-serif;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.04);
}

.logo img {
  height: 42px;
}

.search-container {
  flex: 1;
  display: flex;
  justify-content: center;
}

.search-input {
  width: 60%;
  max-width: 480px;
  padding: 10px 18px;
  border-radius: 28px;
  border: 1px solid #d1d5db;
  font-size: 15px;
  transition:
    border-color 0.3s ease,
    box-shadow 0.3s ease;
  background-color: #f9fafb;
}

.search-input:focus {
  outline: none;
  border-color: #4f46e5;
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.2);
}

.profile {
  position: relative;
  cursor: pointer;
  display: flex;
  align-items: center;
}

.avatar {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #4f46e5;
  transition: transform 0.2s ease;
}

.avatar:hover {
  transform: scale(1.05);
}

.dropdown {
  position: absolute;
  top: 55px;
  right: 0;
  background: white;
  border-radius: 10px;
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.08);
  width: 170px;
  padding: 12px;
  display: flex;
  flex-direction: column;
  text-align: left;
  animation: dropdown-fade 0.3s ease;
}

.username {
  font-weight: 600;
  margin-bottom: 12px;
  font-size: 14px;
  color: #333;
}

.logout-btn {
  background: #4f46e5;
  color: white;
  padding: 8px 14px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
  transition: background 0.3s ease;
}

.logout-btn:hover:not(:disabled) {
  background: #4338ca;
}

.logout-btn:disabled {
  background: #9ca3af;
  cursor: not-allowed;
}

/* Dropdown Animation */
@keyframes dropdown-fade {
  from {
    opacity: 0;
    transform: translateY(-6px);
  }

  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Fade transition */
.fade-enter-active,
.fade-leave-active {
  transition: all 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-5px);
}
</style>
