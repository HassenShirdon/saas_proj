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
      const res = await employeeApi.getEmployees()
      this.employees = res.data
      this.loading = false
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
