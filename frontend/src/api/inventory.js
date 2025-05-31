// src/api/products.js
import axios from './axios'

export const getProducts = () => axios.get('/inventory/products/')
export const getProduct = (id) => axios.get(`/inventory/products/${id}/`)
export const createProduct = (product) => axios.post('/inventory/products/', product)
export const updateProduct = (id, product) => axios.put(`/inventory/products/${id}/`, product)
export const deleteProduct = (id) => axios.delete(`/inventory/products/${id}/`)
