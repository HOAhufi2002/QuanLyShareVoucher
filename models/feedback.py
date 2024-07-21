from db import get_db_connection

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
