// src/stores/productStore.js
import { defineStore } from 'pinia'
import * as productApi from '@/api/inventory'

export const useProductStore = defineStore('product', {
  state: () => ({
    products: [],
    loading: false,
  }),
  actions: {
    async fetchProducts() {
      this.loading = true
      const res = await productApi.getProducts()
      this.products = res.data
      this.loading = false
    },
    async addProduct(product) {
      await productApi.createProduct(product)
      await this.fetchProducts()
    },
    async updateProduct(id, product) {
      await productApi.updateProduct(id, product)
      await this.fetchProducts()
    },
    async removeProduct(id) {
      await productApi.deleteProduct(id)
      await this.fetchProducts()
    },
  },
})
