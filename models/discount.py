from db import get_db_connection
from datetime import datetime
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
    @staticmethod
    def get_discount_by_code(discount_code):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT mg.*, ct.idnhacungcap
            FROM MaGiamGia mg
            JOIN ChuongTrinhGiamGia ct ON mg.idChuongTrinhGiamGia = ct.id
            WHERE mg.ma = ?
        ''', (discount_code,))
        discount = cursor.fetchone()
        conn.close()
        return discount
    @staticmethod
    def nhacungcap_add_discount(ma, phan_tram_giam_gia, ngay_het_han, id_chuong_trinh_giam_gia):
        conn = get_db_connection()
        cursor = conn.cursor()

        # Thêm mã giảm giá mới
        cursor.execute('''
            INSERT INTO MaGiamGia (ma, phanTramGiamGia, ngayHetHan, idChuongTrinhGiamGia, isDel)
            VALUES (?, ?, ?, ?, 0)
        ''', (ma, phan_tram_giam_gia, ngay_het_han, id_chuong_trinh_giam_gia))
        conn.commit()

        # Lấy ID của mã giảm giá vừa được chèn vào
        cursor.execute('SELECT @@IDENTITY AS id')
        ma_giam_gia_id = cursor.fetchone()[0]

        # Tạo thông báo mới
        noi_dung = f"Nhà cung cấp đã tạo mã giảm giá mới: {ma}, Giảm {phan_tram_giam_gia}%."
        ngay_gui = datetime.now().date()
        cursor.execute('''
            INSERT INTO ThongBao (noiDung, ngayGui)
            VALUES (?, ?)
        ''', (noi_dung, ngay_gui))
        conn.commit()

        # Lấy ID của thông báo vừa được chèn vào
        cursor.execute('SELECT @@IDENTITY AS id')
        thong_bao_id = cursor.fetchone()[0]

        # Gửi thông báo cho tất cả người dùng
        cursor.execute('''
            INSERT INTO ThongBao_NguoiDung (idThongBao, idNguoiDung, trangThai)
            SELECT ?, id, 'chuaDoc' FROM NguoiDung
        ''', (thong_bao_id,))
        conn.commit()

        conn.close()
        
    @staticmethod
    def nhacungcap_get_discounts_by_supplier(id_nha_cung_cap):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT mg.*, ctg.tenChuongTrinh, ctg.moTa
            FROM MaGiamGia mg
            JOIN ChuongTrinhGiamGia ctg ON mg.idChuongTrinhGiamGia = ctg.id
            WHERE ctg.idNhaCungCap = ? AND mg.isDel = 0
        ''', (id_nha_cung_cap,))
        discounts = cursor.fetchall()
        conn.close()
        return discounts