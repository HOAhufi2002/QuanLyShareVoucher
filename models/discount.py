from db import get_db_connection

class Discount:
    @staticmethod
    def add_discount(ten_chuong_trinh, mo_ta, ngay_bat_dau, ngay_ket_thuc, nha_cung_cap_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO ChuongTrinhGiamGia (tenChuongTrinh, moTa, ngayBatDau, ngayKetThuc, idNhaCungCap)
            VALUES (?, ?, ?, ?, ?)
        ''', (ten_chuong_trinh, mo_ta, ngay_bat_dau, ngay_ket_thuc, nha_cung_cap_id))
        conn.commit()
        conn.close()
    @staticmethod
    def get_all_discounts_with_suppliers():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                ChuongTrinhGiamGia.id, 
                ChuongTrinhGiamGia.tenChuongTrinh, 
                ChuongTrinhGiamGia.moTa, 
                ChuongTrinhGiamGia.ngayBatDau, 
                ChuongTrinhGiamGia.ngayKetThuc, 
                NhaCungCap.tenNhaCungCap
            FROM 
                ChuongTrinhGiamGia
            JOIN 
                NhaCungCap ON ChuongTrinhGiamGia.idNhaCungCap = NhaCungCap.id
            WHERE 
                ChuongTrinhGiamGia.isDel = 0
        ''')
        discounts = cursor.fetchall()
        conn.close()
        return discounts
    @staticmethod
    def get_all_discounts():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                ChuongTrinhGiamGia.id, 
                ChuongTrinhGiamGia.tenChuongTrinh, 
                ChuongTrinhGiamGia.moTa, 
                ChuongTrinhGiamGia.ngayBatDau, 
                ChuongTrinhGiamGia.ngayKetThuc, 
                MaGiamGia.phanTramGiamGia,
                MaGiamGia.ma,
                NhaCungCap.tenNhaCungCap
            FROM 
                ChuongTrinhGiamGia
            JOIN 
                MaGiamGia ON ChuongTrinhGiamGia.id = MaGiamGia.idChuongTrinhGiamGia
            JOIN 
                NhaCungCap ON ChuongTrinhGiamGia.idNhaCungCap = NhaCungCap.id
            WHERE 
                ChuongTrinhGiamGia.isDel = 0 AND MaGiamGia.isDel = 0
        ''')
        discounts = cursor.fetchall()
        conn.close()
        return discounts

    @staticmethod
    def get_discount_by_id(discount_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                ChuongTrinhGiamGia.id, 
                ChuongTrinhGiamGia.tenChuongTrinh, 
                ChuongTrinhGiamGia.moTa, 
                ChuongTrinhGiamGia.ngayBatDau, 
                ChuongTrinhGiamGia.ngayKetThuc, 
                MaGiamGia.phanTramGiamGia,
                MaGiamGia.ma,
                ChuongTrinhGiamGia.idNhaCungCap
            FROM 
                ChuongTrinhGiamGia
            JOIN 
                MaGiamGia ON ChuongTrinhGiamGia.id = MaGiamGia.idChuongTrinhGiamGia
            WHERE 
                ChuongTrinhGiamGia.id = ? AND ChuongTrinhGiamGia.isDel = 0 AND MaGiamGia.isDel = 0
        ''', (discount_id,))
        discount = cursor.fetchone()
        conn.close()
        return discount
    @staticmethod
    def update_discount(discount_id, ten_chuong_trinh, mo_ta, ngay_bat_dau, ngay_ket_thuc, nha_cung_cap_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE ChuongTrinhGiamGia
            SET tenChuongTrinh = ?, moTa = ?, ngayBatDau = ?, ngayKetThuc = ?, idNhaCungCap = ?
            WHERE id = ?
        ''', (ten_chuong_trinh, mo_ta, ngay_bat_dau, ngay_ket_thuc, nha_cung_cap_id, discount_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_discount(discount_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE ChuongTrinhGiamGia
            SET isDel = 1
            WHERE id = ?
        ''', (discount_id,))
        conn.commit()
        conn.close()
    @staticmethod
    def get_all_discounts_for_voucher():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                id, 
                tenChuongTrinh
            FROM 
                ChuongTrinhGiamGia
            WHERE 
                isDel = 0
        ''')
        discounts = cursor.fetchall()
        conn.close()
        return discounts
    @staticmethod
    def search_discounts(search=None, expiry_date=None, discount_percent=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = '''
            SELECT 
                ChuongTrinhGiamGia.id,
                ChuongTrinhGiamGia.tenChuongTrinh,
                ChuongTrinhGiamGia.moTa,
                ChuongTrinhGiamGia.ngayBatDau,
                ChuongTrinhGiamGia.ngayKetThuc,
                MaGiamGia.ma,
                MaGiamGia.phanTramGiamGia
            FROM 
                ChuongTrinhGiamGia
            JOIN 
                MaGiamGia ON ChuongTrinhGiamGia.id = MaGiamGia.idChuongTrinhGiamGia
            WHERE 
                ChuongTrinhGiamGia.isDel = 0 AND MaGiamGia.isDel = 0
        '''
        params = []

        if search:
            query += ' AND ChuongTrinhGiamGia.tenChuongTrinh LIKE ?'
            params.append(f'%{search}%')
        if expiry_date:
            query += ' AND MaGiamGia.ngayHetHan <= ?'
            params.append(expiry_date)
        if discount_percent:
            query += ' AND MaGiamGia.phanTramGiamGia >= ?'
            params.append(discount_percent)

        cursor.execute(query, params)
        discounts = cursor.fetchall()
        conn.close()
        return discounts