<template>
  <nav class="navbar navbar-expand fixed-top bg-white border-bottom shadow-sm" style="z-index: 1000;">
    <div class="container-fluid px-3">
      <div class="d-flex align-items-center">
        <button class="btn btn-outline-light d-md-none me-2" @click="$emit('toggle-sidebar')"
          aria-label="Toggle sidebar">
          <i class="bi bi-list fs-5"></i>
        </button>
        <span class="navbar-brand fw-bold text-primary">Dashboard</span>
      </div>
      <div class="d-flex align-items-center gap-3">
        <input type="text" class="form-control rounded-pill" placeholder="Search..." style="max-width: 200px;" />
        <div class="dropdown">
          <button class="btn btn-outline-light dropdown-toggle d-flex align-items-center gap-2" type="button"
            data-bs-toggle="dropdown" aria-expanded="false">
            <img src="https://via.placeholder.com/36" alt="User Avatar" class="rounded-circle" width="36" height="36" />
            <span class="d-none d-md-inline text-primary">{{ userName }}</span>
          </button>
          <ul class="dropdown-menu dropdown-menu-end">
            <li><span class="dropdown-item-text text-primary">{{ userName }}</span></li>
            <li><span class="dropdown-item-text">admin@company.com</span></li>
            <li>
              <hr class="dropdown-divider" />
            </li>
            <li><a class="dropdown-item text-primary" href="#">Profile</a></li>
            <li><a class="dropdown-item text-primary" href="#">Settings</a></li>
            <li>
              <button class="dropdown-item text-primary" @click="logout" :disabled="isLoggingOut">
                {{ isLoggingOut ? 'Logging out...' : 'Logout' }}
              </button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<script>
export default {
  name: 'TopNav',
  emits: ['toggle-sidebar'],
  data() {
    return {
      userName: 'Admin User', // Replace with actual user data
      isLoggingOut: false,
    };
  },
  methods: {
    logout() {
      this.isLoggingOut = true;
      setTimeout(() => {
        // Simulate logout
        this.isLoggingOut = false;
        // Add actual logout logic here
      }, 2000);
    },
  },
};
</script>

<style scoped>
.navbar {
  height: 64px;
}

.navbar-brand,
.dropdown-item {
  color: #3B82F6 !important;
}

.form-control,
.btn-outline-light {
  border-color: #F0F0F0;
}

.form-control:focus {
  border-color: #3B82F6;
  box-shadow: 0 0 0 0.2rem rgba(59, 130, 246, 0.25);
}

.dropdown-menu {
  border: 1px solid #F0F0F0;
}
</style>