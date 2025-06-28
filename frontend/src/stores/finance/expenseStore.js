//src/stores/finance/expenseStore.js
import { defineStore } from 'pinia'
import * as expenseApi from '@/api/finance'

export const useExpenseStore = defineStore('expense', {
  state: () => ({
    expenses: [],
    loading: false,
  }),
  actions: {
    async fetchExpenses() {
      this.loading = true
      try {
        const res = await expenseApi.getExpenses()
        console.log('✅ API response:', res)
        this.expenses = res.data
      } catch (error) {
        console.error('❌ API fetch failed:', error)
      } finally {
        this.loading = false
      }
    },
    async addExpense(expense) {
      await expenseApi.createExpense(expense)
      await this.fetchExpenses()
    },
    async updateExpense(id, expense) {
      await expenseApi.updateExpense(id, expense)
      await this.fetchExpenses()
    },
    async removeExpense(id) {
      await expenseApi.deleteExpense(id)
      await this.fetchExpenses()
    },
  },
})
