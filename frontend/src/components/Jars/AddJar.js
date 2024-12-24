// src/components/Jars/AddJar.js

import React, { useState } from 'react';
import { addJar } from '../../services/api';

const AddJar = () => {
  const [name, setName] = useState('');
  const [category, setCategory] = useState('');
  const [balance, setBalance] = useState(0);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const jarData = {
        name,
        category,
        balance,
      };
      await addJar(jarData);
      // Reset fields after successful submission
      setName('');
      setCategory('');
      setBalance(0);
    } catch (err) {
      setError('Failed to add jar');
    }
  };

  return (
    <div>
      <h2>Add New Jar</h2>
      {error && <div className="error">{error}</div>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Jar Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Category"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        />
        <input
          type="number"
          placeholder="Balance"
          value={balance}
          onChange={(e) => setBalance(e.target.value)}
        />
        <button type="submit">Add Jar</button>
      </form>
    </div>
  );
};

export default AddJar;
