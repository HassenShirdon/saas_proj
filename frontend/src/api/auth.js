import api from "./api";

class AuthService {
  // Login user
  async login(credentials) {
    try {
      const response = await api.post("/token/", credentials);

      if (response.data.access && response.data.refresh) {
        localStorage.setItem("access_token", response.data.access);
        localStorage.setItem("refresh_token", response.data.refresh);

        // Set default authorization header for this axios instance
        api.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${response.data.access}`;
      }

      return response.data;
    } catch (error) {
      throw error.response?.data || error;
    }
  }

  // Logout user
  logout() {
    localStorage.removeItem("access_token");
    localStorage.removeItem("refresh_token");
    localStorage.removeItem("user"); // If you’re storing user info separately

    delete api.defaults.headers.common["Authorization"];

    // Optional: call backend logout if you need to invalidate refresh tokens server-side
    // return api.post("/logout/");
  }

  // Refresh token manually (not usually needed because api.js interceptor handles it)
  async refreshToken() {
    try {
      const refreshToken = localStorage.getItem("refresh_token");
      if (!refreshToken) {
        throw new Error("No refresh token available");
      }

      const response = await api.post("/token/refresh/", {
        refresh: refreshToken,
      });

      if (response.data.access) {
        localStorage.setItem("access_token", response.data.access);
        api.defaults.headers.common[
          "Authorization"
        ] = `Bearer ${response.data.access}`;
      }

      return response.data;
    } catch (error) {
      this.logout();
      throw error.response?.data || error;
    }
  }

  // Get current authenticated user (if your backend provides it)
  async getCurrentUser() {
    try {
      const response = await api.get("/user/");
      localStorage.setItem("user", JSON.stringify(response.data));
      return response.data;
    } catch (error) {
      throw error.response?.data || error;
    }
  }

  // Check if user is authenticated
  isAuthenticated() {
    return !!localStorage.getItem("access_token");
  }

  // Get stored tokens
  getTokens() {
    return {
      access: localStorage.getItem("access_token"),
      refresh: localStorage.getItem("refresh_token"),
    };
  }
}

export default new AuthService();
