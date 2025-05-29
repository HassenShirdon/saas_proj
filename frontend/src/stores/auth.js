// src/stores/auth.js
import { defineStore } from 'pinia'
import api from '@/api/axios'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: null,
    refreshToken: null,
    user: null,
    currentTenant: null,
    tenants: [],
  }),

  actions: {
    async login(credentials) {
      try {
        const response = await api.post('/api/auth/login/', credentials)
        this.accessToken = response.data.access
        this.refreshToken = response.data.refresh
        this.user = response.data.user

        // Load tenants for this user
        await this.fetchTenants()
        return true
      } catch (error) {
        throw error
      }
    },

    async fetchTenants() {
      try {
        const response = await api.get('/api/tenants/')
        this.tenants = response.data
        if (this.tenants.length > 0) {
          this.currentTenant = this.tenants[0] // Default to first tenant
        }
      } catch (error) {
        throw error
      }
    },

    async refreshToken() {
      try {
        const response = await api.post('/api/auth/refresh/', {
          refresh: this.refreshToken,
        })
        this.accessToken = response.data.access
        return response.data
      } catch (error) {
        this.logout()
        throw error
      }
    },

    logout() {
      this.accessToken = null
      this.refreshToken = null
      this.user = null
      this.currentTenant = null
      this.tenants = []
    },

    setCurrentTenant(tenant) {
      this.currentTenant = tenant
    },
  },

  persist: true, // Optional: for persisting state
})
