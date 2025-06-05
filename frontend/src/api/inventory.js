// src/api/products.js
import axios from '@/api/axios'

export const getProducts = () => axios.get('/inventory/products/')
export const getProduct = (id) => axios.get(`/inventory/products/${id}/`)
export const createProduct = (product) => axios.post('/inventory/products/', product)
export const updateProduct = (id, product) => axios.put(`/inventory/products/${id}/`, product)
export const deleteProduct = (id) => axios.delete(`/inventory/products/${id}/`)

export const getCustomers = () => {
  return axios.get('/inventory/Customers')
}

export const createCustomer = (customer) => {
  return axios.post('/inventory/Customers', customer)
}

export const updateCustomer = (id, customer) => {
  return axios.put(`/inventory/Customers/${id}`, customer)
}

export const deleteCustomer = (id) => {
  return axios.delete(`/inventory/Customers/${id}`)
}
