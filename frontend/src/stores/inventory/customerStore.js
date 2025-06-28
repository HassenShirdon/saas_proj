// src/stores/productStore.js
import { defineStore } from 'pinia'
import * as customerApi from '@/api/inventory'

export const useCustomerStore = defineStore('customer', {
  state: () => ({
    customers: [],
    loading: false,
  }),
  actions: {
    async fetchCustomers() {
      this.loading = true

      try {
        const res = await customerApi.getCustomers()
        console.log('✅ API response:', res)
        // Assuming the API returns an object with a 'data' property containing the customers
        this.customers = res.data
      } catch (error) {
        console.error('❌ API fetch failed:', error)
        // Optionally, you can handle the error state here, e.g., show a notification
      } finally {
        this.loading = false
      }
    },
    async addCustomer(customer) {
      await customerApi.createCustomer(customer)
      await this.fetchCustomers()
    },
    async updateCustomer(id, customer) {
      await customerApi.updateCustomer(id, customer)
      await this.fetchCustomers()
    },
    async removeCustomer(id) {
      await customerApi.deleteCustomer(id)
      await this.fetchCustomers()
    },
  },
})
