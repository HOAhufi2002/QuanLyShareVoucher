# routes/auth.py
from flask import render_template, request, redirect, url_for, session, flash
from . import auth_bp
from models.nguoidung import NguoiDung
from models.user import User
import bcrypt

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.get_by_email_and_password(email, password)
        if user:
            session['user_id'] = user['id']
            session['user_name'] = user['hoTen']
            session['user_role'] = user['quyen']
            return redirect(url_for('main.home'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        ho_ten = request.form['ho_ten']
        ngay_sinh = request.form['ngay_sinh']
        dia_chi = request.form['dia_chi']
        so_dien_thoai = request.form['so_dien_thoai']
        email = request.form['email']
        mat_khau = request.form['mat_khau']
        confirm_mat_khau = request.form['confirm_mat_khau']
        quyen = 'khachhang'

        if mat_khau != confirm_mat_khau:
            flash('Mật khẩu không khớp')
            return redirect(url_for('auth.register'))

        existing_user = User.get_user_by_email(email)
        if existing_user:
            flash('Email đã được đăng ký')
            return redirect(url_for('auth.register'))

        User.add_user(ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, mat_khau, quyen)
        flash('Đăng ký thành công. Vui lòng đăng nhập.')
        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')