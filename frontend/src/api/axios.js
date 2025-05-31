// src/api/axios.js
import axios from 'axios'
const subdomain = window.location.hostname.split('.')[0]

const instance = axios.create({
  baseURL: `http://${subdomain}.localhost:8000/api/`, //'http://localhost:8000/api/',
})

instance.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

export default instance
