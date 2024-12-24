// src/components/Expenses/EditExpense.js

import React, { useState, useEffect } from 'react';
import { getExpenseById, updateExpense } from '../../services/api';
import { useParams, useHistory } from 'react-router-dom';

const EditExpense = () => {
  const { id } = useParams();
  const history = useHistory();

  const [category, setCategory] = useState('');
  const [amount, setAmount] = useState('');
  const [date, setDate] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchExpense = async () => {
      try {
        const result = await getExpenseById(id);
        const { category, amount, date } = result.data;
        setCategory(category);
        setAmount(amount);
        setDate(date);
      } catch (err) {
        setError('Failed to fetch expense');
      }
    };
    fetchExpense();
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const updatedExpense = { category, amount, date };
      await updateExpense(id, updatedExpense);
      history.push('/expenses');  // Redirect back to expense list
    } catch (err) {
      setError('Failed to update expense');
    }
  };

  return (
    <div>
      <h2>Edit Expense</h2>
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
        <button type="submit">Update Expense</button>
      </form>
    </div>
  );
};

export default EditExpense;
