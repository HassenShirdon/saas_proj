import { defineStore } from 'pinia'
import * as supplierInvoiceApi from '@/api/finance'

export const useSupplierInvoiceStore = defineStore('supplierInvoice', {
  state: () => ({
    supplierInvoices: [],
    loading: false,
  }),
  actions: {
    async fetchSupplierInvoices() {
      this.loading = true
      try {
        const res = await supplierInvoiceApi.getSupplierInvoices()
        console.log('✅ API response:', res)
        this.supplierInvoices = res.data
      } catch (error) {
        console.error('❌ API fetch failed:', error)
      } finally {
        this.loading = false
      }
    },
    async addSupplierInvoice(supplierInvoice) {
      await supplierInvoiceApi.createSupplierInvoice(supplierInvoice)
      await this.fetchSupplierInvoices()
    },
    async updateSupplierInvoice(id, supplierInvoice) {
      await supplierInvoiceApi.updateSupplierInvoice(id, supplierInvoice)
      await this.fetchSupplierInvoices()
    },
    async removeSupplierInvoice(id) {
      await supplierInvoiceApi.deleteSupplierInvoice(id)
      await this.fetchSupplierInvoices()
    },
  },
})
