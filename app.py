from flask import Flask,session,g
from routes import main_bp, auth_bp, admin_bp, discount_bp, favorite_bp, supplier_bp, notification_bp, search_bp, feedback_bp
from models.notification import Notification
from routes.auth import auth_bp

app = Flask(__name__)

# Đặt secret key
app.secret_key = 'cascascascas112y'  # Thay 'your_secret_key' bằng một chuỗi ký tự bí mật bất kỳ

app.register_blueprint(main_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(discount_bp)
app.register_blueprint(favorite_bp)
app.register_blueprint(supplier_bp)
app.register_blueprint(notification_bp)
app.register_blueprint(search_bp)
app.register_blueprint(feedback_bp)

@app.before_request
def before_request():
    if 'user_id' in session:
        user_id = session['user_id']
        notifications = Notification.get_notifications(user_id)
        g.notification_count = len([n for n in notifications if n[3] == 'chuaDoc'])
    else:
        g.notification_count = 0
if __name__ == '__main__':
    app.run(debug=True)
