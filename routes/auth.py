# routes/auth.py
from flask import render_template, request, redirect, url_for, session, flash
from . import auth_bp
from models.nguoidung import NguoiDung

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = NguoiDung.get_by_email_and_password(email, password)
        if user:
            session['user_id'] = user.id
            session['user_name'] = user.hoTen  # Thêm dòng này để lưu tên vào session
            session['user_role'] = user.quyen
            return redirect(url_for('main.home'))
        else:
            flash('Invalid credentials')
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('main.home'))
