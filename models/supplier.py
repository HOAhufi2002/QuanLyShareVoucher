# models/supplier.py
from db import get_db_connection

class Supplier:
    @staticmethod
    def get_all_suppliers():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, tenNhaCungCap, diaChi, soDienThoai, email FROM NhaCungCap WHERE isDel = 0
        ''')
        suppliers = cursor.fetchall()
        conn.close()
        return suppliers

    @staticmethod
    def get_supplier_by_id(supplier_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM NhaCungCap WHERE id = ?', (supplier_id,))
        supplier = cursor.fetchone()
        cursor.execute('''
            SELECT p.id, p.tensanpham, p.gia, p.idmagiamgia, m.ma
            FROM SanPham p
            LEFT JOIN MaGiamGia m ON p.idmagiamgia = m.id
            WHERE p.idnhacungcap = ? AND p.isdel = 0
        ''', (supplier_id,))
        products = cursor.fetchall()
        cursor.execute('''
            SELECT ctg.id, ctg.tenChuongTrinh, ctg.moTa, ctg.ngayBatDau, ctg.ngayKetThuc, mg.ma, mg.phanTramGiamGia
            FROM ChuongTrinhGiamGia ctg
            LEFT JOIN MaGiamGia mg ON ctg.id = mg.idChuongTrinhGiamGia
            WHERE ctg.idNhaCungCap = ? AND ctg.isDel = 0
        ''', (supplier_id,))
        discounts = cursor.fetchall()
        conn.close()
        return supplier, products, discounts
    @staticmethod
    def get_discounts_by_supplier_id(supplier_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT 
                MaGiamGia.id,
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
                ChuongTrinhGiamGia.idNhaCungCap = ? AND MaGiamGia.isDel = 0 AND ChuongTrinhGiamGia.isDel = 0
        ''', (supplier_id,))
        discounts = cursor.fetchall()
        conn.close()
        return discounts
    @staticmethod
    def add_supplier(ten_nha_cung_cap, dia_chi, so_dien_thoai, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO NhaCungCap (tenNhaCungCap, diaChi, soDienThoai, email)
            VALUES (?, ?, ?, ?)
        ''', (ten_nha_cung_cap, dia_chi, so_dien_thoai, email))
        conn.commit()
        conn.close()
    @staticmethod
    def update_supplier(supplier_id, ten_nha_cung_cap, dia_chi, so_dien_thoai, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE NhaCungCap
            SET tenNhaCungCap = ?, diaChi = ?, soDienThoai = ?, email = ?
            WHERE id = ?
        ''', (ten_nha_cung_cap, dia_chi, so_dien_thoai, email, supplier_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_supplier(supplier_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM NhaCungCap WHERE id = ?
        ''', (supplier_id,))
        conn.commit()
        conn.close()
    @staticmethod
    def get_all_suppliers():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, tenNhaCungCap FROM NhaCungCap WHERE isDel = 0')
        suppliers = cursor.fetchall()
        conn.close()
        return suppliers
    @staticmethod
    def update_supplier_info(user_id, ten_nha_cung_cap, dia_chi, so_dien_thoai, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE NhaCungCap
            SET tenNhaCungCap = ?, diaChi = ?, soDienThoai = ?, email = ?
            WHERE id = (
                SELECT id FROM NhaCungCap WHERE email = (
                    SELECT email FROM NguoiDung WHERE id = ?
                )
            )
        ''', (ten_nha_cung_cap, dia_chi, so_dien_thoai, email, user_id))
        conn.commit()
        conn.close()
    @staticmethod
    def get_by_user_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM NhaCungCap WHERE idNguoiDung = ?
        ''', (user_id,))
        supplier = cursor.fetchone()
        conn.close()
        return supplier