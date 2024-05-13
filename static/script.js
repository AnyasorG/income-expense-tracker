// static/script.js

// JavaScript code for client-side interactions
document.addEventListener("DOMContentLoaded", function () {
    const signupForm = document.getElementById("signupForm");
    const loginForm = document.getElementById("loginForm");

    signupForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const username = signupForm.querySelector("#signupUsername").value;
        const password = signupForm.querySelector("#signupPassword").value;
        // Send signup request to the server (not implemented yet)
        console.log("Signup:", { username, password });

        // Clear input fields after form submission
        signupForm.reset();
    });

    loginForm.addEventListener("submit", function (event) {
        event.preventDefault();
        const username = loginForm.querySelector("#loginUsername").value;
        const password = loginForm.querySelector("#loginPassword").value;
        // Send login request to the server (not implemented yet)
        console.log("Login:", { username, password });

        // Clear input fields after form submission
        loginForm.reset();
    });
});
