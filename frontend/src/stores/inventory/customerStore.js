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
      const res = await customerApi.getCustomers()
      this.customers = res.data
      this.loading = false
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
