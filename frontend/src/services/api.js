import axios from "axios";

// Load the base API URL from environment variables or fallback to localhost
const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000/api";

// Create a reusable Axios instance with the base URL
const api = axios.create({
  baseURL: API_URL, // Set API URL for all requests
  headers: { 'Content-Type': 'application/json' }
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
  throw error.response?.data || { message: "An unknown error occurred" };
};

// Authentication Services
export const register = async (data) => {
  try {
    const response = await api.post("/auth/register", data);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const login = async (data) => {
  try {
    const response = await api.post("/auth/login", data);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const getCurrentUser = async (token) => {
  try {
    const response = await api.get("/auth/me", createHeaders(token));
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Jars API
export const addJar = async (jarData) => {
  try {
    const response = await api.post("/jars", jarData);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const getJars = async () => {
  try {
    const response = await api.get("/jars");
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const getJarById = async (id) => {
  try {
    const response = await api.get(`/jars/${id}`);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const updateJar = async (id, jarData) => {
  try {
    const response = await api.put(`/jars/${id}`, jarData);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const deleteJar = async (id) => {
  try {
    const response = await api.delete(`/jars/${id}`);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Expenses API
export const addExpense = async (expenseData) => {
  try {
    const response = await api.post("/expenses", expenseData);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const getExpenses = async () => {
  try {
    const response = await api.get("/expenses");
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const updateExpense = async (id, expenseData) => {
  try {
    const response = await api.put(`/expenses/${id}`, expenseData);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const deleteExpense = async (id) => {
  try {
    const response = await api.delete(`/expenses/${id}`);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Goals API
export const addGoal = async (goalData) => {
  try {
    const response = await api.post("/goals", goalData);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const getGoals = async () => {
  try {
    const response = await api.get("/goals");
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const updateGoal = async (id, goalData) => {
  try {
    const response = await api.put(`/goals/${id}`, goalData);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const deleteGoal = async (id) => {
  try {
    const response = await api.delete(`/goals/${id}`);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Incomes API
export const addIncome = async (incomeData) => {
  try {
    const response = await api.post("/incomes", incomeData);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const getIncomes = async () => {
  try {
    const response = await api.get("/incomes");
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const updateIncome = async (id, incomeData) => {
  try {
    const response = await api.put(`/incomes/${id}`, incomeData);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

export const deleteIncome = async (id) => {
  try {
    const response = await api.delete(`/incomes/${id}`);
    return response.data;
  } catch (error) {
    handleError(error);
  }
};

// Budget Overview API
export const getBudgetOverview = async () => {
  try {
    const response = await api.get("/budget-overview");
    return response.data;
  } catch (error) {
    handleError(error);
  }
};
