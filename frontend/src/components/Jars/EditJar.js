// src/components/Jars/EditJar.js

import React, { useState, useEffect } from 'react';
import { getJarById, updateJar } from '../../services/api';
import { useParams, useHistory } from 'react-router-dom';

const EditJar = () => {
  const { id } = useParams();
  const history = useHistory();

  const [name, setName] = useState('');
  const [category, setCategory] = useState('');
  const [balance, setBalance] = useState(0);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchJar = async () => {
      try {
        const result = await getJarById(id);
        const { name, category, balance } = result.data;
        setName(name);
        setCategory(category);
        setBalance(balance);
      } catch (err) {
        setError('Failed to fetch jar');
      }
    };
    fetchJar();
  }, [id]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const updatedJar = {
        name,
        category,
        balance,
      };
      await updateJar(id, updatedJar);
      history.push('/jars');  // Redirect back to jar list
    } catch (err) {
      setError('Failed to update jar');
    }
  };

  return (
    <div>
      <h2>Edit Jar</h2>
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
        <button type="submit">Update Jar</button>
      </form>
    </div>
  );
};

export default EditJar;
