import axios from 'axios'

export const fetchCustomers = () => {
  return axios.get('http://jeeh.localhost:8000/inventory/Customers/')
}
