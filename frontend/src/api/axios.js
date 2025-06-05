import axios from 'axios'

const getApiBaseUrl = () => {
  const subdomain = window.location.hostname.split('.')[0]
  // if (process.env.NODE_ENV === 'production') {
  //   return `https://${subdomain}.localhost.com/api/`
  // }
  return `http://${subdomain}.localhost:8000/api/`
}

const instance = axios.create({
  baseURL: getApiBaseUrl(),
  headers: {
    'Content-Type': 'application/json',
    Accept: 'application/json',
  },
  xsrfCookieName: 'csrftoken',
  xsrfHeaderName: 'X-CSRFToken',
  withCredentials: true,
  timeout: 10000,
})

instance.interceptors.request.use((config) => {
  const token = localStorage.getItem('access_token')
  if (token) {
    config.headers.Authorization = `Bearer ${token}`
  }
  return config
})

instance.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('access_token')
      window.location.href = '/login'
    }

    return Promise.reject({
      message: error.response?.data?.message || 'An error occurred',
      status: error.response?.status,
      data: error.response?.data,
    })
  },
)

export default instance
