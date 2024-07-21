from db import get_db_connection

class Favorite:
    @staticmethod
    def get_by_user_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                ChuongTrinhGiamGia.id,
                ChuongTrinhGiamGia.tenChuongTrinh,
                ChuongTrinhGiamGia.moTa,
                MaGiamGia.ma,
                MaGiamGia.phanTramGiamGia,
                ChuongTrinhGiamGia.ngayBatDau,
                ChuongTrinhGiamGia.ngayKetThuc
            FROM 
                ChuongTrinhYeuThich
            JOIN 
                ChuongTrinhGiamGia ON ChuongTrinhYeuThich.idChuongTrinhGiamGia = ChuongTrinhGiamGia.id
            JOIN 
                MaGiamGia ON MaGiamGia.idChuongTrinhGiamGia = ChuongTrinhGiamGia.id
            WHERE 
                ChuongTrinhYeuThich.idNguoiDung = ? AND ChuongTrinhYeuThich.isDel = 0
        ''', (user_id,))
        favorites = cursor.fetchall()
        conn.close()
        return favorites

    @staticmethod
    def add_favorite(user_id, discount_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO ChuongTrinhYeuThich (idNguoiDung, idChuongTrinhGiamGia, ngayThem, isDel)
            VALUES (?, ?, GETDATE(), 0)
        ''', (user_id, discount_id))
        conn.commit()
        conn.close()

    @staticmethod
    def remove_favorite(user_id, discount_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE ChuongTrinhYeuThich
            SET isDel = 1
            WHERE idNguoiDung = ? AND idChuongTrinhGiamGia = ?
        ''', (user_id, discount_id))
        conn.commit()
        conn.close()
