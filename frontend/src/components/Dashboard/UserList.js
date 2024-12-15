import React, { useState, useEffect } from "react";
import { getUsers } from "../../services/api";

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchUsers = async () => {
      try {
        const token = localStorage.getItem("token");
        const response = await getUsers(token);
        setUsers(response.data);
      } catch (error) {
        setError("Failed to fetch users.");
      }
    };
    fetchUsers();
  }, []);

  return (
    <div>
      <h2>User List</h2>
      {error && <p>{error}</p>}
      <ul>
        {users.map((user) => (
          <li key={user.id}>
            {user.email} - {user.role}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default UserList;
