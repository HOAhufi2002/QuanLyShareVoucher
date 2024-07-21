from db import get_db_connection
import json

class Feedback:
    @staticmethod
    def get_feedback_by_discount_id(discount_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                PhanHoi.id,
                PhanHoi.noiDung,
                PhanHoi.ngayPhanHoi,  -- Sử dụng cột ngayPhanHoi
                NguoiDung.hoTen
            FROM 
                PhanHoi
            JOIN 
                NguoiDung ON PhanHoi.idNguoiDung = NguoiDung.id
            WHERE 
                PhanHoi.idChuongTrinhGiamGia = ? AND PhanHoi.isDel = 0
        ''', (discount_id,))
        feedbacks = cursor.fetchall()
        conn.close()
        return feedbacks

    @staticmethod
    def add_feedback(user_id, discount_id, content):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO PhanHoi (idNguoiDung, idChuongTrinhGiamGia, noiDung, ngayPhanHoi, isDel)
            VALUES (?, ?, ?, GETDATE(), 0)
        ''', (user_id, discount_id, content))
        conn.commit()
        conn.close()

    @staticmethod
    def get_top_feedback_vouchers():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT TOP 5 magiamgia.ma, COUNT(*) AS soLuongPhanHoi
            FROM PhanHoi
            JOIN magiamgia ON PhanHoi.idChuongTrinhGiamGia = magiamgia.id
            GROUP BY magiamgia.ma
            ORDER BY soLuongPhanHoi DESC
        ''')
        rows = cursor.fetchall()
        conn.close()
        labels = [row[0] for row in rows]
        values = [row[1] for row in rows]
        return {'labels': labels, 'values': values}
