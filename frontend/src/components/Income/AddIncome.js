// src/components/Incomes/AddIncome.js

import React, { useState } from 'react';
import { addIncome } from '../../services/api';

const AddIncome = () => {
  const [source, setSource] = useState('');
  const [amount, setAmount] = useState('');
  const [date, setDate] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const incomeData = {
        source,
        amount,
        date,
      };
      await addIncome(incomeData);
      // Reset fields after successful submission
      setSource('');
      setAmount('');
      setDate('');
    } catch (err) {
      setError('Failed to add income');
    }
  };

  return (
    <div>
      <h2>Add New Income</h2>
      {error && <div className="error">{error}</div>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Source"
          value={source}
          onChange={(e) => setSource(e.target.value)}
        />
        <input
          type="number"
          placeholder="Amount"
          value={amount}
          onChange={(e) => setAmount(e.target.value)}
        />
        <input
          type="date"
          value={date}
          onChange={(e) => setDate(e.target.value)}
        />
        <button type="submit">Add Income</button>
      </form>
    </div>
  );
};

export default AddIncome;
