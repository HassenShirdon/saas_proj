import { defineStore } from 'pinia'
import * as purchaseOrderApi from '@/api/inventory'

export const usePurchaseOrderStore = defineStore('purchaseOrder', {
  state: () => ({
    purchaseOrders: [],
    loading: false,
  }),
  actions: {
    async fetchPurchaseOrders() {
      this.loading = true
      const res = await purchaseOrderApi.getPurchaseOrders()
      this.purchaseOrders = res.data
      this.loading = false
    },
    async addPurchaseOrder(purchaseOrder) {
      await purchaseOrderApi.createPurchaseOrder(purchaseOrder)
      await this.fetchPurchaseOrders()
    },
    async updatePurchaseOrder(id, purchaseOrder) {
      await purchaseOrderApi.updatePurchaseOrder(id, purchaseOrder)
      await this.fetchPurchaseOrders()
    },
    async removePurchaseOrder(id) {
      await purchaseOrderApi.deletePurchaseOrder(id)
      await this.fetchPurchaseOrders()
    },
  },
})
