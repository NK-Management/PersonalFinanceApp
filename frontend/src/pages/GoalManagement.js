import React, { useState, useEffect } from "react";
import { getGoals, deleteGoal } from "../../services/api";
import { Link } from "react-router-dom";
import GoalList from "../components/Goals/GoalList";  // Import the GoalList component
import GoalProgress from "../components/Goals/GoalProgress";  // Import the GoalProgress component

function GoalManagement() {
  const [goals, setGoals] = useState([]);
  const [error, setError] = useState("");

  // Fetch goals when the component mounts
  useEffect(() => {
    const fetchGoals = async () => {
      try {
        const result = await getGoals();
        setGoals(result);
      } catch (err) {
        setError("Failed to fetch goals");
      }
    };
    fetchGoals();
  }, []);

  // Handle the deletion of a goal
  const handleDelete = async (id) => {
    try {
      await deleteGoal(id);
      setGoals(goals.filter((goal) => goal.id !== id));  // Update the state to remove the deleted goal
    } catch (err) {
      setError("Failed to delete goal");
    }
  };

  return (
    <div className="container">
      <h2>Goal Management</h2>

      {error && <div className="error">{error}</div>}

      {/* GoalProgress to show progress of goals */}
      <GoalProgress goals={goals} />

      {/* GoalList to list and manage goals */}
      <GoalList goals={goals} handleDelete={handleDelete} />

      {/* Link to add a new goal */}
      <div className="add-goal">
        <Link to="/add-goal">
          <button>Add New Goal</button>
        </Link>
      </div>
    </div>
  );
}

export default GoalManagement;
