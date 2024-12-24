// src/App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

// Main Pages
import Home from './pages/Home';
import AdminDashboard from './pages/AdminDashboard';
import BudgetDashboard from './pages/BudgetDashboard';
import GoalManagement from './pages/GoalManagement';
import BudgetOverview from './components/Dashboard/BudgetOverview';

// Jars Pages
import AddJar from './components/Jars/AddJar';
import EditJar from './components/Jars/EditJar';
import JarList from './components/Jars/JarList';

// Expenses Pages
import AddExpense from './components/Expenses/AddExpense';
import EditExpense from './components/Expenses/EditExpense';
import ExpenseList from './components/Expenses/ExpenseList';

// Goals Pages
import AddGoal from './components/Goals/AddGoal';
import EditGoal from './components/Goals/EditGoal';
import GoalProgress from './components/Goals/GoalProgress';

// Incomes Pages
import AddIncome from './components/Incomes/AddIncome';
import EditIncome from './components/Incomes/EditIncome';
import IncomeList from './components/Incomes/IncomeList';

function App() {
  return (
    <Router>
      <Routes>
        {/* Main Pages */}
        <Route path="/" element={<Home />} />
        <Route path="/admin" element={<AdminDashboard />} />
        <Route path="/budget-dashboard" element={<BudgetDashboard />} />
        <Route path="/goal-management" element={<GoalManagement />} />
        <Route path="/budget-overview" element={<BudgetOverview />} />

        {/* Jars Routes */}
        <Route path="/add-jar" element={<AddJar />} />
        <Route path="/edit-jar/:id" element={<EditJar />} />
        <Route path="/jars" element={<JarList />} />
        
        {/* Expenses Routes */}
        <Route path="/add-expense" element={<AddExpense />} />
        <Route path="/edit-expense/:id" element={<EditExpense />} />
        <Route path="/expenses" element={<ExpenseList />} />

        {/* Goals Routes */}
        <Route path="/add-goal" element={<AddGoal />} />
        <Route path="/edit-goal/:id" element={<EditGoal />} />
        <Route path="/goal-progress" element={<GoalProgress />} />

        {/* Incomes Routes */}
        <Route path="/add-income" element={<AddIncome />} />
        <Route path="/edit-income/:id" element={<EditIncome />} />
        <Route path="/income-list" element={<IncomeList />} />
      </Routes>
    </Router>
  );
}

export default App;
