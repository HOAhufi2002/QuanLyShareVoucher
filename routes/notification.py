from flask import Blueprint, render_template, redirect, url_for, session
from models.notification import Notification

notification_bp = Blueprint('notification', __name__)

@notification_bp.route('/notifications', methods=['GET'])
def notifications():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    notifications = Notification.get_notifications(session['user_id'])
    return render_template('notifications.html', notifications=notifications)

@notification_bp.route('/mark_as_read/<int:notification_id>', methods=['POST'])
def mark_as_read(notification_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    Notification.mark_as_read(notification_id, session['user_id'])
    return redirect(url_for('notification.notifications'))
