<template>
  <div class="main-container">
    <!-- Top Navigation -->
    <nav class="top-nav">
      <div class="nav-left">
        <button class="menu-btn" @click="$emit('toggleSidebar')">
          <span class="menu-icon">&#9776;</span>
        </button>
        <span class="brand">Dashboard</span>
      </div>
      <div class="nav-right">
        <input class="search-input" type="text" placeholder="Search..." />
        <img class="avatar" src="https://ui-avatars.com/api/?name=User" alt="User" />
      </div>
    </nav>

    <!-- Main Content Area -->
    <div class="main-content container-fluid px-2 px-md-4">
      <div class="table-responsive">
        <router-view />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "MainArea"
};
</script>

<style scoped>
* {
  box-sizing: border-box;
  margin: 0;
  font-size: 12px !important;
  text-decoration: none !important;
}

.main-container {
  display: flex;
  flex-direction: column;
  margin-left: 260px;
  min-height: 100vh;
  background-color: #f9f9f9;
  transition: margin-left 0.3s;
}

.top-nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  height: 64px;
  background: #fff;
  border-bottom: 1px solid #eaeaea;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 24px;
  z-index: 100;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
}

.nav-left {
  display: flex;
  align-items: center;
}

.menu-btn {
  background: none;
  border: none;
  font-size: 24px;
  margin-right: 16px;
  cursor: pointer;
  display: none;
}

.menu-icon {
  display: inline-block;
}

.brand {
  font-size: 20px;
  font-weight: bold;
  color: #333;
}

.nav-right {
  display: flex;
  align-items: center;
  gap: 16px;
}

.search-input {
  padding: 6px 12px;
  border: 1px solid #e0e0e0;
  border-radius: 20px;
  font-size: 14px;
  outline: none;
  transition: border 0.2s;
}

.search-input:focus {
  border: 1.5px solid #007bff;
}

.avatar {
  width: 36px;
  height: 36px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid #e0e0e0;
}

/* Responsive Styles */
@media (max-width: 991px) {
  .main-container {
    margin-left: 0;
  }

  .menu-btn {
    display: block;
  }
}

@media (max-width: 600px) {
  .top-nav {
    padding: 0 10px;
    height: 56px;
  }

  .brand {
    font-size: 16px;
  }

  .search-input {
    display: none;
  }

  .avatar {
    width: 30px;
    height: 30px;
  }
}

.main-content {
  padding-top: 24px;
  margin-top: 64px;
  overflow-y: auto;
  flex-grow: 1;
}

.table-responsive {
  width: 100%;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
}

.table-responsive::-webkit-scrollbar {
  height: 8px;
}

.table-responsive::-webkit-scrollbar-track {
  background: #f1f1f1;
}

.table-responsive::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 4px;
}

.table-responsive::-webkit-scrollbar-thumb:hover {
  background: #555;
}
</style>
