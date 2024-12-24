// src/components/Incomes/IncomeList.js

import React, { useEffect, useState } from 'react';
import { getIncomes, deleteIncome } from '../../services/api';
import { Link } from 'react-router-dom';

const IncomeList = () => {
  const [incomes, setIncomes] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchIncomes = async () => {
      try {
        const result = await getIncomes();
        setIncomes(result.data);
      } catch (err) {
        setError('Failed to fetch incomes');
      }
    };
    fetchIncomes();
  }, []);

  const handleDelete = async (id) => {
    try {
      await deleteIncome(id);
      setIncomes(incomes.filter((income) => income.id !== id)); // Remove deleted income from the list
    } catch (err) {
      setError('Failed to delete income');
    }
  };

  return (
    <div>
      <h2>Incomes</h2>
      {error && <div className="error">{error}</div>}
      <ul>
        {incomes.map((income) => (
          <li key={income.id}>
            {income.source} - ${income.amount} on {income.date}
            <button onClick={() => handleDelete(income.id)}>Delete</button>
            <Link to={`/edit-income/${income.id}`}>Edit</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default IncomeList;
