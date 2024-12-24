import React, { useEffect, useState } from 'react';
import { getGoals, deleteGoal } from '../../services/api';
import { Link } from 'react-router-dom';

const GoalList = () => {
    const [goals, setGoals] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchGoals = async () => {
            try {
                const result = await getGoals();
                setGoals(result);  // Assuming getGoals returns an array of goal objects
            } catch (err) {
                setError('Failed to fetch goals');
            }
        };
        fetchGoals();
    }, []);

    const handleDelete = async (id) => {
        try {
            await deleteGoal(id);  // API call to delete the goal
            setGoals(goals.filter((goal) => goal.id !== id));  // Update the state by removing the deleted goal
        } catch (err) {
            setError('Failed to delete goal');
        }
    };

    return (
        <div>
            <h2>Goals</h2>
            {error && <div className="error">{error}</div>}
            {goals.length === 0 ? (
                <p>No goals found.</p>
            ) : (
                <ul>
                    {goals.map((goal) => (
                        <li key={goal.id}>
                            <span>{goal.title} - ${goal.targetAmount}</span>
                            <button onClick={() => handleDelete(goal.id)}>Delete</button>
                            <Link to={`/edit-goal/${goal.id}`}>Edit</Link>
                        </li>
                    ))}
                </ul>
            )}
        </div>
    );
};

export default GoalList;
