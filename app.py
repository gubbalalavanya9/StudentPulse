from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('student.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def dashboard():
    conn = get_db_connection()
    total = conn.execute('SELECT COUNT(*) FROM students').fetchone()[0]
    depts = conn.execute('SELECT DISTINCT department FROM students').fetchall()
    conn.close()
    return render_template('dashboard.html', total=total, depts=depts)

@app.route('/add')
def add_page():
    return render_template('add_student.html')

@app.route('/add_student', methods=['POST'])
def add_student():
    data = (
        request.form['name'],
        request.form['roll'],
        request.form['dept'],
        request.form['year']
    )
    conn = get_db_connection()
    conn.execute(
        'INSERT INTO students (name, roll_no, department, year) VALUES (?,?,?,?)',
        data
    )
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/students')
def students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return render_template('view_students.html', students=students)

@app.route('/department/<dept>')
def department(dept):
    conn = get_db_connection()
    students = conn.execute(
        'SELECT * FROM students WHERE department=?', (dept,)
    ).fetchall()
    conn.close()
    return render_template('department.html', students=students, dept=dept)

if __name__ == '__main__':
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            roll_no TEXT,
            department TEXT,
            year INTEGER
        )
    ''')
    conn.commit()
    conn.close()
    app.run(debug=True)