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
          <div class="username">John Doe</div>
          <button @click="logout" class="logout-btn">Logout</button>
        </div>
      </transition>
    </div>
  </header>
</template>

<script>
export default {
  data() {
    return {
      showDropdown: false,
    }
  },
  methods: {
    logout() {
      // Your logout logic here
      console.log('Logging out...')
    },
  },
}
</script>

<style scoped>
.topnav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 64px;
  background-color: #ffffff;
  border-bottom: 1px solid #e0e0e0;
  padding: 0 20px;
  position: sticky;
  top: 0;
  z-index: 100;
}

.logo img {
  height: 40px;
}

.search-container {
  flex: 1;
  display: flex;
  justify-content: center;
}

.search-input {
  width: 60%;
  max-width: 500px;
  padding: 10px 16px;
  border-radius: 20px;
  border: 1px solid #ccc;
  outline: none;
  font-size: 14px;
}

.profile {
  position: relative;
  cursor: pointer;
}

.avatar {
  width: 40px;
  height: 40px;
  border-radius: 50%;
  object-fit: cover;
}

.dropdown {
  position: absolute;
  top: 50px;
  right: 0;
  background: white;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  width: 150px;
  padding: 10px;
  display: flex;
  flex-direction: column;
  text-align: left;
}

.username {
  font-weight: bold;
  margin-bottom: 10px;
}

.logout-btn {
  background: #1976d2;
  color: white;
  padding: 6px 12px;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-size: 14px;
}

.logout-btn:hover {
  background: #125aa2;
}

/* Fade animation */
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
