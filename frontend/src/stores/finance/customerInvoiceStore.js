import { defineStore } from 'pinia'
import * as customerInvoiceApi from '@/api/finance'

export const useCustomerInvoiceStore = defineStore('customerInvoice', {
  state: () => ({
    customerInvoices: [],
    loading: false,
  }),
  actions: {
    async fetchCustomerInvoices() {
      this.loading = true
      try {
        const res = await customerInvoiceApi.getCustomerInvoices()
        console.log('✅ API response:', res)
        this.customerInvoices = res.data
      } catch (error) {
        console.error('❌ API fetch failed:', error)
      } finally {
        this.loading = false
      }
    },
    async addCustomerInvoice(customerInvoice) {
      await customerInvoiceApi.createCustomerInvoice(customerInvoice)
      await this.fetchCustomerInvoices()
    },
    async updateCustomerInvoice(id, customerInvoice) {
      await customerInvoiceApi.updateCustomerInvoice(id, customerInvoice)
      await this.fetchCustomerInvoices()
    },
    async removeCustomerInvoice(id) {
      await customerInvoiceApi.deleteCustomerInvoice(id)
      await this.fetchCustomerInvoices()
    },
  },
})
