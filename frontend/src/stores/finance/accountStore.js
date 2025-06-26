//src/stores/finance/accountStore.js
import { defineStore } from 'pinia'
import * as accountApi from '@/api/finance'

export const useAccountStore = defineStore('account', {
  state: () => ({
    accounts: [],
    loading: false,
  }),
  actions: {
    async fetchAccounts() {
      this.loading = true
      try {
        const res = await accountApi.getAccounts()
        console.log('✅ API response:', res)
        this.accounts = res.data
      } catch (error) {
        console.error('❌ API fetch failed:', error)
      } finally {
        this.loading = false
      }
    },
    async addAccount(account) {
      await accountApi.createAccount(account)
      await this.fetchAccounts()
    },
    async updateAccount(id, account) {
      await accountApi.updateAccount(id, account)
      await this.fetchAccounts()
    },
    async removeAccount(id) {
      await accountApi.deleteAccount(id)
      await this.fetchAccounts()
    },
  },
})
