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
/* Reset and Base Styles */
* {
  box-sizing: border-box;
  margin: 0;
  font-size: 12px !important;
  text-decoration: none !important;
}

/* Main Container */
.main-container {
  display: flex;
  flex-direction: column;
  margin-left: 260px;
  min-height: 100vh;
  background-color: #f9f9f9;
  transition: margin-left 0.3s;
}

/* Top Navigation - UNCHANGED */
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

/* Main Content - Enhanced for Table Responsiveness */
.main-content {
  padding-top: 24px;
  margin-top: 64px;
  flex-grow: 1;
  height: calc(100vh - 64px - 24px);
  overflow: hidden;
  padding-left: 16px;
  padding-right: 16px;
  padding-bottom: 16px;
}

/* Table Container - The Key Enhancement */
.table-responsive {
  width: 100%;
  height: 100%;
  overflow: auto;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  background: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: relative;
}

/* Enhanced Scrollbar Styling */
.table-responsive::-webkit-scrollbar {
  width: 12px;
  height: 12px;
}

.table-responsive::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 6px;
}

.table-responsive::-webkit-scrollbar-thumb {
  background: #c1c1c1;
  border-radius: 6px;
  border: 1px solid #f1f1f1;
}

.table-responsive::-webkit-scrollbar-thumb:hover {
  background: #a8a8a8;
}

.table-responsive::-webkit-scrollbar-corner {
  background: #f1f1f1;
}

/* Table Styling for Long Tables */
.table-responsive table {
  width: 100%;
  min-width: max-content;
  /* Allows table to expand beyond container */
  border-collapse: separate;
  border-spacing: 0;
  margin: 0;
}

.table-responsive th,
.table-responsive td {
  padding: 8px 12px;
  text-align: left;
  border-bottom: 1px solid #dee2e6;
  white-space: nowrap;
  /* Prevents text wrapping */
  min-width: 100px;
  /* Minimum column width */
  max-width: 250px;
  /* Maximum column width */
}

.table-responsive th {
  background: #f8f9fa;
  position: sticky;
  top: 0;
  z-index: 10;
  font-weight: 600;
  border-bottom: 2px solid #dee2e6;
}

.table-responsive tbody tr:hover {
  background-color: #f5f5f5;
}

/* Text Truncation for Long Content */
.table-responsive .text-truncate {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  max-width: 200px;
}

/* Specific Column Widths for Better Layout */
.table-responsive .col-narrow {
  width: 80px;
  min-width: 80px;
  max-width: 80px;
}

.table-responsive .col-medium {
  width: 120px;
  min-width: 120px;
  max-width: 150px;
}

.table-responsive .col-wide {
  width: 200px;
  min-width: 150px;
  max-width: 300px;
}

.table-responsive .col-description {
  min-width: 200px;
  max-width: 400px;
}

.table-responsive .col-notes {
  min-width: 150px;
  max-width: 300px;
}

/* Form Controls in Tables */
.table-responsive .form-control {
  width: 100%;
  min-width: 90px;
  font-size: 12px !important;
  padding: 4px 8px;
  border: 1px solid #ced4da;
  border-radius: 4px;
}

.table-responsive .form-control:focus {
  border-color: #80bdff;
  box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25);
}

.table-responsive .form-control.is-invalid {
  border-color: #dc3545;
}

.table-responsive .invalid-feedback {
  display: block;
  font-size: 11px !important;
  color: #dc3545;
  margin-top: 2px;
}

/* Table Warning Rows */
.table-responsive .table-warning {
  background-color: rgba(255, 243, 205, 0.5) !important;
}

.table-responsive .table-warning:hover {
  background-color: rgba(255, 243, 205, 0.8) !important;
}

/* Long Row Management */
.table-responsive tr {
  min-height: 40px;
}

.table-responsive td {
  vertical-align: middle;
  word-break: break-word;
  overflow-wrap: break-word;
}

/* For very long content in cells */
.table-responsive .cell-content {
  display: block;
  max-height: 60px;
  overflow-y: auto;
  line-height: 1.4;
}

.table-responsive .cell-content::-webkit-scrollbar {
  width: 4px;
}

.table-responsive .cell-content::-webkit-scrollbar-thumb {
  background: #ccc;
  border-radius: 2px;
}

/* Responsive Breakpoints */
@media (max-width: 991px) {
  .main-container {
    margin-left: 0;
  }

  .menu-btn {
    display: block;
  }

  .main-content {
    padding-left: 8px;
    padding-right: 8px;
  }
}

@media (max-width: 768px) {
  .main-content {
    padding-left: 4px;
    padding-right: 4px;
    padding-top: 16px;
  }

  .table-responsive th,
  .table-responsive td {
    padding: 6px 8px;
    min-width: 80px;
  }

  .table-responsive .text-truncate {
    max-width: 120px;
  }

  .table-responsive .form-control {
    padding: 3px 6px;
    min-width: 70px;
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

  .main-content {
    margin-top: 56px;
    height: calc(100vh - 56px - 16px);
    padding-left: 2px;
    padding-right: 2px;
    padding-top: 8px;
  }

  .table-responsive th,
  .table-responsive td {
    padding: 4px 6px;
    min-width: 60px;
    font-size: 11px !important;
  }

  .table-responsive .text-truncate {
    max-width: 80px;
  }

  .table-responsive .form-control {
    padding: 2px 4px;
    min-width: 50px;
    font-size: 11px !important;
  }
}

@media (max-width: 480px) {

  .table-responsive th,
  .table-responsive td {
    padding: 3px 4px;
    min-width: 50px;
    font-size: 10px !important;
  }

  .table-responsive .text-truncate {
    max-width: 60px;
  }

  .table-responsive .form-control {
    padding: 1px 3px;
    min-width: 40px;
    font-size: 10px !important;
  }
}

/* Horizontal Scroll Indicator */
.table-responsive::after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  width: 20px;
  height: 100%;
  background: linear-gradient(to left, rgba(255, 255, 255, 0.8), transparent);
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s;
}

.table-responsive:hover::after {
  opacity: 1;
}

/* Print Styles */
@media print {
  .main-container {
    margin-left: 0;
  }

  .top-nav {
    display: none;
  }

  .main-content {
    margin-top: 0;
    height: auto;
    padding: 0;
  }

  .table-responsive {
    border: none;
    box-shadow: none;
    overflow: visible;
    height: auto;
  }

  .table-responsive table {
    min-width: 100%;
  }

  .table-responsive th,
  .table-responsive td {
    font-size: 9px !important;
    padding: 2px 4px;
  }
}
</style>
