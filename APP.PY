from flask import Flask, request, render_template
import sqlite3
from markupsafe import escape

app = Flask(__name__)

# إنشاء قاعدة البيانات والجداول إذا لم تكن موجودة
def init_db():
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                         id INTEGER PRIMARY KEY,
                         username TEXT NOT NULL,
                         points INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        points = int(request.form['points'])
        
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        
        c.execute("SELECT * FROM users WHERE username=?", (username,))
        user = c.fetchone()
        
        if user:
            c.execute("UPDATE users SET points=? WHERE username=?", (points, username))
        else:
            c.execute("INSERT INTO users (username, points) VALUES (?, ?)", (username, points))
        
        conn.commit()
        conn.close()

    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute("SELECT * FROM users")
    users = c.fetchall()
    conn.close()
    
    return render_template('index.html', users=users)

@app.route('/users')
def show_users():
    conn = sqlite3.connect