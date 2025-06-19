// src/stores/inventory/productCategoriesStore.js
import { defineStore } from 'pinia'
import * as productCategoryApi from '@/api/inventory'

export const useProductCategoryStore = defineStore('productCategories', {
  state: () => ({
    productCategories: [],
    loading: false,
  }),
  actions: {
    async fetchProductCategories() {
      this.loading = true
      try {
        const res = await productCategoryApi.getProductCategories()
        this.productCategories = res.data
        this.loading = false
      } catch (error) {
        this.loading = false
        throw error
      }
    },
    async addProductCategory(productCategory) {
      try {
        await productCategoryApi.createProductCategory(productCategory)
        await this.fetchProductCategories()
      } catch (error) {
        throw error
      }
    },
    async updateProductCategory(id, productCategory) {
      try {
        await productCategoryApi.updateProductCategory(id, productCategory)
        await this.fetchProductCategories()
      } catch (error) {
        throw error
      }
    },
    async removeProductCategory(id) {
      try {
        await productCategoryApi.deleteProductCategory(id)
        await this.fetchProductCategories()
      } catch (error) {
        throw error
      }
    },
  },
})
