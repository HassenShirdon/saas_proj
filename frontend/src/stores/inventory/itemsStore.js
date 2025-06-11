import { defineStore } from 'pinia'
import * as ItemsApi from '@/api/inventory'

export const useItemsStore = defineStore('items', {
  state: () => ({
    items: [],
    loading: false,
  }),
  actions: {
    async fetchItems() {
      this.loading = true
      try {
        const res = await ItemsApi.getItems()
        this.items = res.data
        this.loading = false
      } catch (error) {
        this.loading = false
        throw error
      }
    },
    async addItem(item) {
      try {
        await ItemsApi.createItem(item)
        await this.fetchItems()
      } catch (error) {
        throw error
      }
    },
    async updateItem(id, item) {
      try {
        await ItemsApi.updateItem(id, item)
        await this.fetchItems()
      } catch (error) {
        throw error
      }
    },
    async removeItem(id) {
      try {
        await ItemsApi.deleteItem(id)
        await this.fetchItems()
      } catch (error) {
        throw error
      }
    },
  },
})
