import axios from '@/api/axios'

export const getEmployees = () => {
  return axios.get(`/hrm/employees`)
}

export const getEmployee = (id) => {
  return axios.get(`/hrm/employees/${id}/`)
}

export const createEmployee = (employee) => {
  return axios.post(`/hrm/employees/`, employee)
}

export const updateEmployee = (id, employee) => {
  return axios.put(`/hrm/employees/${id}/`, employee)
}

export const deleteEmployee = (id) => {
  return axios.delete(`/hrm/employees/${id}/`)
}

export const getDepartments = () => {
  return axios.get(`/hrm/departments/`)
}

export const getDepartment = (id) => {
  return axios.get(`/hrm/departments/${id}/`)
}

export const createDepartment = (department) => {
  return axios.post(`/hrm/departments/`, department)
}

export const updateDepartment = (id, department) => {
  return axios.put(`/hrm/departments/${id}/`, department)
}

export const deleteDepartment = (id) => {
  return axios.delete(`/hrm/departments/${id}/`)
}

export const getAttendances = () => {
  return axios.get(`/hrm/attendance/`)
}

export const getAttendance = (id) => {
  return axios.get(`/hrm/attendance/${id}/`)
}
export const createAttendance = (attendance) => {
  return axios.post('/hrm/attendance/', attendance)
}

export const updateAttendance = (id, attendance) => {
  return axios.put(`/hrm/attendance/${id}/`, attendance)
}

export const deleteAttendance = (id) => {
  return axios.delete(`/hrm/attendance/${id}/`)
}

export const getLeaves = () => {
  return axios.get(`/hrm/leave-types/`)
}
export const getLeave = (id) => {
  return axios.get(`/hrm/leave-types/${id}/`)
}

export const createLeave = (leave) => {
  return axios.post(`/hrm/leave-types/`, leave)
}

export const updateLeave = (id, leave) => {
  return axios.put(`/hrm/leave-types/${id}/`, leave)
}
export const deleteLeave = (id) => {
  return axios.delete(`/hrm/leave-types/${id}/`)
}

export const getSalaries = () => {
  return axios.get(`hrm/salary-history/`)
}

export const getSalary = (id) => {
  return axios.get(`hrm/salary-history/${id}/`)
}
export const createSalary = (salary) => {
  return axios.post('hrm/salary-history/', salary)
}
export const updateSalary = (id, salary) => {
  return axios.put(`hrm/salary-history/{id}/`, salary)
}
export const deleteSalary = (id) => {
  return axios.delete(`hrm/salary-history/${id}/`)
}

export const getPerformanceReviews = () => {
  return axios.get(`/hrm/performance-reviews/`)
}

export const getPerformanceReview = (id) => {
  return axios.get(`/hrm/performance-reviews/${id}/`)
}

export const createPerformanceReview = (review) => {
  return axios.post(`/hrm/performance-reviews/`, review)
}
export const updatePerformanceReview = (id, review) => {
  return axios.put(`/hrm/performance-reviews/${id}/`, review)
}
export const deletePerformanceReview = (id) => {
  return axios.delete(`/hrm/performance-reviews/${id}/`)
}
