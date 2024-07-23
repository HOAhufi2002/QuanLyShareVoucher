from db import get_db_connection

class Program:
    @staticmethod
    def nhacungcap_add_program(ten_chuong_trinh, mo_ta, ngay_bat_dau, ngay_ket_thuc, id_nha_cung_cap):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO ChuongTrinhGiamGia (tenChuongTrinh, moTa, ngayBatDau, ngayKetThuc, idNhaCungCap)
            VALUES (?, ?, ?, ?, ?)
        ''', (ten_chuong_trinh, mo_ta, ngay_bat_dau, ngay_ket_thuc, id_nha_cung_cap))
        conn.commit()
        conn.close()

    @staticmethod
    def nhacungcap_get_programs_by_supplier(id_nha_cung_cap):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM ChuongTrinhGiamGia
            WHERE idNhaCungCap = ? AND isDel = 0
        ''', (id_nha_cung_cap,))
        programs = cursor.fetchall()
        conn.close()
        return programs
