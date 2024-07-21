from flask import render_template, request, redirect, url_for, session, flash
from . import main_bp
from models.discount import Discount
from models.nguoidung import NguoiDung
from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from models.notification import Notification
@main_bp.route('/')
def home():
    discounts = Discount.get_all_discounts()
    return render_template('home.html', discounts=discounts)

@main_bp.route('/chuongtrinh/<int:id>')
def chuongtrinh_detail(id):
    discount = Discount.get_discount_by_id(id)
    if discount:
        return render_template('chuongtrinh_detail.html', discount=discount)
    else:
        return 'Chuong trinh not found', 404

@main_bp.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    user_id = session['user_id']
    user = User.get_by_id(user_id)

    if request.method == 'POST':
        ho_ten = request.form['ho_ten']
        email = request.form['email']
        User.update_user_info(user_id, ho_ten, email)
        flash('Thông tin cá nhân đã được cập nhật.')
        return redirect(url_for('main.profile'))

    return render_template('profile.html', user=user)

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
