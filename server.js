const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());

// Placeholder arrays to store income and expenses
let incomeList = [];
let expenseList = [];

// Routes

// Route to add income
app.post("/income", (req, res) => {
    const { amount, description } = req.body;

    // Validate incoming data
    if (!amount || !description) {
        return res.status(400).json({ error: "Amount and description are required." });
    }

    // Add income to the list
    const newIncome = { amount, description };
    incomeList.push(newIncome);

    // Send success response
    res.status(201).json({ message: "Income added successfully", income: newIncome });
});

// Route to add expense
app.post("/expenses", (req, res) => {
    const { amount, description } = req.body;

    // Validate incoming data
    if (!amount || !description) {
        return res.status(400).json({ error: "Amount and description are required." });
    }

    // Add expense to the list
    const newExpense = { amount, description };
    expenseList.push(newExpense);

    // Send success response
    res.status(201).json({ message: "Expense added successfully", expense: newExpense });
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
