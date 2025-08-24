import { defineStore } from "pinia";
import { ref, computed } from "vue";
import apiClient from "../api/axios";
import router from "../router";

export const useAuthStore = defineStore("auth", () => {
  const user = ref(JSON.parse(localStorage.getItem("user") || "null"));
  const isLoading = ref(false);
  const error = ref(null);

  const isAuthenticated = computed(() => !!user.value);
  const getUser = computed(() => user.value);

  const login = async (credentials) => {
    isLoading.value = true;
    error.value = null;

    try {
      const response = await apiClient.post("/token/", credentials);
      const { access, refresh } = response.data;

      localStorage.setItem("access_token", access);
      localStorage.setItem("refresh_token", refresh);

      // Fetch user data
      const userResponse = await apiClient.get("/user/");
      user.value = userResponse.data; // userResponse.data should include role
      localStorage.setItem("user", JSON.stringify(user.value));

      // Return role for routing
      return user.value.role;
    } catch (err) {
      error.value = err.response?.data?.detail || "Login failed";
      throw err;
    } finally {
      isLoading.value = false;
    }
  };

  const logout = async () => {
    isLoading.value = true;

    try {
      // If your Django setup supports token blacklisting
      const refreshToken = localStorage.getItem("refresh_token");
      if (refreshToken) {
        await apiClient.post("/token/blacklist/", { refresh: refreshToken });
      }
    } catch (err) {
      console.warn("Logout blacklist failed:", err);
      // Continue with logout even if blacklist fails
    } finally {
      // Clear storage regardless of blacklist success
      localStorage.removeItem("access_token");
      localStorage.removeItem("refresh_token");
      localStorage.removeItem("user");
      user.value = null;
      isLoading.value = false;

      router.push("/login");
    }
  };

  const register = async (userData) => {
    isLoading.value = true;
    error.value = null;

    try {
      const response = await apiClient.post("/register/", userData);
      return response.data;
    } catch (err) {
      error.value = err.response?.data || "Registration failed";
      throw err;
    } finally {
      isLoading.value = false;
    }
  };

  const refreshToken = async () => {
    try {
      const refreshToken = localStorage.getItem("refresh_token");
      if (!refreshToken) {
        throw new Error("No refresh token available");
      }

      const response = await apiClient.post("/token/refresh/", {
        refresh: refreshToken,
      });

      const { access } = response.data;
      localStorage.setItem("access_token", access);
      return access;
    } catch (err) {
      logout();
      throw err;
    }
  };

  // Initialize auth state from localStorage
  const initializeAuth = () => {
    const storedUser = localStorage.getItem("user");
    if (storedUser) {
      user.value = JSON.parse(storedUser);
    }
  };

  return {
    user,
    isLoading,
    error,
    isAuthenticated,
    getUser,
    login,
    logout,
    register,
    refreshToken,
    initializeAuth,
  };
});
