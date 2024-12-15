import React, { useState, useEffect } from "react";
import { getUsers, updateUserRole } from "../../services/api";

const RoleManagement = () => {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState("");
  const [message, setMessage] = useState("");

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await getUsers(token);
        setUsers(response.data);
      } catch (err) {
        setError("Failed to fetch users.");
      }
    };
    fetchUsers();
  }, []);

  const handleRoleChange = async (userId, newRole) => {
    try {
      const token = localStorage.getItem("token");
      await updateUserRole(userId, newRole, token);
      setUsers((prevUsers) =>
        prevUsers.map((user) =>
          user.id === userId ? { ...user, role: newRole } : user
        )
      );
      setMessage("Role updated successfully.");
    } catch (err) {
      setError("Failed to update role.");
    }
  };

  return (
    <div>
      <h2>Role Management</h2>
      {error && <p style={{ color: "red" }}>{error}</p>}
      {message && <p style={{ color: "green" }}>{message}</p>}
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.email} - {user.role}
            <select
              value={user.role}
              onChange={(e) => handleRoleChange(user.id, e.target.value)}
            >
              <option value="user">User</option>
              <option value="admin">Admin</option>
            </select>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default RoleManagement;
