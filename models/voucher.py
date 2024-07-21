from db import get_db_connection

class Voucher:
    @staticmethod
    def add_voucher(ma, phan_tram_giam_gia, ngay_het_han, chuong_trinh_giam_gia_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO MaGiamGia (ma, phanTramGiamGia, ngayHetHan, idChuongTrinhGiamGia)
            VALUES (?, ?, ?, ?)
        ''', (ma, phan_tram_giam_gia, ngay_het_han, chuong_trinh_giam_gia_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_vouchers_with_programs():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                MaGiamGia.id, 
                MaGiamGia.ma, 
                MaGiamGia.phanTramGiamGia, 
                MaGiamGia.ngayHetHan, 
                ChuongTrinhGiamGia.tenChuongTrinh
            FROM 
                MaGiamGia
            JOIN 
                ChuongTrinhGiamGia ON MaGiamGia.idChuongTrinhGiamGia = ChuongTrinhGiamGia.id
            WHERE 
                MaGiamGia.isDel = 0
        ''')
        vouchers = cursor.fetchall()
        conn.close()
        return vouchers

    @staticmethod
    def get_voucher_by_id(voucher_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                id, 
                ma, 
                phanTramGiamGia, 
                ngayHetHan, 
                idChuongTrinhGiamGia
            FROM 
                MaGiamGia
            WHERE 
                id = ? AND isDel = 0
        ''', (voucher_id,))
        voucher = cursor.fetchone()
        conn.close()
        return voucher

    @staticmethod
    def update_voucher(voucher_id, ma, phan_tram_giam_gia, ngay_het_han, chuong_trinh_giam_gia_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE MaGiamGia
            SET ma = ?, phanTramGiamGia = ?, ngayHetHan = ?, idChuongTrinhGiamGia = ?
            WHERE id = ?
        ''', (ma, phan_tram_giam_gia, ngay_het_han, chuong_trinh_giam_gia_id, voucher_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_voucher(voucher_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE MaGiamGia
            SET isDel = 1
            WHERE id = ?
        ''', (voucher_id,))
        conn.commit()
        conn.close()
