import { defineStore } from 'pinia'

export const useThemeStore = defineStore('theme', {
  state: () => ({
    isDarkMode: localStorage.getItem('theme') === 'dark' || false,
  }),
  actions: {
    toggleTheme() {
      this.isDarkMode = !this.isDarkMode
      localStorage.setItem('theme', this.isDarkMode ? 'dark' : 'light')
      document.documentElement.setAttribute('data-theme', this.isDarkMode ? 'dark' : 'light')
    },
    initTheme() {
      // Initialize theme on app load
      const savedTheme = localStorage.getItem('theme') || 'light'
      this.isDarkMode = savedTheme === 'dark'
      document.documentElement.setAttribute('data-theme', savedTheme)
    },
  },
})
