# models/nguoidung.py
from db import get_db_connection

class NguoiDung:
    @staticmethod
    def get_by_email_and_password(email, password):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM NguoiDung WHERE email=? AND matKhau=? AND isDel=0', (email, password))
        user = cursor.fetchone()
        conn.close()
        return user

    @staticmethod
    def get_by_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM NguoiDung WHERE id=? AND isDel=0', (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user
