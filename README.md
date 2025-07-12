# Flask-To-do-App
# TaskFlow - Flask-Based Task Manager

**TaskFlow** is a simple, user-friendly web application built using Flask (Python), allowing users to manage their tasks efficiently. It supports features like adding tasks, editing, deleting, marking as completed, due dates, filtering, search, and dark mode.

---

## 🚀 Features

* ✅ Add / Edit / Delete tasks
* 📅 Assign and view due dates
* 🟢 Mark tasks as completed
* 🔍 Search by title or description
* 🗂️ Filter tasks by All / Completed / Pending
* 🌙 Toggle between light and dark themes
* 💻 Responsive design for desktop and mobile

---

## 📦 Tech Stack

* **Backend:** Flask (Python)
* **Frontend:** HTML, CSS, JavaScript
* **Database:** SQLite

---

## 🛠️ Installation & Setup

### Prerequisites:

* Python 3.7+

### Steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/taskflow.git
   cd taskflow
   ```
2. Install Flask:

   ```bash
   pip install flask
   ```
3. Run the app:

   ```bash
   python app.py
   ```
4. Open your browser and navigate to:

   ```
   http://127.0.0.1:5000/
   ```

---

## 📁 Project Structure

```
taskflow/
├── app.py
├── tasks.db (auto-generated)
├── templates/
│   └── index.html
└── static/
    ├── style.css
    └── script.js
```

---

## 🧪 Testing

* Manual testing was conducted for all CRUD operations
* Filter and search tested with various inputs
* UI tested on mobile and desktop screens

---

## 🐞 Troubleshooting

| Problem            | Solution                                  |
| ------------------ | ----------------------------------------- |
| App not starting   | Ensure Flask is installed and Python 3.7+ |
| CSS/JS not loading | Check static folder and file references   |
| DB not updating    | Ensure `tasks.db` has write permissions   |

---

## 📌 Future Improvements

* User authentication
* Task prioritization (High, Medium, Low)
* Notifications / Reminders
* Drag-and-drop task sorting
* Deployment to Render / Heroku

---

## 🙌 Acknowledgements

This project was built as part of my internship at **Infotact** while learning Flask. Special thanks to the mentors and teammates for their guidance and support!

---



## 👤 Author

**Sirisha Bantupakiri**
[LinkedIn](https://www.linkedin.com/in/sirisha-bantupakiri)
