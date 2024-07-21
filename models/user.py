from db import get_db_connection

class User:
    @staticmethod
    def get_by_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, hoTen, email, matkhau
            FROM NguoiDung
            WHERE id = ?
        ''', (user_id,))
        user = cursor.fetchone()
        conn.close()
        return user

    @staticmethod
    def update_user_info(user_id, ho_ten, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE NguoiDung
            SET hoTen = ?, email = ?
            WHERE id = ?
        ''', (ho_ten, email, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def update_password(user_id, hashed_password):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE NguoiDung
            SET matkhau = ?
            WHERE id = ?
        ''', (hashed_password, user_id))
        conn.commit()
        conn.close()
