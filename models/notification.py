from db import get_db_connection

class Notification:
    @staticmethod
    def add_notification(noi_dung, ngay_gui, trang_thai, id_nguoi_dung=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO ThongBao (idNguoiDung, noiDung, ngayGui, trangThai)
            VALUES (?, ?, ?, ?)
        ''', (id_nguoi_dung, noi_dung, ngay_gui, trang_thai))
        conn.commit()
        conn.close()

    @staticmethod
    def mark_as_read(notification_id, user_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE ThongBao
            SET idNguoiDung = ?, trangThai = 'daDoc'
            WHERE id = ?
        ''', (user_id, notification_id))
        conn.commit()
        conn.close()

    @staticmethod
    def get_notifications(user_id=None):
        conn = get_db_connection()
        cursor = conn.cursor()
        if user_id:
            cursor.execute('''
                SELECT * FROM ThongBao
                WHERE idNguoiDung = ? OR idNguoiDung IS NULL
            ''', (user_id,))
        else:
            cursor.execute('SELECT * FROM ThongBao')
        notifications = cursor.fetchall()
        conn.close()
        return notifications
