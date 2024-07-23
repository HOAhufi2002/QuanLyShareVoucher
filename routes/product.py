from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from db import get_db_connection
from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from models.product import Product
from models.supplier import Supplier  # Import thêm Supplier

product_bp = Blueprint('product', __name__)

@product_bp.route('/products')
def product_list():
    products = Product.get_all()
    return render_template('product_list.html', products=products)

@product_bp.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if session.get('user_role') != 'nhacungcap':
        flash('Bạn không có quyền truy cập vào trang này.')
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        tensanpham = request.form['tensanpham']
        gia = request.form['gia']
        idNhaCungCap = session.get('user_id')

        Product.add_product(tensanpham, gia, idNhaCungCap)
        flash('Sản phẩm đã được thêm thành công.')
        return redirect(url_for('product.product_list'))

    suppliers = Supplier.get_all_suppliers()
    return render_template('add_product.html', suppliers=suppliers)

@product_bp.route('/vouchers/add', methods=['GET', 'POST'])
def add_voucher():
    if session.get('user_role') != 'nhacungcap':
        flash('Bạn không có quyền truy cập vào trang này.')
        return redirect(url_for('main.home'))

    if request.method == 'POST':
        ma = request.form['ma']
        phan_tram_giam_gia = request.form['phan_tram_giam_gia']
        ngay_het_han = request.form['ngay_het_han']
        idChuongTrinhGiamGia = request.form['idChuongTrinhGiamGia']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO MaGiamGia (ma, phanTramGiamGia, ngayHetHan, idChuongTrinhGiamGia)
            VALUES (?, ?, ?, ?)
        ''', (ma, phan_tram_giam_gia, ngay_het_han, idChuongTrinhGiamGia))
        conn.commit()
        conn.close()

        flash('Mã giảm giá đã được thêm thành công.')
        return redirect(url_for('product.product_list'))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT id, tenChuongTrinh FROM ChuongTrinhGiamGia WHERE idNhaCungCap = ?', (session.get('user_id'),))
    discounts = cursor.fetchall()
    conn.close()

    return render_template('add_voucher.html', discounts=discounts)
