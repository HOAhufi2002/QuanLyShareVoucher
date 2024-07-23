# models/order.py

from db import get_db_connection

class Order:
    @staticmethod
    def create_order(idNguoiDung, idSanPham, diaChiGiaoHang, tongTien):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Orders (idNguoiDung, idSanPham, ngayDatHang, diaChiGiaoHang, tongTien)
            VALUES (?, ?, GETDATE(), ?, ?)
        ''', (idNguoiDung, idSanPham, diaChiGiaoHang, tongTien))
        conn.commit()
        conn.close()
    @staticmethod
    def get_orders_by_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT Orders.*, SanPham.tenSanPham, SanPham.gia 
            FROM Orders
            JOIN SanPham ON Orders.idSanPham = SanPham.id
            WHERE Orders.idNguoiDung = ?
        ''', (user_id,))
        orders = cursor.fetchall()
        conn.close()
        return orders