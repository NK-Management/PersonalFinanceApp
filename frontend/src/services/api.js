import axios from "axios";

// Load the base API URL from environment variables or fallback to localhost
const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

// Create a reusable Axios instance with the base URL
const api = axios.create({
  baseURL: API_URL,
});

// Helper function to add Authorization headers
const createHeaders = (token) => ({
  headers: {
    Authorization: `Bearer ${token}`,
  },
});

// Error handler to log and transform errors
const handleError = (error) => {
  console.error("API Error:", error.response || error.message);
  // Re-throw the error to allow calling functions to handle it
  throw error.response?.data || { message: "An unknown error occurred" };
};

// API Methods

// Register a new user
export const register = async (data) => {
  try {
    const response = await api.post("/auth/register", data);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Login a user and get the JWT token
export const login = async (data) => {
  try {
    const response = await api.post("/auth/login", data);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Get details of the currently authenticated user
export const getCurrentUser = async (token) => {
  try {
    const response = await api.get("/auth/me", createHeaders(token));
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Update the role of a user (Admin only)
export const updateUserRole = async (userId, role, token) => {
  try {
    const response = await api.put(
      `/auth/role/${userId}`,
      { role },
      createHeaders(token)
    );
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Get all users (Admin only)
export const getUsers = async (token) => {
  try {
    const response = await api.get("/admin/users", createHeaders(token));
    return response.data;
  } catch (error) {
    handleError(error);
  }
};
