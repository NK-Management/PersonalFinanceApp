// src/components/Expenses/ExpenseList.js

import React, { useEffect, useState } from 'react';
import { getExpenses, deleteExpense } from '../../services/api';
import { Link } from 'react-router-dom';

const ExpenseList = () => {
  const [expenses, setExpenses] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchExpenses = async () => {
      try {
        const result = await getExpenses();
        setExpenses(result.data);
      } catch (err) {
        setError('Failed to fetch expenses');
      }
    };
    fetchExpenses();
  }, []);

  const handleDelete = async (id) => {
    try {
      await deleteExpense(id);
      setExpenses(expenses.filter((expense) => expense.id !== id)); // Remove deleted expense from the list
    } catch (err) {
      setError('Failed to delete expense');
    }
  };

  return (
    <div>
      <h2>Expenses</h2>
      {error && <div className="error">{error}</div>}
      <ul>
        {expenses.map((expense) => (
          <li key={expense.id}>
            {expense.category} - ${expense.amount} on {expense.date}
            <button onClick={() => handleDelete(expense.id)}>Delete</button>
            <Link to={`/edit-expense/${expense.id}`}>Edit</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ExpenseList;
