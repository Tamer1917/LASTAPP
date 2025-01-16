import sqlite3

# إعداد اتصال بقاعدة البيانات
conn = sqlite3.connect('game_users.db')

# إنشاء جدول المستخدمين
conn.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 username TEXT NOT NULL,
                 join_date TEXT NOT NULL);''')
