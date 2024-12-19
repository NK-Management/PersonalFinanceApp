import React, { useState } from "react";
import { register } from "../../services/api";

const Register = () => {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);

  const handleRegister = async (e) => {
    e.preventDefault();

    // Basic client-side validation
    if (!username || !email || !password) {
      setMessage("All fields are required.");
      return;
    }

    setLoading(true);
    setMessage(""); // Clear any previous message

    try {
      await register({ username, email, password });
      setMessage("Registration successful! Please log in.");
    } catch (error) {
      // Extract detailed error message
      const errorMessage =
        error.response?.data?.message ||
        error.response?.data?.errors?.[0]?.message ||
        "Registration failed.";
      setMessage(errorMessage);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h2>Register</h2>
      <form onSubmit={handleRegister}>
        <input
          type="text"
          placeholder="Username"
          aria-label="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type="email"
          placeholder="Email"
          aria-label="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          aria-label="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit" disabled={loading} aria-label="Register">
          {loading ? "Registering..." : "Register"}
        </button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
};

export default Register;
