from flask import Flask, render_template, request, jsonify

# إنشاء تطبيق Flask
app = Flask(__name__)

# مسار الصفحة الرئيسية يعرض رسالة نصية
@app.route('/')
def home():
    # عرض صفحة index.html من مجلد templates
    return render_template('index.html')

# مسار يعرض صفحة HTML
@app.route('/html')
def html_page():
    return render_template('index.html')

# مسار لقبول بيانات المستخدم
@app.route('/save-user', methods=['POST'])
def save_user():
    # استقبال بيانات JSON من الطلب
    user_data = request.get_json()
    if not user_data:
        return jsonify({"error": "لا توجد بيانات"}), 400
    
    # استخراج البيانات وإجراء معالجتك
    user_id = user_data.get('userId')
    username = user_data.get('username')

    # هنا يمكن إضافة المنطق لحفظ المستخدم في قاعدة البيانات
    print(f"استقبال بيانات المستخدم: {user_data}")

    return jsonify({"message": "تم حفظ بيانات المستخدم بنجاح!"}), 200

# مسار للـ favicon.ico
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

# تشغيل الخادم
if __name__ == '__main__':
    app.run(debug=True)
