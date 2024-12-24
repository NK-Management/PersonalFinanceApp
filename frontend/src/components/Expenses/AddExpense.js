// src/components/Expenses/AddExpense.js

import React, { useState } from 'react';
import { addExpense } from '../../services/api';

const AddExpense = () => {
  const [category, setCategory] = useState('');
  const [amount, setAmount] = useState('');
  const [date, setDate] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const expenseData = { category, amount, date };
      await addExpense(expenseData);
      setCategory('');
      setAmount('');
      setDate('');
    } catch (err) {
      setError('Failed to add expense');
    }
  };

  return (
    <div>
      <h2>Add New Expense</h2>
      {error && <div className="error">{error}</div>}
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Category"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
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
        <button type="submit">Add Expense</button>
      </form>
    </div>
  );
};

export default AddExpense;
