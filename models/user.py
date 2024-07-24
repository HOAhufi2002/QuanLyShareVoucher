from db import get_db_connection
import hashlib

class User:
    @staticmethod
    def get_by_id(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, hoTen, email, matkhau, ngaySinh, diaChi, soDienThoai, quyen
            FROM NguoiDung
            WHERE id = ?
        ''', (user_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            columns = [column[0] for column in cursor.description]
            return dict(zip(columns, row))
        return None

    @staticmethod
    def update_user_info(user_id, ho_ten, email, ngay_sinh, dia_chi, so_dien_thoai, quyen):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE NguoiDung
            SET hoTen = ?, email = ?, ngaySinh = ?, diaChi = ?, soDienThoai = ?, quyen = ?
            WHERE id = ?
        ''', (ho_ten, email, ngay_sinh, dia_chi, so_dien_thoai, quyen, user_id))
        conn.commit()
        conn.close()
    @staticmethod
    def update_user(user_id, ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, mat_khau, quyen):
        conn = get_db_connection()
        cursor = conn.cursor()
        hashed_password = hashlib.sha256(mat_khau.encode()).hexdigest() if mat_khau else None

        if hashed_password:
            cursor.execute('''
                UPDATE NguoiDung
                SET hoTen = ?, ngaySinh = ?, diaChi = ?, soDienThoai = ?, email = ?, matKhau = ?, quyen = ?
                WHERE id = ?
            ''', (ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, hashed_password, quyen, user_id))
        else:
            cursor.execute('''
                UPDATE NguoiDung
                SET hoTen = ?, ngaySinh = ?, diaChi = ?, soDienThoai = ?, email = ?, quyen = ?
                WHERE id = ?
            ''', (ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, quyen, user_id))

        conn.commit()
        conn.close()

    @staticmethod
    def get_all_users():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, hoTen, ngaySinh, diaChi, soDienThoai, email, quyen FROM NguoiDung where isDel = 0')
        rows = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        users = [dict(zip(columns, row)) for row in rows]
        conn.close()
        return users
    @staticmethod
    def update_isdel(user_id, isdel):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE NguoiDung
            SET isDel = ?
            WHERE id = ?
        ''', (isdel, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def delete_user(user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM NguoiDung WHERE id = ?', (user_id,))
        conn.commit()
        conn.close()
    @staticmethod
    def get_by_email(email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM NguoiDung WHERE email = ?', (email,))
        row = cursor.fetchone()
        conn.close()
        if row:
            columns = [column[0] for column in cursor.description]
            return dict(zip(columns, row))
        return None

    @staticmethod
    def update_password(user_id, hashed_password):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE NguoiDung
            SET matkhau = ?
            WHERE id = ?
        ''', (hashed_password, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def add_user(ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, mat_khau, quyen):
        conn = get_db_connection()
        cursor = conn.cursor()
        hashed_password = hashlib.sha256(mat_khau.encode()).hexdigest()
        cursor.execute('''
            INSERT INTO NguoiDung (hoTen, ngaySinh, diaChi, soDienThoai, email, matKhau, quyen)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, hashed_password, quyen))
        conn.commit()
        conn.close()

    @staticmethod
    def get_user_by_email(email):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM NguoiDung WHERE email = ?
        ''', (email,))
        user = cursor.fetchone()
        conn.close()
        return user
 
    @staticmethod
    def insert_user(ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, mat_khau, quyen, is_del):
        query = """
        INSERT INTO NguoiDung (hoTen, ngaySinh, diaChi, soDienThoai, email, matKhau, quyen, isDel)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute(query, (ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, mat_khau, quyen, is_del))
            conn.commit()
            user_id = cursor.execute("SELECT @@IDENTITY AS id").fetchone()[0]
            conn.close()
            return user_id
        except Exception as e:
            print(f"Error inserting user: {e}")
            return None

    @staticmethod
    def get_by_email_and_password(email, password):
        user = User.get_by_email(email)
        if user:
            hashed_password = hashlib.sha256(password.encode()).hexdigest()
            if user['matKhau'] == hashed_password:
                return user
        return None
