# utils.py
from models.notification import ThongBao

def get_unread_notifications_count(user_id):
    return ThongBao.get_unread_notifications_count(user_id)
