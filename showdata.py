import sqlite3

def show_users():
    conn = sqlite3.connect('chess_game.db')
    cursor = conn.cursor()

    # إجراء انضمام بين جدول users وجدول user_points
    cursor.execute('''
    SELECT 
        users.user_id, 
        users.username, 
        users.first_name, 
        users.last_name, 
        users.date_joined, 
        user_points.points
    FROM 
        users
    LEFT JOIN 
        user_points 
    ON 
        users.user_id = user_points.user_id
    ''')

    users = cursor.fetchall()

    # عرض البيانات
    for user in users:
        print(f"ID: {user[0]}, Username: {user[1]}, First Name: {user[2]}, Last Name: {user[3]}, Date Joined: {user[4]}, Points: {user[5]}")

    conn.close()

if __name__ == "__main__":
    show_users()
