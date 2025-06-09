import { defineStore } from 'pinia'
import * as supplierApi from '@/api/inventory'

export const useSupplierStore = defineStore('supplier', {
  state: () => ({
    suppliers: [],
    loading: false,
  }),
  actions: {
    async fetchSuppliers() {
      this.loading = true
      const res = await supplierApi.getSuppliers()
      this.suppliers = res.data
      this.loading = false
    },
    async addSupplier(supplier) {
      await supplierApi.createSupplier(supplier)
      await this.fetchSuppliers()
    },
    async updateSupplier(id, supplier) {
      await supplierApi.updateSupplier(id, supplier)
      await this.fetchSuppliers()
    },
    async removeSupplier(id) {
      await supplierApi.deleteSupplier(id)
      await this.fetchSuppliers()
    },
  },
}) 