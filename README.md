# Smart Expense Splitter 💰

A simple, intuitive tool to manage shared expenses among a group of people. Add members, track expenses, and automatically calculate who owes whom.

Built with **Flask (Python backend)** and a clean **HTML/CSS frontend**.

## 🚀 Live Demo

Check out the live version hosted on Render:
[🔗 Smart Expense Splitter](https://smart-expense-splitter-hzkh.onrender.com/)

## 🛠 Features

- Add and delete members dynamically
- Record expenses with category, payer, and amount
- Automatically calculate total spent by each member
- Generate settlements: who owes whom
- Reset all data to start fresh
- Responsive and minimalistic frontend

## 📁 Project Structure
```
smart-expense-splitter/
│
├── app.py             # Main Flask backend application
├── init_db.py         # Initializes SQLite DB with sample members
├── requirements.txt   # Python dependencies
├── Dockerfile         # Containerization for deployment
├── templates/         # HTML templates
│   ├── index.html
│   └── summary.html
└── static/
    └── style.css      # Frontend styling
```

## 🔧 Technologies Used

- Python (Flask, SQLite)
- HTML / CSS / Jinja2 Templates
- Docker (for containerized deployment)
- Render (for hosting)

## ✨ Acknowledgements

- Backend powered by Flask
- Frontend built with HTML/CSS
- Deployed live on Render
