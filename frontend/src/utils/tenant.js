// src/utils/tenant.js
export function getTenantFromSubdomain() {
  const host = window.location.hostname // e.g., tenant1.localhost
  const parts = host.split('.')
  if (parts.length >= 2 && parts[1] === 'localhost') {
    return parts[0] // tenant1
  }
  return null
}
