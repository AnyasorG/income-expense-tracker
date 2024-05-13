const express = require("express");
const bodyParser = require("body-parser");

const app = express();
const PORT = 3000;

// Middleware
app.use(bodyParser.json());

// Routes
app.post("/signup", (req, res) => {
    const { username, password } = req.body;
    // Save username and hashed password to the database (not implemented yet)
    console.log("Signup:", { username, password });
    res.sendStatus(200);
});

app.post("/login", (req, res) => {
    const { username, password } = req.body;
    // Check username and password against the database (not implemented yet)
    console.log("Login:", { username, password });
    res.sendStatus(200);
});

// Handle root route
app.get("/", (req, res) => {
    res.send("Welcome to the Income and Expense Tracker!");
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
