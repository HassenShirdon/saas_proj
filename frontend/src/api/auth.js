// src/api/auth.js
import axios from './axios'

// 🔐 POST: Login with username/password → returns tokens
export async function loginUser(credentials) {
  const response = await axios.post('token/', credentials)
  // Store tokens using the same keys as in authStore.js
  localStorage.setItem('access_token', response.data.access)
  if (response.data.refresh) {
    localStorage.setItem('refresh_token', response.data.refresh)
  }
  return response.data // { access: "...", refresh: "..." }
}

/**
 * 🔓 Logout user by removing tokens from storage
 */
export function logoutUser() {
  localStorage.removeItem('access_token')
  localStorage.removeItem('refresh_token')
}
