// src/components/Goals/EditGoal.js

import React, { useState, useEffect } from 'react';
import { getGoalById, updateGoal } from '../../services/api';
import { useParams, useHistory } from 'react-router-dom';

const EditGoal = () => {
  const { id } = useParams();
  const history = useHistory();

  const [name, setName] = useState('');
  const [amount, setAmount] = useState('');
  const [deadline, setDeadline] = useState('');
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchGoal = async () => {
      try {
        const result = await getGoalById(id);
        const { name, amount, deadline } = result.data;
        setName(name);
        setAmount(amount);
        setDeadline(deadline);
      } catch (err) {
        setError('Failed to fetch goal');
      }
    };
    fetchGoal();
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const updatedGoal = { name, amount, deadline };
      await updateGoal(id, updatedGoal);
      history.push('/goals');  // Redirect back to goal list
    } catch (err) {
      setError('Failed to update goal');
    }
  };

  return (
    <div>
      <h2>Edit Goal</h2>
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
        <button type="submit">Update Goal</button>
      </form>
    </div>
  );
};

export default EditGoal;
