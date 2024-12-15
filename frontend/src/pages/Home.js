import React from "react";
import Login from "../components/Auth/Login";
import Register from "../components/Auth/Register";

const Home = () => {
  return (
    <div>
      <h1>Welcome</h1>
      <Login />
      <Register />
    </div>
  );
};

export default Home;
