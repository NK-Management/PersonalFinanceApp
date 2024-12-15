import React from "react";
import UserList from "../components/Dashboard/UserList";
import RoleManagement from "../components/Dashboard/RoleManagement";

const AdminDashboard = () => {
  return (
    <div>
      <h1>Admin Dashboard</h1>
      <UserList />
      <RoleManagement />
    </div>
  );
};

export default AdminDashboard;
