from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = 'tasks.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            due_date TEXT,
            completed INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    filter_by = request.args.get('filter', 'all')
    search_query = request.args.get('search', '').lower()

    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    if filter_by == 'completed':
        c.execute("SELECT * FROM tasks WHERE completed = 1")
    elif filter_by == 'pending':
        c.execute("SELECT * FROM tasks WHERE completed = 0")
    else:
        c.execute("SELECT * FROM tasks")

    tasks = c.fetchall()
    conn.close()

    filtered_tasks = [
        t for t in tasks if search_query in t[1].lower() or (t[2] and search_query in t[2].lower())
    ]

    return render_template('index.html', tasks=filtered_tasks, selected_filter=filter_by)

@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    description = request.form.get('description')
    due_date = request.form.get('due_date')
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('INSERT INTO tasks (title, description, due_date) VALUES (?, ?, ?)',
              (title, description, due_date))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    new_title = request.form['title']
    new_description = request.form.get('description')
    new_due_date = request.form.get('due_date')
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('UPDATE tasks SET title = ?, description = ?, due_date = ? WHERE id = ?',
              (new_title, new_description, new_due_date, task_id))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
