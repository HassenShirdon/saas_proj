// src/api/products.js
import axios from '@/api/axios'

// Products
export const getProducts = () => {
  return axios.get(`/inventory/products/`)
}
export const getProduct = (id) => {
  return axios.get(`/inventory/product/${id}/`)
}
export const createProduct = (product) => {
  return axios.post(`/inventory/products/`, product)
}
export const updateProduct = (id, product) => {
  return axios.put(`/inventory/product/${id}/`, product)
}
export const deleteProduct = (id) => {
  axios.delete(`/inventory/product/${id}/`)
}
// Customers
export const getCustomers = () => {
  return axios.get(`/inventory/Customers/`) // This is correct
}

export const getCustomer = (id) => {
  return axios.get(`/inventory/Customer/${id}/`) // Added missing slash at end
}

export const createCustomer = (customer) => {
  return axios.post(`/inventory/Customers/`, customer) // This is correct
}

export const updateCustomer = (id, customer) => {
  return axios.put(`/inventory/Customer/${id}/`, customer) // Added missing slash at end
}

export const deleteCustomer = (id) => {
  return axios.delete(`/inventory/Customer/${id}/`) // Added missing slash at end
}

// Suppliers
export const getSuppliers = () => {
  return axios.get(`/inventory/suppliers/`)
}
export const getSupplier = (id) => {
  return axios.get(`/inventory/supplier/${id}/`)
}
export const createSupplier = (supplier) => {
  return axios.post(`/inventory/suppliers/`, supplier)
}
export const updateSupplier = (id, supplier) => {
  return axios.put(`/inventory/supplier/${id}/`, supplier)
}
export const deleteSupplier = (id) => {
  return axios.delete(`/inventory/supplier/${id}/`)
}

// Product Categories
export const getProductCategories = () => {
  return axios.get(`/inventory/product-categories/`)
}
export const getProductCategory = (id) => {
  return axios.get(`/inventory/product-category/${id}/`)
}
export const createProductCategory = (productCategory) => {
  return axios.post(`/inventory/product-categories/`, productCategory)
}
export const updateProductCategory = (id, productCategory) => {
  return axios.put(`/inventory/product-category/${id}/`, productCategory)
}
export const deleteProductCategory = (id) => {
  return axios.delete(`/inventory/product-category/${id}/`)
}

// inventory Items
export const getItems = () => {
  return axios.get(`/inventory/inventory-items/`)
}
export const getItem = (id) => {
  return axios.get(`/inventory/inventory-item/${id}/`)
}
export const createItem = (item) => {
  return axios.post(`/inventory/inventory-items/`, item)
}
export const updateItem = (id, item) => {
  return axios.put(`/inventory/inventory-item/${id}/`, item)
}
export const deleteItem = (id) => {
  return axios.delete(`/inventory/inventory-item/${id}/`)
}
//purchase orders
export const getPurchaseOrders = () => {
  return axios.get(`/inventory/purchase-orders/`)
}

const getPurchaseOrder = (id) => {
  return axios.get(`/inventory/purchase-order/${id}/`)
}

export const createPurchaseOrder = (purchaseOrder) => {
  return axios.post('/inventory/purchase-orders/', purchaseOrder)
}
export const updatePurchaseOrder = (id, purchaseOrder) => {
  return axios.put(`/inventory/purchase-order/${id}/`, purchaseOrder)
}
export const deletePurchaseOrder = (id) => {
  return axios.delete(`/inventory/purchase-order/${id}/`)
}

//StockMovement
export const getStockMovements = () => {
  return axios.get(`/inventory/stocks`)
}

export const getStockMovement = (id) => {
  return axios.get(`/inventory/stock/${id}/`)
}

export const createStockMovement = (stock) => {
  return axios.post(`/inventory/stocks/`, stock)
}

export const updateStockMovement = (id, stock) => {
  return axios.put(`/inventory/stock/${id}/`, stock)
}

export const deleteStockMovement = (id) => {
  return axios.delete(`/inventory/stock/${id}/`)
}
