from flask import render_template, request, redirect, url_for, session, flash
from . import main_bp
from models.discount import Discount
from models.nguoidung import NguoiDung
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from models.notification import Notification
from models.feedback import Feedback  # Giả sử bạn có model Feedback để lấy dữ liệu phản hồi
from models.rating import Rating      # Giả sử bạn có model Rating để lấy dữ liệu đánh giá
from models.supplier import Supplier
import json
@main_bp.route('/')
def home():
    if 'user_id' in session:
        user_id = session['user_id']
        notifications = Notification.get_notifications(user_id)
        notification_count = len([n for n in notifications if n[3] == 'chuaDoc'])
    else:
        notification_count = 0

    user_role = session.get('user_role')
    feedback_data = None
    rating_data = None
    chuongtrinh = []
    
    if user_role == 'admin':
        feedback_data = json.dumps(Feedback.get_top_feedback_vouchers())
        rating_data = json.dumps(Rating.get_top_rated_vouchers())
    else:
        discounts = Discount.get_all_discounts()
        chuongtrinh = get_chuongtrinh()
    
    return render_template('home.html', user_role=user_role, feedback_data=feedback_data, rating_data=rating_data, chuongtrinh=chuongtrinh, notification_count=notification_count)
def get_chuongtrinh():
    # Định nghĩa hàm này để lấy dữ liệu của chương trình
    return [
        {'id': 1, 'tenChuongTrinh': 'Chương trình 1'},
        {'id': 2, 'tenChuongTrinh': 'Chương trình 2'}
    ]

@main_bp.route('/chuongtrinh/<int:id>')
def chuongtrinh_detail(id):
    discount = Discount.get_discount_by_id(id)
    if discount:
        return render_template('chuongtrinh_detail.html', discount=discount)
    else:
        return 'Chuong trinh not found', 404

@main_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))

    user = User.get_by_id(user_id)
    supplier = None
    if user['quyen'] == 'nhacungcap':
        supplier = Supplier.get_by_user_id(user_id)

    if request.method == 'POST':
        hoTen = request.form['hoTen']
        email = request.form['email']
        ngaySinh = request.form['ngaySinh']
        diaChi = request.form['diaChi']
        soDienThoai = request.form['soDienThoai']
        quyen = user['quyen']  # Không cho phép người dùng thay đổi quyền

        User.update_user_info(user_id, hoTen, email, ngaySinh, diaChi, soDienThoai, quyen)
        
        if supplier:
            tenNhaCungCap = request.form['tenNhaCungCap']
            diaChiNCC = request.form['diaChi']
            soDienThoaiNCC = request.form['soDienThoai']
            emailNCC = request.form['email']
            Supplier.update_supplier_info(supplier['id'], tenNhaCungCap, diaChiNCC, soDienThoaiNCC, emailNCC)
        
        flash('Cập nhật thông tin thành công')
        return redirect(url_for('main.profile'))

    return render_template('profile.html', user=user, supplier=supplier)






@main_bp.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        current_password = request.form['current_password']
        new_password = request.form['new_password']
        confirm_password = request.form['confirm_password']

        user_id = session['user_id']
        user = User.get_by_id(user_id)

        if not check_password_hash(user['matkhau'], current_password):
            flash('Mật khẩu hiện tại không đúng.')
        elif new_password != confirm_password:
            flash('Mật khẩu mới và xác nhận mật khẩu không khớp.')
        else:
            hashed_password = generate_password_hash(new_password)
            User.update_password(user_id, hashed_password)
            flash('Mật khẩu đã được thay đổi thành công.')
            return redirect(url_for('main.profile'))

    return render_template('change_password.html')

@main_bp.route('/contact')
def contact():
    return render_template('contact.html')
