# models/nhacungcap.py
from db import get_db_connection

class NhaCungCap:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM NhaCungCap WHERE isDel=0')
        nhacungcap = cursor.fetchall()
        conn.close()
        return nhacungcap
