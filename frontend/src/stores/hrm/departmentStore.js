import { defineStore } from 'pinia'
import * as departmentApi from '@/api/hrm'

export const useDepartmentStore = defineStore('departmentStore', {
  state: () => ({
    departments: [],
    department: null,
    loading: false,
    error: null,
  }),

  actions: {
    async fetchDepartments() {
      this.loading = true
      try {
        const response = await departmentApi.getDepartments()
        this.departments = response.data
      } catch (error) {
        this.error = error
      } finally {
        this.loading = false
      }
    },

    async fetchDepartment(id) {
      this.loading = true
      try {
        const response = await departmentApi.getDepartment(id)
        this.department = response.data
      } catch (error) {
        this.error = error
      } finally {
        this.loading = false
      }
    },

    async createDepartment(department) {
      this.loading = true
      try {
        const response = await departmentApi.createDepartment(department)
        this.departments.push(response.data)
      } catch (error) {
        this.error = error
      } finally {
        this.loading = false
      }
    },

    async updateDepartment(id, department) {
      this.loading = true
      try {
        const response = await departmentApi.updateDepartment(id, department)
        const index = this.departments.findIndex((dep) => dep.id === id)
        if (index !== -1) {
          this.departments[index] = response.data
        }
      } catch (error) {
        this.error = error
      } finally {
        this.loading = false
      }
    },

    async deleteDepartment(id) {
      this.loading = true
      try {
        await departmentApi.deleteDepartment(id)
        this.departments = this.departments.filter((dep) => dep.id !== id)
      } catch (error) {
        this.error = error
      } finally {
        this.loading = false
      }
    },
  },
})
