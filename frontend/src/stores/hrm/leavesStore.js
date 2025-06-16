import { defineStore } from 'pinia'
import * as leaveApi from '@/api/hrm'
export const useLeavesStore = defineStore('leaves', {
  state: () => ({
    leaves: [],
    loading: false,
  }),
  actions: {
    async fetchLeaves() {
      this.loading = true
      const res = await leaveApi.getLeaves()
      this.leaves = res.data
      this.loading = false
    },
    async addLeave(leave) {
      await leaveApi.createLeave(leave)
      await this.fetchLeaves()
    },
    async updateLeave(id, leave) {
      await leaveApi.updateLeave(id, leave)
      await this.fetchLeaves()
    },
    async removeLeave(id) {
      await leaveApi.deleteLeave(id)
      await this.fetchLeaves()
    },
  },
})
