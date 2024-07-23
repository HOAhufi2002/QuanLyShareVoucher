from flask import render_template, request, redirect, url_for, session, flash
from . import admin_bp
from models.discount import Discount
from models.supplier import Supplier
from models.voucher import Voucher
from models.notification import Notification
from datetime import date  # Thêm dòng này để nhập khẩu mô-đun date
from models.user import User
from models.product import Product

@admin_bp.route('/users/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        ho_ten = request.form['hoTen']
        ngay_sinh = request.form['ngaySinh']
        dia_chi = request.form['diaChi']
        so_dien_thoai = request.form['soDienThoai']
        email = request.form['email']
        mat_khau = request.form['matKhau']
        quyen = request.form['quyen']
        User.add_user(ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, mat_khau, quyen)
        return redirect(url_for('admin.manage_users'))
    return render_template('admin/add_user.html')

# Route quản lý chương trình giảm giá
@admin_bp.route('/manage_discounts', methods=['GET', 'POST'])
def manage_discounts():
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        ten_chuong_trinh = request.form['ten_chuong_trinh']
        mo_ta = request.form['mo_ta']
        ngay_bat_dau = request.form['ngay_bat_dau']
        ngay_ket_thuc = request.form['ngay_ket_thuc']
        nha_cung_cap_id = request.form['nha_cung_cap']
        Discount.add_discount(ten_chuong_trinh, mo_ta, ngay_bat_dau, ngay_ket_thuc, nha_cung_cap_id)
        flash('Chương trình giảm giá đã được thêm.')

    discounts = Discount.get_all_discounts_with_suppliers()
    suppliers = Supplier.get_all_suppliers()
    return render_template('admin/manage_discounts.html', discounts=discounts, suppliers=suppliers)
@admin_bp.route('/manage_users', methods=['GET'])
def manage_users():
    users = User.get_all_users()
    return render_template('admin/manage_users.html', users=users)
# Route để sửa tài khoản
@admin_bp.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = User.get_by_id(user_id)

    if request.method == 'POST':
        ho_ten = request.form['hoTen']
        ngay_sinh = request.form['ngaySinh']
        dia_chi = request.form['diaChi']
        so_dien_thoai = request.form['soDienThoai']
        email = request.form['email']
        mat_khau = request.form['matKhau']
        quyen = request.form['quyen']
        User.update_user(user_id, ho_ten, ngay_sinh, dia_chi, so_dien_thoai, email, mat_khau, quyen)
        return redirect(url_for('admin.manage_users'))

    return render_template('admin/edit_user.html', user=user)

@admin_bp.route('/users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    User.update_isdel(user_id, True)
    return redirect(url_for('admin.manage_users'))

# Route chỉnh sửa chương trình giảm giá
@admin_bp.route('/edit_discount/<int:discount_id>', methods=['GET', 'POST'])
def edit_discount(discount_id):
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('auth.login'))

    discount = Discount.get_discount_by_id(discount_id)
    suppliers = Supplier.get_all_suppliers()

    if request.method == 'POST':
        ten_chuong_trinh = request.form['ten_chuong_trinh']
        mo_ta = request.form['mo_ta']
        ngay_bat_dau = request.form['ngay_bat_dau']
        ngay_ket_thuc = request.form['ngay_ket_thuc']
        nha_cung_cap_id = request.form['nha_cung_cap']
        Discount.update_discount(discount_id, ten_chuong_trinh, mo_ta, ngay_bat_dau, ngay_ket_thuc, nha_cung_cap_id)
        flash('Chương trình giảm giá đã được cập nhật.')
        return redirect(url_for('admin.manage_discounts'))

    return render_template('admin/edit_discount.html', discount=discount, suppliers=suppliers)

# Route xóa chương trình giảm giá
@admin_bp.route('/delete_discount/<int:discount_id>', methods=['POST'])
def delete_discount(discount_id):
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('auth.login'))

    Discount.delete_discount(discount_id)
    flash('Chương trình giảm giá đã được xóa.')
    return redirect(url_for('admin.manage_discounts'))

@admin_bp.route('/manage_vouchers', methods=['GET', 'POST'])
def manage_vouchers():
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        ma = request.form['ma']
        phan_tram_giam_gia = request.form['phan_tram_giam_gia']
        ngay_het_han = request.form['ngay_het_han']
        chuong_trinh_giam_gia_id = request.form['chuong_trinh_giam_gia']
        Voucher.add_voucher(ma, phan_tram_giam_gia, ngay_het_han, chuong_trinh_giam_gia_id)
        flash('Mã giảm giá đã được thêm.')

        # Thêm thông báo
        discount = Discount.get_discount_by_id(chuong_trinh_giam_gia_id)
        noi_dung = f"{discount[1]} - Mã giảm giá: {ma} - Giảm giá: {phan_tram_giam_gia}%"

        Notification.add_notification(noi_dung, date.today(), 'chuaDoc')

    vouchers = Voucher.get_all_vouchers_with_programs()
    programs = Discount.get_all_discounts_for_voucher()
    return render_template('admin/manage_vouchers.html', vouchers=vouchers, programs=programs)


# Route chỉnh sửa mã giảm giá
@admin_bp.route('/edit_voucher/<int:voucher_id>', methods=['GET', 'POST'])
def edit_voucher(voucher_id):
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('auth.login'))

    voucher = Voucher.get_voucher_by_id(voucher_id)
    programs = Discount.get_all_discounts()

    if request.method == 'POST':
        ma = request.form['ma']
        phan_tram_giam_gia = request.form['phan_tram_giam_gia']
        ngay_het_han = request.form['ngay_het_han']
        chuong_trinh_giam_gia_id = request.form['chuong_trinh_giam_gia']
        Voucher.update_voucher(voucher_id, ma, phan_tram_giam_gia, ngay_het_han, chuong_trinh_giam_gia_id)
        flash('Mã giảm giá đã được cập nhật.')
        return redirect(url_for('admin.manage_vouchers'))

    return render_template('admin/edit_voucher.html', voucher=voucher, programs=programs)

# Route xóa mã giảm giá
@admin_bp.route('/delete_voucher/<int:voucher_id>', methods=['POST'])
def delete_voucher(voucher_id):
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('auth.login'))

    Voucher.delete_voucher(voucher_id)
    flash('Mã giảm giá đã được xóa.')
    return redirect(url_for('admin.manage_vouchers'))
@admin_bp.route('/manage_suppliers', methods=['GET', 'POST'])
def manage_suppliers():
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        ten_nha_cung_cap = request.form['ten_nha_cung_cap']
        dia_chi = request.form['dia_chi']
        so_dien_thoai = request.form['so_dien_thoai']
        email = request.form['email']
        Supplier.add_supplier(ten_nha_cung_cap, dia_chi, so_dien_thoai, email)
        flash('Nhà cung cấp đã được thêm.')

    suppliers = Supplier.get_all_suppliers()
    return render_template('admin/manage_suppliers.html', suppliers=suppliers)

@admin_bp.route('/edit_supplier/<int:supplier_id>', methods=['GET', 'POST'])
def edit_supplier(supplier_id):
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('auth.login'))

    supplier = Supplier.get_supplier_by_id(supplier_id)

    if request.method == 'POST':
        ten_nha_cung_cap = request.form['ten_nha_cung_cap']
        dia_chi = request.form['dia_chi']
        so_dien_thoai = request.form['so_dien_thoai']
        email = request.form['email']
        Supplier.update_supplier(supplier_id, ten_nha_cung_cap, dia_chi, so_dien_thoai, email)
        flash('Nhà cung cấp đã được cập nhật.')
        return redirect(url_for('admin.manage_suppliers'))

    return render_template('admin/edit_supplier.html', supplier=supplier)

@admin_bp.route('/delete_supplier/<int:supplier_id>', methods=['POST'])
def delete_supplier(supplier_id):
    if 'user_id' not in session or session['user_role'] != 'admin':
        return redirect(url_for('auth.login'))

    Supplier.delete_supplier(supplier_id)
    flash('Nhà cung cấp đã được xóa.')
    return redirect(url_for('admin.manage_suppliers'))

@admin_bp.route('/manage_products')
def manage_products():
    if session.get('user_role') != 'admin':
        flash('Bạn không có quyền truy cập vào trang này.')
        return redirect(url_for('main.home'))

    products = Product.get_all()
    return render_template('admin/manage_products.html', products=products)

@admin_bp.route('/manage_products/add', methods=['GET', 'POST'])
def add_product():
    if session.get('user_role') != 'admin':
        flash('Bạn không có quyền truy cập vào trang này.')
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        tensanpham = request.form['tensanpham']
        gia = request.form['gia']
        idNhaCungCap = request.form['idNhaCungCap']

        Product.add_product(tensanpham, gia, idNhaCungCap)
        flash('Sản phẩm đã được thêm thành công.')
        return redirect(url_for('admin.manage_products'))

    suppliers = Supplier.get_all_suppliers()
    return render_template('admin/add_product.html', suppliers=suppliers)