import { defineStore } from 'pinia'
import * as attendanceApi from '@/api/hrm'

export const useAttendanceStore = defineStore('attendance', {
  state: () => ({
    attendances: [],
    loading: false,
  }),
  actions: {
    async fetchAttendances() {
      this.loading = true
      const res = await attendanceApi.getAttendances()
      this.attendances = res.data
      this.loading = false
    },
    async addAttendance(attendance) {
      await attendanceApi.createAttendance(attendance)
      await this.fetchAttendances()
    },
    async updateAttendance(id, attendance) {
      await attendanceApi.updateAttendance(id, attendance)
      await this.fetchAttendances()
    },
    async removeAttendance(id) {
      await attendanceApi.deleteAttendance(id)
      await this.fetchAttendances()
    },
  },
})
