// src/api/products.js
import axios from '@/api/axios'

// Products
export const getProducts = () => axios.get('/inventory/products/')
export const getProduct = (id) => axios.get(`/inventory/products/${id}/`)
export const createProduct = (product) => axios.post('/inventory/products/', product)
export const updateProduct = (id, product) => axios.put(`/inventory/products/${id}/`, product)
export const deleteProduct = (id) => axios.delete(`/inventory/products/${id}/`)

// Customers
export const getCustomers = () => {
  return axios.get('/inventory/Customers/')
}
export const getCustomer = (id) => {
  return axios.get(`/inventory/Customer/${id}/`)
}
export const createCustomer = (customer) => {
  return axios.post('/inventory/Customers/', customer)
}
export const updateCustomer = (id, customer) => {
  return axios.put(`/inventory/Customers/${id}`, customer)
}
export const deleteCustomer = (id) => {
  return axios.delete(`/inventory/Customers/${id}`)
}

// Suppliers
export const getSuppliers = () => {
  return axios.get('/inventory/suppliers/')
}
export const getSupplier = (id) => {
  return axios.get(`/inventory/Supplier/${id}/`)
}
export const createSupplier = (supplier) => {
  return axios.post('/inventory/suppliers/', supplier)
}
export const updateSupplier = (id, supplier) => {
  return axios.put(`/inventory/suppliers/${id}`, supplier)
}
export const deleteSupplier = (id) => {
  return axios.delete(`/inventory/suppliers/${id}`)
}

// Product Categories - Fixed naming and parameter issues
export const getProductCategories = () => {
  return axios.get('/inventory/product-categories/')
}
export const getProductCategory = (id) => {
  return axios.get(`/inventory/product-categories/${id}/`)
}
export const createProductCategory = (productCategory) => {
  return axios.post('/inventory/product-categories/', productCategory)
}
export const updateProductCategory = (id, productCategory) => {
  return axios.put(`/inventory/product-categories/${id}/`, productCategory)
}
export const deleteProductCategory = (id) => {
  return axios.delete(`/inventory/product-categories/${id}/`)
}