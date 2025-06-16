import { defineStore } from 'pinia'
import * as employeeApi from '@/api/hrm'

export const useEmployeeStore = defineStore('employee', {
  state: () => ({
    employees: [],
    loading: false,
  }),
  actions: {
    async fetchEmployees() {
      this.loading = true
      try {
        const res = await employeeApi.getEmployees()
        console.log('✅ API response:', res)
        this.employees = res.data
      } catch (error) {
        console.error('❌ API fetch failed:', error)
        alert('Failed to fetch employees. See console for details.')
      } finally {
        this.loading = false
      }
    },
    async addEmployee(employee) {
      await employeeApi.createEmployee(employee)
      await this.fetchEmployees()
    },
    async updateEmployee(id, employee) {
      await employeeApi.updateEmployee(id, employee)
      await this.fetchEmployees()
    },
    async removeEmployee(id) {
      await employeeApi.deleteEmployee(id)
      await this.fetchEmployees()
    },
  },
})
