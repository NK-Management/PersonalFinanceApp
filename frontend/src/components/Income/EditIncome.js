// src/components/Incomes/EditIncome.js

import React, { useState, useEffect } from 'react';
import { getIncomeById, updateIncome } from '../../services/api';
import { useParams, useHistory } from 'react-router-dom';

const EditIncome = () => {
  const { id } = useParams();
  const history = useHistory();

  const [source, setSource] = useState('');
  const [amount, setAmount] = useState('');
  const [date, setDate] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchIncome = async () => {
      try {
        const result = await getIncomeById(id);
        const { source, amount, date } = result.data;
        setSource(source);
        setAmount(amount);
        setDate(date);
      } catch (err) {
        setError('Failed to fetch income');
      }
    };
    fetchIncome();
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const updatedIncome = {
        source,
        amount,
        date,
      };
      await updateIncome(id, updatedIncome);
      history.push('/incomes');  // Redirect back to income list
    } catch (err) {
      setError('Failed to update income');
    }
  };

  return (
    <div>
      <h2>Edit Income</h2>
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
        <button type="submit">Update Income</button>
      </form>
    </div>
  );
};

export default EditIncome;
