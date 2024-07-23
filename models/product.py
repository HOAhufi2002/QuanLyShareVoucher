from db import get_db_connection

class Product:
    @staticmethod
    def get_all():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT sp.id, sp.tensanpham, sp.gia, ncc.tenNhaCungCap, mg.ma
            FROM SanPham sp
            LEFT JOIN NhaCungCap ncc ON sp.idNhaCungCap = ncc.id
            LEFT JOIN MaGiamGia mg ON sp.idMaGiamGia = mg.id
            WHERE sp.isDel = 0
        ''')
        products = cursor.fetchall()
        conn.close()
        return products

    @staticmethod
    def add_product(tensanpham, gia, idNhaCungCap):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO SanPham (tensanpham, gia, idNhaCungCap)
            VALUES (?, ?, ?)
        ''', (tensanpham, gia, idNhaCungCap))
        conn.commit()
        conn.close()
    @staticmethod
    def get_product_by_id(product_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
   SELECT p.id, p.tensanpham, p.gia, p.idnhacungcap, p.idmagiamgia, p.isdel, ncc.tenNhaCungCap
            FROM SanPham p
            JOIN NhaCungCap ncc ON p.idnhacungcap = ncc.id
            WHERE p.id = ?
        ''', (product_id,))
        product = cursor.fetchone()
        conn.close()
        return product
    @staticmethod
    def get_product_by_id1(product_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT p.id, p.tensanpham, p.gia, p.idnhacungcap, p.idmagiamgia, p.isdel, ncc.tenNhaCungCap
            FROM SanPham p
            JOIN NhaCungCap ncc ON p.idnhacungcap = ncc.id
            WHERE p.id = ?
        ''', (product_id,))
        product = cursor.fetchone()
        conn.close()
        return product
    @staticmethod
    def nhacungcap_add_product(ten_san_pham, gia, id_nha_cung_cap):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO SanPham (tenSanPham, gia, idNhaCungCap)
            VALUES (?, ?, ?)
        ''', (ten_san_pham, gia, id_nha_cung_cap))
        conn.commit()
        conn.close()
    @staticmethod
    def get_by_id(product_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM SanPham WHERE id = ? AND isDel = 0
        ''', (product_id,))
        product = cursor.fetchone()
        conn.close()
        if product:
            return {
                'id': product[0],
                'tenSanPham': product[1],
                'gia': product[2],
                'idNhaCungCap': product[3],
                'idMaGiamGia': product[4],
                'isDel': product[5]
            }
        return None
    @staticmethod
    def nhacungcap_get_products_by_supplier(id_nha_cung_cap):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM SanPham
            WHERE idNhaCungCap = ? AND isDel = 0
        ''', (id_nha_cung_cap,))
        products = cursor.fetchall()
        conn.close()
        return products