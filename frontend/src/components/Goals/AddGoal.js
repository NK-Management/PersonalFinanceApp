// src/components/Goals/AddGoal.js

import React, { useState } from 'react';
import { addGoal } from '../../services/api';

const AddGoal = () => {
  const [name, setName] = useState('');
  const [amount, setAmount] = useState('');
  const [deadline, setDeadline] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const goalData = { name, amount, deadline };
      await addGoal(goalData);
      setName('');
      setAmount('');
      setDeadline('');
    } catch (err) {
      setError('Failed to add goal');
    }
  };

  return (
    <div>
      <h2>Add New Goal</h2>
      {error && <div className="error">{error}</div>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Goal Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <input
          type="date"
          value={deadline}
          onChange={(e) => setDeadline(e.target.value)}
        />
        <button type="submit">Add Goal</button>
      </form>
    </div>
  );
};

export default AddGoal;
