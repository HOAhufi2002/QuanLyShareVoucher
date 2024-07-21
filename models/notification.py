from db import get_db_connection

class Notification:
    @staticmethod
    def add_notification(noi_dung, ngay_gui, trang_thai, id_nguoi_dung=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO ThongBao (noiDung, ngayGui)
            VALUES (?, ?)
        ''', (noi_dung, ngay_gui))
        conn.commit()
        conn.close()

    @staticmethod
    def mark_as_read(notification_id, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        # Kiểm tra xem bản ghi đã tồn tại trong ThongBao_NguoiDung chưa
        cursor.execute('''
            SELECT * FROM ThongBao_NguoiDung
            WHERE idThongBao = ? AND idNguoiDung = ?
        ''', (notification_id, user_id))
        record = cursor.fetchone()
        if record:
            # Nếu đã tồn tại, cập nhật trạng thái thành 'daDoc'
            cursor.execute('''
                UPDATE ThongBao_NguoiDung
                SET trangThai = 'daDoc'
                WHERE idThongBao = ? AND idNguoiDung = ?
            ''', (notification_id, user_id))
        else:
            # Nếu chưa tồn tại, thêm bản ghi mới vào ThongBao_NguoiDung
            cursor.execute('''
                INSERT INTO ThongBao_NguoiDung (idThongBao, idNguoiDung, trangThai)
                VALUES (?, ?, 'daDoc')
            ''', (notification_id, user_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_notifications(user_id=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        if user_id:
            cursor.execute('''
                SELECT tb.id, tb.noiDung, tb.ngayGui, ISNULL(tbnd.trangThai, 'chuaDoc') AS trangThai
                FROM ThongBao tb
                LEFT JOIN ThongBao_NguoiDung tbnd ON tb.id = tbnd.idThongBao AND tbnd.idNguoiDung = ?
            ''', (user_id,))
        else:
            cursor.execute('''
                SELECT tb.id, tb.noiDung, tb.ngayGui, 'chuaDoc' AS trangThai
                FROM ThongBao tb
            ''')
        notifications = cursor.fetchall()
        conn.close()
        return notifications
