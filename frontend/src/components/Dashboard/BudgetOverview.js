import React, { useEffect, useState } from 'react';
import { getBudgetOverview } from '../../services/api';

function BudgetOverview() {
    const [budget, setBudget] = useState({});

    useEffect(() => {
        const fetchBudget = async () => {
            const data = await getBudgetOverview();
            setBudget(data);
        };
        fetchBudget();
    }, []);

    return (
        <div className="container">
            <h2>Budget Overview</h2>
            <p>Total Income: ${budget.totalIncome}</p>
            <p>Total Expenses: ${budget.totalExpenses}</p>
            <p>Remaining Budget: ${budget.remainingBudget}</p>
            <p>Overspending: {budget.overspending ? 'Yes' : 'No'}</p>
        </div>
    );
}

export default BudgetOverview;
