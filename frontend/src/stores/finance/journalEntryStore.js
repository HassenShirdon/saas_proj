import { defineStore } from 'pinia'
import * as journalEntryApi from '@/api/finance'

export const useJournalEntryStore = defineStore('journalEntry', {
  state: () => ({
    journalEntries: [],
    loading: false,
  }),
  actions: {
    async fetchJournalEntries() {
      this.loading = true
      try {
        const res = await journalEntryApi.getJournalEntries()
        console.log('✅ API response:', res)
        this.journalEntries = res.data
      } catch (error) {
        console.error('❌ API fetch failed:', error)
      } finally {
        this.loading = false
      }
    },
    async addJournalEntry(journalEntry) {
      await journalEntryApi.createJournalEntries(journalEntry)
      await this.fetchJournalEntries()
    },
    async updateJournalEntry(id, journalEntry) {
      await journalEntryApi.updateJournalEntry(id, journalEntry)
      await this.fetchJournalEntries()
    },
    async removeJournalEntry(id) {
      await journalEntryApi.deleteJournalEntry(id)
      await this.fetchJournalEntries()
    },
  },
})
