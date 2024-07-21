# models/search.py
from db import get_db_connection

class SearchHistory:
    @staticmethod
    def get_by_user_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM LichSuTimKiem WHERE idNguoiDung=? AND isDel=0', (user_id,))
        history = cursor.fetchall()
        conn.close()
        return history

    @staticmethod
    def add_search(user_id, keyword):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO LichSuTimKiem (idNguoiDung, tuKhoa, isDel) VALUES (?, ?, 0)', (user_id, keyword))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_search(user_id, keyword):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('UPDATE LichSuTimKiem SET isDel=1 WHERE idNguoiDung=? AND tuKhoa=?', (user_id, keyword))
        conn.commit()
        conn.close()
