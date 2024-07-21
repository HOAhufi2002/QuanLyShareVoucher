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
        cursor.execute('''
            SELECT id, tenNhaCungCap, diaChi, soDienThoai, email FROM NhaCungCap WHERE id = ? AND isDel = 0
        ''', (supplier_id,))
        supplier = cursor.fetchone()
        conn.close()
        return supplier

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