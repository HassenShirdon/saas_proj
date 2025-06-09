// src/stores/inventory/productCategoriesStore.js
import { defineStore } from 'pinia'
import * as productCategoryApi from '@/api/inventory'

export const useProductCategoryStore = defineStore('productCategory', {
  state: () => ({
    productCategories: [], // Fixed: changed from 'products' to 'productCategories'
    loading: false,
  }),
  actions: {
    async fetchProductCategories() {
      // Fixed: method name should match what component calls
      this.loading = true
      try {
        const res = await productCategoryApi.getProductCategories()
        this.productCategories = res.data // Fixed: assign to correct state property
        this.loading = false
      } catch (error) {
        console.error('Error adding product category:', error)
        throw error
      }
    },
    async addproductCategory(productCategory) {
      try {
        await productCategoryApi.createproductCategory(productCategory)
        await this.fetchproductCategories() // Fixed: call correct method
      } catch (error) {
        console.error('Error adding product category:', error)
        throw error
      }
    },
    async updateproductCategory(id, productCategory) {
      try {
        await productCategoryApi.updateproductCategory(id, productCategory)
        await this.fetchproductCategories() // Fixed: call correct method
      } catch (error) {
        console.error('Error updating product category:', error)
        throw error
      }
    },
    async removeproductCategory(id) {
      try {
        await productCategoryApi.deleteproductCategory(id)
        await this.fetchproductCategories() // Fixed: call correct method
      } catch (error) {
        console.error('Error removing product category:', error)
        throw error
      }
    },
  },
})
