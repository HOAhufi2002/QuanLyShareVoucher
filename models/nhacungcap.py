# models/nhacungcap.py
from db import get_db_connection

class NhaCungCap:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM NhaCungCap WHERE isDel=0')
        nhacungcap = cursor.fetchall()
        conn.close()
        return nhacungcap

    @staticmethod
    def insert_supplier(ten_nha_cung_cap, dia_chi, so_dien_thoai, email, is_del, id_nguoi_dung):
        if id_nguoi_dung is None:
            raise ValueError("idNguoiDung cannot be null")
        query = """
        INSERT INTO NhaCungCap (tenNhaCungCap, diaChi, soDienThoai, email, isDel, idNguoiDung)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(query, (ten_nha_cung_cap, dia_chi, so_dien_thoai, email, is_del, id_nguoi_dung))
        conn.commit()
        conn.close()

    @staticmethod
    def get_supplier_by_id(supplier_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM NhaCungCap WHERE id = ?", supplier_id)
        supplier = cursor.fetchone()
        conn.close()
        return supplier

    @staticmethod
    def update_supplier(supplier_id, tenNhaCungCap, diaChi, soDienThoai, email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE NhaCungCap SET tenNhaCungCap = ?, diaChi = ?, soDienThoai = ?, email = ?
            WHERE id = ?
        """, tenNhaCungCap, diaChi, soDienThoai, email, supplier_id)
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_suppliers():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM NhaCungCap WHERE isDel = 0")
        suppliers = cursor.fetchall()
        conn.close()
        return suppliers

    @staticmethod
    def delete_supplier(supplier_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE NhaCungCap SET isDel = 1 WHERE id = ?", supplier_id)
        conn.commit()
        conn.close()