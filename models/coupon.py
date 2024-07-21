from db import get_db_connection

class Coupon:
    @staticmethod
    def get_all_coupons():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, ma, phanTramGiamGia, ngayHetHan, idChuongTrinhGiamGia
            FROM MaGiamGia
            WHERE isDel = 0
        ''')
        coupons = cursor.fetchall()
        conn.close()
        return coupons

    @staticmethod
    def get_coupon_by_id(coupon_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, ma, phanTramGiamGia, ngayHetHan, idChuongTrinhGiamGia
            FROM MaGiamGia
            WHERE id = ? AND isDel = 0
        ''', (coupon_id,))
        coupon = cursor.fetchone()
        conn.close()
        return coupon

    @staticmethod
    def add_coupon(ma, phan_tram_giam_gia, ngay_het_han, id_chuong_trinh_giam_gia):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO MaGiamGia (ma, phanTramGiamGia, ngayHetHan, idChuongTrinhGiamGia, isDel)
            VALUES (?, ?, ?, ?, 0)
        ''', (ma, phan_tram_giam_gia, ngay_het_han, id_chuong_trinh_giam_gia))
        conn.commit()
        conn.close()

    @staticmethod
    def update_coupon(coupon_id, ma, phan_tram_giam_gia, ngay_het_han, id_chuong_trinh_giam_gia):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE MaGiamGia
            SET ma = ?, phanTramGiamGia = ?, ngayHetHan = ?, idChuongTrinhGiamGia = ?
            WHERE id = ? AND isDel = 0
        ''', (ma, phan_tram_giam_gia, ngay_het_han, id_chuong_trinh_giam_gia, coupon_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_coupon(coupon_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE MaGiamGia
            SET isDel = 1
            WHERE id = ?
        ''', (coupon_id,))
        conn.commit()
        conn.close()
