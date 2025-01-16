import sqlite3
import telebot

# تهيئة البوت
API_TOKEN = '7679813979:AAGWex1J2x6mIabmBgKMXGhGuILrPN2wLGo'
bot = telebot.TeleBot(API_TOKEN)

# إنشاء قاعدة البيانات (يمكنك وضع هذا الجزء في بداية السكربت)
def create_database():
    conn = sqlite3.connect('chess_game.db')
    cursor = conn.cursor()

    # إنشاء جدول المستخدمين إذا لم يكن موجودًا
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        first_name TEXT,
        last_name TEXT,
        date_joined TEXT
    )
    ''')

    # إنشاء جدول النقاط إذا لم يكن موجودًا
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_points (
        user_id INTEGER PRIMARY KEY,
        points INTEGER DEFAULT 0,
        FOREIGN KEY (user_id) REFERENCES users(user_id)
    )
    ''')

    conn.commit()
    conn.close()

# إضافة مستخدم جديد
def add_new_user(user_id, username, first_name, last_name):
    conn = sqlite3.connect('chess_game.db')
    cursor = conn.cursor()

    # إضافة المستخدم إلى جدول المستخدمين
    cursor.execute('''
    INSERT OR IGNORE INTO users (user_id, username, first_name, last_name, date_joined)
    VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)
    ''', (user_id, username, first_name, last_name))

    # إضافة المستخدم إلى جدول النقاط مع 5 نقاط مبدئية
    cursor.execute('''
    INSERT OR IGNORE INTO user_points (user_id, points)
    VALUES (?, 5)
    ''', (user_id,))

    conn.commit()
    conn.close()

# استرجاع بيانات المستخدم
def get_user_data(user_id):
    conn = sqlite3.connect('chess_game.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users WHERE user_id = ?', (user_id,))
    user_data = cursor.fetchone()

    conn.close()
    return user_data

# استرجاع النقاط للمستخدم
def get_user_points(user_id):
    conn = sqlite3.connect('chess_game.db')
    cursor = conn.cursor()

    cursor.execute('SELECT points FROM user_points WHERE user_id = ?', (user_id,))
    points = cursor.fetchone()

    conn.close()
    return points[0] if points else 0

# معالجة أمر البدء /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name

    # إضافة المستخدم إلى قاعدة البيانات
    add_new_user(user_id, username, first_name, last_name)

    # استرجاع النقاط الحالية
    points = get_user_points(user_id)

    bot.reply_to(message, f"أهلاً وسهلاً بك في لعبة الشطرنج! لديك {points} نقاط.")

# تشغيل البوت
if __name__ == "__main__":
    create_database()  # تأكد من أن قاعدة البيانات موجودة
    bot.polling()








