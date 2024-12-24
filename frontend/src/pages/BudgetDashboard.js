import React from 'react';
import { Link } from 'react-router-dom';
import JarList from '../components/Jars/JarList';
import ExpenseList from '../components/Expenses/ExpenseList';
import GoalProgress from '../components/Goals/GoalProgress';
import IncomeList from '../components/Income/IncomeList';
import BudgetOverview from '../components/Dashboard/BudgetOverview';

function BudgetDashboard() {
  return (
    <div className="container">
      <h2>Budget Dashboard</h2>
      
      {/* Budget Overview */}
      <BudgetOverview />

      {/* Jars Section */}
      <div className="section">
        <h3>Your Jars</h3>
        <JarList />
        <Link to="/add-jar">Add Jar</Link>
      </div>

      {/* Expenses Section */}
      <div className="section">
        <h3>Your Expenses</h3>
        <ExpenseList />
        <Link to="/add-expense">Add Expense</Link>
      </div>

      {/* Goals Section */}
      <div className="section">
        <h3>Your Goals</h3>
        <GoalProgress />
        <Link to="/add-goal">Add Goal</Link>
      </div>

      {/* Incomes Section */}
      <div className="section">
        <h3>Your Incomes</h3>
        <IncomeList />
        <Link to="/add-income">Add Income</Link>
      </div>
    </div>
  );
}

export default BudgetDashboard;
