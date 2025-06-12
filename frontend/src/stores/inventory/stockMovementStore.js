import { defineStore } from 'pinia'
import * as StockMovementApi from '@/api/inventory'

export const useStockmovementStore = defineStore('stockmovement', {
  state: () => ({
    StockMovement: [],
    loading: false,
  }),
  actions: {
    async fetchStockMovement() {
      this.loading = true
      const res = await StockMovementApi.getStockMovements()
      this.StockMovement = res.data
      this.loading = false
    },
    async addStockMovement(stockmovement) {
      await StockMovementApi.createStockMovement(stockmovement)
      await this.fetchStockMovement()
    },
    async updateStockMovement(id, stockmovement) {
      await StockMovementApi.updateStockMovement(id, stockmovement)
      await this.fetchStockMovement()
    },
    async removeStockMovement(id) {
      await StockMovementApi.deleteStockMovement(id)
      await this.fetchStockMovement()
    },
  },
})
