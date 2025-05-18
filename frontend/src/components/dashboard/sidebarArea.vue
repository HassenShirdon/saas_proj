<template>
  <aside class="sidebar">
    <div class="sidebar-header">
      <h2>Dashboard</h2>
    </div>

    <nav class="menu">
      <ul>
        <li>
          <RouterLink to="/dashboard" class="link">Home</RouterLink>
        </li>

        <li @click="toggleInventory" class="link has-dropdown">
          Inventory
          <span class="arrow" :class="{ open: showInventory }">▾</span>
        </li>
        <ul v-if="showInventory" class="submenu">
          <li><RouterLink to="/products" class="sublink">Products</RouterLink></li>
          <li><RouterLink to="/categories" class="sublink">Categories</RouterLink></li>
          <li><RouterLink to="/brands" class="sublink">Brands</RouterLink></li>
          <li><RouterLink to="/suppliers" class="sublink">Suppliers</RouterLink></li>
          <li><RouterLink to="/units" class="sublink">Units</RouterLink></li>
          <li><RouterLink to="/stock" class="sublink">Stock</RouterLink></li>
          <li><RouterLink to="/purchases" class="sublink">Purchases</RouterLink></li>
          <li><RouterLink to="/sales" class="sublink">Sales</RouterLink></li>
          <li><RouterLink to="/returns" class="sublink">Returns</RouterLink></li>
        </ul>

        <li><RouterLink to="/reports" class="link">Reports</RouterLink></li>
        <li><RouterLink to="/settings" class="link">Settings</RouterLink></li>
      </ul>
    </nav>
  </aside>
</template>

<script>
export default {
  data() {
    return {
      showInventory: false,
    }
  },
  methods: {
    toggleInventory() {
      this.showInventory = !this.showInventory
    },
  },
}
</script>

<style scoped>
.sidebar {
  width: 260px;
  background-color: #1976d2; /* light primary */
  color: white;
  height: 100vh;
  padding: 20px 15px;
  position: fixed;
  top: 0;
  left: 0;
  overflow-y: auto;
}

.sidebar-header {
  font-size: 22px;
  font-weight: bold;
  margin-bottom: 30px;
  text-align: center;
  color: #fff;
}

.menu ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.link,
.sublink {
  display: block;
  padding: 10px 15px;
  border-radius: 6px;
  color: white;
  text-decoration: none;
  font-size: 15px;
  transition: background 0.2s ease;
}

.link:hover,
.sublink:hover {
  background-color: rgba(255, 255, 255, 0.15);
}

.has-dropdown {
  cursor: pointer;
  position: relative;
}

.arrow {
  float: right;
  transition: transform 0.3s ease;
}

.arrow.open {
  transform: rotate(180deg);
}

.submenu {
  padding-left: 15px;
  margin-top: 5px;
}
</style>
