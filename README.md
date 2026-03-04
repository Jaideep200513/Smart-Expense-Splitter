# Smart Expense Splitter 💰
#### Video Demo: [https://youtu.be/HakefN077Eo?si=cWZW-6a5gj9dPP7X](https://youtu.be/HakefN077Eo?si=cWZW-6a5gj9dPP7X)
#### Description:

The **Smart Expense Splitter** is a Flask-based web application designed to simplify shared expense management among groups of people. Whether it’s for roommates, friends traveling together, or colleagues splitting bills, this tool helps users easily manage who paid for what and who owes whom.

### Project Overview
The project provides an intuitive interface where users can:
- Add and remove members dynamically.
- Log expenses by specifying who paid, for what, and how much.
- View all transactions in a clear list.
- Automatically calculate a summary showing total contributions and settlements (who owes whom).
- Reset data anytime to start a new session.

This eliminates the manual effort of calculating balances or using spreadsheets to track group expenses.

---

### Technical Details
The project is built with **Flask (Python)** for the backend, **SQLite** for local data storage, and **HTML/CSS (Jinja templates)** for the frontend. The database and app logic are lightweight, making the app easy to deploy anywhere.

#### Files and Their Roles:

- **`app.py`** – The main Flask application that handles all routes, including adding members, logging expenses, calculating summaries, and resetting data.
- **`init_db.py`** – Initializes the SQLite database and preloads it with five sample members to help users get started.
- **`templates/index.html`** – The main dashboard page where users can add members and record expenses.
- **`templates/summary.html`** – Displays the total spent by each member and who owes whom.
- **`static/style.css`** – Handles the visual styling of the interface.
- **`requirements.txt`** – Lists the project dependencies (`Flask`, `gunicorn`) for easy setup.
- **`Dockerfile`** – Used for containerizing the app to deploy easily on Render or similar platforms.

---

### How It Works
1. When the app starts, it checks if the database exists; if not, it creates one using `init_db.py`.
2. Users can add new members to the group via the interface.
3. Each expense is linked to the member who paid, with category, amount, and timestamp recorded.
4. The **Summary** section computes:
   - Total expenses for each member.
   - How much each member owes or is owed.
   - A settlement list showing minimum transactions required to balance everything.
5. The **Reset** button clears all data for a fresh start.

---

### Design Choices
- **Flask** was chosen for its simplicity and seamless integration with HTML templates.
- **SQLite** was used since it’s lightweight and perfect for a local web app (no external DB setup needed).
- The **minimal UI** was intentional — clean, distraction-free, and easy to understand.
- **Dockerization** ensures the project runs identically on any environment (local or cloud).

---

### Deployment
The project was containerized using **Docker** and deployed successfully on **Render**.  
Live demo: [https://smart-expense-splitter-hzkh.onrender.com/](https://smart-expense-splitter-hzkh.onrender.com/)

---

### Reflection
This project allowed me to apply the concepts learned throughout **CS50**, including:
- Backend logic and routing with Flask.
- Database management with SQL.
- Web design using HTML/CSS.
- Debugging and deployment workflows.

Building this project was both challenging and rewarding, as it brought together all the foundational knowledge from the course into a real, practical tool that people can use daily.
