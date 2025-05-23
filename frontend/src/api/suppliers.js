import axios from './axiosInstance'

export function fetchSuppliers() {
  return axios.get('suppliers/')
}
