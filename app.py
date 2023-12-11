from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Створення бази даних та таблиці
conn = sqlite3.connect('employees.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        last_name TEXT,
        first_name TEXT,
        position TEXT,
        years_worked INTEGER
    )
''')
conn.commit()
conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return render_template('index.html', employees=employees)

@app.route('/add_employee', methods=['POST'])
def add_employee():
    last_name = request.form['last_name']
    first_name = request.form['first_name']
    position = request.form['position']
    years_worked = request.form['years_worked']

    conn = sqlite3.connect('employees.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO employees (last_name, first_name, position, years_worked)
        VALUES (?, ?, ?, ?)
    ''', (last_name, first_name, position, years_worked))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
