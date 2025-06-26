import { defineStore } from 'pinia'
import * as accountListApi from '@api/finance'

export const useAccountListStore = defineStore('accountList', {
  state: () => ({
    accounts: [],
    loading: false,
  }),
  actions: {
    async fetchAccountlists() {
      this.loading = true
      try {
        const res = await accountListApi.getAccounts()
        console.log('✅ API response:', res)
        this.accounts = res.data
      } catch (error) {
        console.error('❌ API fetch failed:', error)
      } finally {
        this.loading = false
      }
    },
    async addAccountlist(accountList) {
      await accountListApi.createAccount(accountList)
      await this.fetchAccountlists()
    },
    async updateAccountlist(id, accountList) {
      await accountListApi.updateAccount(id, accountList)
      await this.fetchAccountlists()
    },
    async removeAccount(id) {
      await accountListApi.deleteAccountlist(id)
      await this.fetchAccountlists()
    },
  },
})
