import { defineStore } from 'pinia'
import * as accountTypesApi from '@/api/finance'

export const useAccountTypeStore = defineStore('accountType', {
  state: () => ({
    accounts: [],
    loading: false,
  }),
  actions: {
    async fetchAccountTypes() {
      this.loading = true
      try {
        const res = await accountTypesApi.getAccountTypes()
        console.log('✅ API response:', res)
        this.accounts = res.data
      } catch (error) {
        console.error('❌ API fetch failed:', error)
      } finally {
        this.loading = false
      }
    },
    async addAccountType(accountType) {
      await accountTypesApi.createAccount(accountType)
      await this.fetchAccountTypes()
    },
    async updateAccountType(id, accountType) {
      await accountTypesApi.updateAccountType(id, accountType)
      await this.fetchAccountTypes()
    },
    async removeAccountType(id) {
      await accountTypesApi.deleteAccountType(id)
      await this.fetchAccountTypes()
    },
  },
})
