import axios from 'axios'

export const getEmployees = () => {
  return axios.get('/hrm/employees/')
}

export const getEmployee = (id) => {
  return axios.get(`/hrm/employees/${id}/`)
}

export const createEmployee = (employee) => {
  return axios.post('/hrm/employees/', employee)
}

export const updateEmployee = (id, employee) => {
  return axios.put(`/hrm/employees/${id}/`, employee)
}

export const deleteEmployee = (id) => {
  return axios.delete(`/hrm/employees/${id}/`)
}
