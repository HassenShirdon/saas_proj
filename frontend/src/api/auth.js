// src/api/auth.js
import axios from './axios'

// 🔐 POST: Login with username/password → returns tokens
export async function loginUser(credentials) {
  const response = await axios.post('token/', credentials)
  return response.data // { access: "...", refresh: "..." }
}
