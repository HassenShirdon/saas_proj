import { defineStore } from 'pinia'
import * as salaryApi from '@/api/hrm'

export const useSalaryStore = defineStore('salary', {
  state: () => ({
    salaries: [],
    loading: false,
  }),
  actions: {
    async fetchSalaries() {
      this.loading = true
      const res = await salaryApi.getSalaries()
      this.salaries = res.data
      this.loading = false
    },
    async addSalary(salary) {
      await salaryApi.createSalary(salary)
      await this.fetchSalaries()
    },
    async updateSalary(id, salary) {
      await salaryApi.updateSalary(id, salary)
      await this.fetchSalaries()
    },
    async removeSalary(id) {
      await salaryApi.deleteSalary(id)
      await this.fetchSalaries()
    },
  },
})
