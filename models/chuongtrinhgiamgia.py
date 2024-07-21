# models/chuongtrinhgiamgia.py
from db import get_db_connection

class ChuongTrinhGiamGia:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
        SELECT 
            MaGiamGia.ma,
            MaGiamGia.phanTramGiamGia,
            ChuongTrinhGiamGia.ngayBatDau,
            ChuongTrinhGiamGia.ngayKetThuc,
            ChuongTrinhGiamGia.tenChuongTrinh,
            ChuongTrinhGiamGia.moTa
        FROM 
            MaGiamGia
        JOIN 
            ChuongTrinhGiamGia ON MaGiamGia.idChuongTrinhGiamGia = ChuongTrinhGiamGia.id
        WHERE 
            MaGiamGia.isDel = 0 AND ChuongTrinhGiamGia.isDel = 0
    ''')
        chuongtrinh = cursor.fetchall()
        conn.close()
        return chuongtrinh

    @staticmethod
    def get_by_id(chuongtrinh_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM ChuongTrinhGiamGia WHERE id=? AND isDel=0', (chuongtrinh_id,))
        chuongtrinh = cursor.fetchone()
        conn.close()
        return chuongtrinh
