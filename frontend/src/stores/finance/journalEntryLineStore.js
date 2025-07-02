import { defineStore } from 'pinia'
import * as journalEntryLineApi from '@/api/finance'

export const useJournalEntryLineStore = defineStore('journalEntryLine', {
  state: () => ({
    journalEntryLines: [],
    loading: false,
  }),
  actions: {
    async fetchJournalEntryLines() {
      this.loading = true
      try {
        const res = await journalEntryLineApi.getJournalEntryLines()
        console.log('✅ API response:', res)
        this.journalEntryLines = res.data
      } catch (error) {
        console.error('❌ API fetch failed:', error)
      } finally {
        this.loading = false
      }
    },
    async addJournalEntryLine(journalEntryLine) {
      await journalEntryLineApi.createJournalEntryLines(journalEntryLine)
      await this.fetchJournalEntryLines()
    },
    async updateJournalEntryLine(id, journalEntryLine) {
      await journalEntryLineApi.updateJournalEntryLine(id, journalEntryLine)
      await this.fetchJournalEntryLines()
    },
    async removeJournalEntryLine(id) {
      await journalEntryLineApi.deleteJournalEntryLine(id)
      await this.fetchJournalEntryLines()
    },
  },
})
