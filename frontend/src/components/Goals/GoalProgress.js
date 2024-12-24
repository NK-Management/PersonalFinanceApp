import React, { useEffect, useState } from 'react';
import { getGoals } from '../../services/api';

function GoalProgress() {
    const [goals, setGoals] = useState([]);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchGoals = async () => {
            try {
                const data = await getGoals();
                setGoals(data);  // Assuming getGoals returns an array of goals
            } catch (err) {
                setError('Failed to fetch goals');
            }
        };
        fetchGoals();
    }, []);

    return (
        <div className="container">
            <h2>Your Goals Progress</h2>
            {error && <div className="error">{error}</div>}
            {goals.length === 0 ? (
                <p>No goals found.</p>
            ) : (
                goals.map((goal) => (
                    <div key={goal.id} className="goal-card">
                        <h3>{goal.title}</h3>
                        <p>Target: ${goal.targetAmount}</p>
                        <p>Progress: ${goal.progress}</p>
                        <p>
                            Completed: {((goal.progress / goal.targetAmount) * 100).toFixed(2)}%
                        </p>
                    </div>
                ))
            )}
        </div>
    );
}

export default GoalProgress;
