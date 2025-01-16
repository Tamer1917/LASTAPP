import sqlite3

conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

print("id | username | user_id")
print("-" * 30)
for row in rows:
    print(f"{row[0]} | {row[1]} | {row[2]}")

conn.close()
