import axios from "axios";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:5000";

const createHeaders = (token) => ({
  headers: {
    Authorization: `Bearer ${token}`,
  },
});

export const register = async (data) => {
  return await axios.post(`${API_URL}/auth/register`, data);
};

export const login = async (data) => {
  return await axios.post(`${API_URL}/auth/login`, data);
};

export const getUsers = async (token) => {
  return await axios.get(`${API_URL}/admin/users`, createHeaders(token));
};

export const updateUserRole = async (userId, role, token) => {
  return await axios.put(
    `${API_URL}/admin/users/${userId}`,
    { role },
    createHeaders(token)
  );
};
