// src/stores/authStore.js
import { defineStore } from 'pinia'
import axios from '@/api/axios'
import router from '@/router/index.js'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    accessToken: localStorage.getItem('access_token'),
    user: null,
  }),
  getters: {
    isAuthenticated: (state) => !!state.accessToken,
  },
  actions: {
    async login(credentials) {
      try {
        const res = await axios.post('token/', credentials)
        this.accessToken = res.data.access
        localStorage.setItem('access_token', res.data.access)
        router.push('/dashboard')
      } catch (error) {
        console.error('Login error:', error.response?.data || error.message)
        throw error // Re-throw the error so the component can catch it
      }
    },
    logout() {
      this.accessToken = null
      this.user = null
      localStorage.removeItem('access_token')
      router.push('/login')
    },
    async refreshToken() {
      try {
        const res = await axios.post('token/refresh/', {
          refresh: localStorage.getItem('refresh_token'),
        })
        this.accessToken = res.data.access
        localStorage.setItem('access_token', res.data.access)
        return res.data.access
      } catch (error) {
        this.logout()
        throw error
      }
    },
  },
})
