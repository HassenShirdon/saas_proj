// src/api/products.js
import axios from '@/api/axios'

// Products
export const getProducts = () => {
  return axios.get('/inventory/products/')
}
export const getProduct = (id) => {
  return axios.get(`/inventory/products/${id}/`)
}
export const createProduct = (product) => {
  return axios.post('/inventory/products/', product)
}
export const updateProduct = (id, product) => {
  return axios.put(`/inventory/products/${id}/`, product)
}
export const deleteProduct = (id) => {
  axios.delete(`/inventory/products/${id}/`)
}
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

export const getItems = () => {
  return axios.get('/inventory/inventory-items/')
}
export const getItem = (id) => {
  return axios.get(`/inventory/inventory-items/${id}/`)
}
export const createItem = (item) => {
  return axios.post('/inventory/inventory-items/', item)
}
export const updateItem = (id, item) => {
  return axios.put(`/inventory/inventory-items/${id}/`, item)
}
export const deleteItem = (id) => {
  return axios.delete(`/inventory/inventory-items/${id}/`)
}

export const getPurchaseOrders = () => {
  return axios.get('/inventory/purchase-orders/')
}

const getPurchaseOrder = (id) => {
  return axios.get(`/inventory/purchase-orders/${id}/`)
}

export const createPurchaseOrder = (purchaseOrder) => {
  return axios.post('/inventory/purchase-orders/', purchaseOrder)
}
export const updatePurchaseOrder = (id, purchaseOrder) => {
  return axios.put(`/inventory/purchase-orders/${id}/`, purchaseOrder)
}
export const deletePurchaseOrder = (id) => {
  return axios.delete(`/inventory/purchase-orders/${id}/`)
}

export const getStockMovements = () => {
  return axios.get(`/inventory/stocks`)
}

export const getStockMovement = (id) => {
  return axios.get(`/inventory/stocks/${id}/`)
}

export const createStockMovement = (stock) => {
  return axios.post(`/inventory/stocks/`, stock)
}

export const updateStockMovement = (id, stock) => {
  return axios.put(`/inventory/stocks/${id}/`, stock)
}

export const deleteStockMovement = (id) => {
  return axios.delete(`/inventory/stocks/${id}/`)
}
