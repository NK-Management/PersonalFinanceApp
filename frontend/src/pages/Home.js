import React from 'react';
import { Link } from 'react-router-dom';
import Login from '../components/Auth/Login';
import Register from '../components/Auth/Register';

const Home = () => {
  return (
    <div className="container">
      <h1>Welcome to Your Budget Tracker</h1>

      {/* Login and Register Section */}
      <div>
        <h2>Login</h2>
        <Login />
      </div>

      <div>
        <h2>Register</h2>
        <Register />
      </div>

      {/* Links to Other Pages */}
      <div>
        <h2>Quick Links</h2>
        <Link to="/budget-dashboard">Go to Dashboard</Link>
      </div>
      <div>
        <Link to="/add-jar">Add a Jar</Link>
      </div>
      <div>
        <Link to="/add-expense">Add an Expense</Link>
      </div>
      <div>
        <Link to="/add-goal">Add a Goal</Link>
      </div>
      <div>
        <Link to="/add-income">Add Income</Link>
      </div>
    </div>
  );
};

export default Home;
