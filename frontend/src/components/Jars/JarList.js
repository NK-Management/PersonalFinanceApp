// src/components/Jars/JarList.js

import React, { useEffect, useState } from 'react';
import { getJars, deleteJar } from '../../services/api';
import { Link } from 'react-router-dom';

const JarList = () => {
  const [jars, setJars] = useState([]);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchJars = async () => {
      try {
        const result = await getJars();
        setJars(result.data);
      } catch (err) {
        setError('Failed to fetch jars');
      }
    };
    fetchJars();
  }, []);

  const handleDelete = async (id) => {
    try {
      await deleteJar(id);
      setJars(jars.filter((jar) => jar.id !== id)); // Remove deleted jar from the list
    } catch (err) {
      setError('Failed to delete jar');
    }
  };

  return (
    <div>
      <h2>Jars</h2>
      {error && <div className="error">{error}</div>}
      <ul>
        {jars.map((jar) => (
          <li key={jar.id}>
            {jar.name} - {jar.category} - ${jar.balance}
            <button onClick={() => handleDelete(jar.id)}>Delete</button>
            <Link to={`/edit-jar/${jar.id}`}>Edit</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default JarList;
