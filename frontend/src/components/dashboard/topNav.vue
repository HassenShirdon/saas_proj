<template>
  <header class="topnav">
    <div class="container-fluid">
      <!-- Logo on the left -->
      <div class="logo-section">
        <img src="@/assets/logo.png" alt="Logo" class="logo-img" />

      </div>

      <!-- Search in the middle -->
      <div class="search-section">
        <div class="search-wrapper">
          <i class="bi bi-search search-icon"></i>
          <input type="text" placeholder="Search products, orders, users..." class="search-input"
            v-model="searchQuery" />
        </div>
      </div>

      <div class="right-controls">
        <!-- Theme toggle button -->
        <button class="theme-toggle" @click="toggleTheme">
          <i class="bi" :class="isDarkMode ? 'bi-sun' : 'bi-moon'"></i>
        </button>
      </div>
      <!-- User profile on the right -->
      <div class="profile-section" @mouseenter="showDropdown = true" @mouseleave="showDropdown = false">
        <div class="user-info">
          <span class="user-name">{{ userName }}</span>
          <div class="avatar-wrapper">
            <img src="@/assets/iconLogo.png" alt="User Avatar" class="avatar" />
          </div>
          <i class="bi bi-chevron-down dropdown-arrow"></i>
        </div>

        <transition name="dropdown-fade">
          <div v-if="showDropdown" class="dropdown-menu">
            <div class="dropdown-header">
              <img src="@/assets/iconLogo.png" alt="User" class="dropdown-avatar" />
              <div class="user-details">
                <div class="dropdown-username">{{ userName }}</div>
                <div class="dropdown-email">admin@company.com</div>
              </div>
            </div>

            <div class="dropdown-divider"></div>

            <div class="dropdown-items">
              <router-link to="/profile" class="dropdown-item">
                <i class="bi bi-person"></i>
                <span>Profile</span>
              </router-link>

              <router-link to="/settings" class="dropdown-item">
                <i class="bi bi-gear"></i>
                <span>Settings</span>
              </router-link>

              <div class="dropdown-divider"></div>

              <button @click="handleLogout" class="dropdown-item logout-item" :disabled="isLoggingOut">
                <i class="bi bi-box-arrow-right"></i>
                <span>{{ isLoggingOut ? 'Logging out...' : 'Logout' }}</span>
              </button>
            </div>
          </div>
        </transition>
      </div>
    </div>
  </header>
</template>

<script setup>
import { ref, computed } from 'vue'
import { storeToRefs } from 'pinia'
import { useAuthStore } from '@/stores/authStore'
import { useRouter } from 'vue-router'

const authStore = useAuthStore()
const router = useRouter()
const { user } = storeToRefs(authStore)

const showDropdown = ref(false)
const isLoggingOut = ref(false)
const searchQuery = ref('')

const userName = computed(() => {
  return user.value && (user.value.name || user.value.username)
    ? (user.value.name || user.value.username)
    : 'Admin User'
})

async function handleLogout() {
  try {
    isLoggingOut.value = true
    showDropdown.value = false
    await authStore.logout()
    router.push('/login')
  } catch (error) {
    console.error('Logout failed:', error)
  } finally {
    isLoggingOut.value = false
  }
}
</script>
<style scoped>
.topnav {
  background: var(--topnav-bg);
  color: var(--topnav-color);
  padding: 0.75rem 1.5rem;
  position: fixed;
  top: 0;
  left: 280px;
  width: calc(100% - 280px);
  height: 64px;
  display: flex;
  align-items: center;
  z-index: 1020;
  border-bottom: 1px solid var(--border-color);
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.topnav.sidebar-collapsed {
  left: 80px;
  width: calc(100% - 80px);
}

.container-fluid {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  padding: 0;
}

/* Logo Section */
.logo-section {
  display: flex;
  align-items: center;
  gap: 12px;
}

.logo-img {
  height: 32px;
  width: auto;
  object-fit: contain;
}



/* Search Section */
.search-section {
  flex: 1;
  max-width: 500px;
  margin: 0 2rem;
}

.search-wrapper {
  position: relative;
  width: 100%;
}

.search-icon {
  position: absolute;
  left: 15px;
  top: 50%;
  transform: translateY(-50%);
  color: var(--text-muted);
  font-size: 0.9rem;
}

.search-input {
  width: 100%;
  padding: 0.5rem 1rem 0.5rem 2.5rem;
  border-radius: 8px;
  border: 1px solid var(--border-color);
  background: var(--search-bg);
  color: var(--text-color);
  transition: all 0.3s;
  font-size: 0.875rem;
  height: 38px;
}

.search-input:focus {
  outline: none;
  border-color: var(--primary-color);
  box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.15);
}

/* Profile Section */
.profile-section {
  position: relative;
}

.user-info {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  padding: 0.5rem 0.75rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s;
}

.user-info:hover {
  background: var(--dropdown-item-hover);
}

.user-name {
  font-weight: 500;
  font-size: 0.875rem;
  white-space: nowrap;
  color: var(--text-color);
}

.avatar-wrapper {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--avatar-bg);
}

.avatar {
  width: 32px;
  height: 32px;
  border-radius: 50%;
  object-fit: cover;
}

.dropdown-arrow {
  font-size: 0.75rem;
  color: var(--text-muted);
  transition: transform 0.2s;
}

.profile-section:hover .dropdown-arrow {
  transform: rotate(180deg);
}

/* Dropdown Menu */
.dropdown-menu {
  position: absolute;
  right: 0;
  top: calc(100% + 8px);
  min-width: 240px;
  background: var(--dropdown-bg);
  border-radius: 8px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  z-index: 1000;
  border: 1px solid var(--border-color);
}

.dropdown-header {
  display: flex;
  align-items: center;
  padding: 1rem;
  background: var(--dropdown-header-bg);
}

.dropdown-avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
  margin-right: 0.75rem;
  border: 2px solid var(--dropdown-avatar-border);
}

.user-details {
  flex: 1;
}

.dropdown-username {
  font-weight: 600;
  margin-bottom: 0.25rem;
  font-size: 0.875rem;
  color: var(--text-color);
}

.dropdown-email {
  font-size: 0.75rem;
  color: var(--text-muted);
}

.dropdown-divider {
  height: 1px;
  background: var(--border-color);
  margin: 0;
}

.dropdown-items {
  padding: 0.5rem 0;
}

.dropdown-item {
  display: flex;
  align-items: center;
  padding: 0.5rem 1rem;
  color: var(--text-color);
  text-decoration: none;
  transition: all 0.2s;
  font-size: 0.875rem;
}

.dropdown-item i {
  margin-right: 0.75rem;
  width: 20px;
  text-align: center;
  font-size: 0.9rem;
}

.dropdown-item:hover {
  background: var(--dropdown-item-hover);
  color: var(--primary-color);
}

.logout-item {
  width: 100%;
  text-align: left;
  background: none;
  border: none;
  color: var(--danger);
}

.logout-item:hover {
  color: var(--danger-dark);
}

.logout-item:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Animations */
.dropdown-fade-enter-active,
.dropdown-fade-leave-active {
  transition: all 0.2s ease;
}

.dropdown-fade-enter-from,
.dropdown-fade-leave-to {
  opacity: 0;
  transform: translateY(-5px);
}

/* Dark Mode Variables */
.dark-mode .topnav {
  --topnav-bg: #1e293b;
  --topnav-color: #f8fafc;
  --search-bg: #334155;
  --border-color: rgba(255, 255, 255, 0.1);
  --dropdown-bg: #334155;
  --dropdown-header-bg: #1e293b;
  --dropdown-avatar-border: #1e293b;
  --dropdown-item-hover: rgba(255, 255, 255, 0.08);
  --text-muted: #94a3b8;
  --avatar-bg: #475569;
}

/* Light Mode Variables */
:root {
  --topnav-bg: #ffffff;
  --topnav-color: #000;
  --search-bg: #f8fafc;
  --border-color: rgba(0, 0, 0, 0.1);
  --dropdown-bg: #ffffff;
  --dropdown-header-bg: #f8fafc;
  --dropdown-avatar-border: #ffffff;
  --dropdown-item-hover: rgba(0, 0, 0, 0.05);
  --text-muted: #64748b;
  --primary-color: #4f46e5;
  --danger: #ef4444;
  --danger-dark: #dc2626;
  --text-color: #1e293b;
  --avatar-bg: #e2e8f0;
}

/* Responsive Design */
@media (max-width: 992px) {
  .topnav {
    left: 0;
    width: 100%;
  }

  .search-section {
    margin: 0 1rem;
  }

  .user-name {
    display: none;
  }
}

@media (max-width: 768px) {
  .topnav {
    padding: 0.75rem 1rem;
  }

  .search-section {
    margin: 0 0.5rem;
    max-width: 200px;
  }

  .dropdown-menu {
    min-width: 200px;
  }
}
</style>