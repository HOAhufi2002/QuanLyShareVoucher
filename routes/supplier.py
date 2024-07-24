from flask import render_template, request, redirect, url_for, session,flash
from . import supplier_bp
from models.supplier import Supplier
from models.product import Product
from models.discount import Discount
from decimal import Decimal  # Thêm dòng này
from models.program import Program

@supplier_bp.route('/suppliers', methods=['GET'])
def supplier_list():
    suppliers = Supplier.get_all_suppliers()
    return render_template('supplier_list.html', suppliers=suppliers)

@supplier_bp.route('/suppliers/<int:supplier_id>')
def supplier_detail(supplier_id):
    supplier, products, discounts = Supplier.get_supplier_by_id(supplier_id)
    if not supplier:
        flash('Nhà cung cấp không tồn tại.')
        return redirect(url_for('supplier.supplier_list'))
    discounted_prices = session.get('discounted_prices', {})
    return render_template('supplier_detail.html', supplier=supplier, products=products, discounts=discounts, discounted_prices=discounted_prices)

@supplier_bp.route('/apply_discount/<int:product_id>', methods=['POST'])
def apply_discount(product_id):
    discount_code = request.form['discount_code']
    product = Product.get_product_by_id(product_id)
    if not product:
        flash('Sản phẩm không tồn tại.')
        return redirect(request.referrer)

    discount = Discount.get_discount_by_code(discount_code)
    if not discount:
        flash('Mã giảm giá không hợp lệ.')
        return redirect(request.referrer)

    if discount.idnhacungcap != product.idnhacungcap:
        flash('Mã giảm giá không thuộc nhà cung cấp của sản phẩm này.')
        return redirect(request.referrer)

    # Chuyển đổi giá trị giảm giá thành Decimal
    discount_percentage = Decimal(discount.phanTramGiamGia) / Decimal(100)
    discounted_price = float(product.gia * (1 - discount_percentage))

    # Lưu giá trị giá đã giảm vào session
    discounted_prices = session.get('discounted_prices', {})
    discounted_prices[str(product_id)] = discounted_price  # Chuyển đổi product_id thành chuỗi
    session['discounted_prices'] = discounted_prices

    return redirect(url_for('supplier.supplier_detail', supplier_id=product.idnhacungcap))

@supplier_bp.route('/remove_discount/<int:product_id>', methods=['POST'])
def remove_discount(product_id):
    discounted_prices = session.get('discounted_prices', {})
    if str(product_id) in discounted_prices:
        del discounted_prices[str(product_id)]
    session['discounted_prices'] = discounted_prices

    product = Product.get_product_by_id(product_id)
    return redirect(url_for('supplier.supplier_detail', supplier_id=product.idnhacungcap))
@supplier_bp.route('/nhacungcap_manage_discounts', methods=['GET', 'POST'])
def nhacungcap_manage_discounts():
    if 'user_id' not in session or session['user_role'] != 'nhacungcap':
        return redirect(url_for('auth.login'))
    
    id_nha_cung_cap = session['user_id']
    
    if request.method == 'POST':
        ma = request.form['ma']
        phan_tram_giam_gia = request.form['phan_tram_giam_gia']
        ngay_het_han = request.form['ngay_het_han']
        id_chuong_trinh_giam_gia = request.form['id_chuong_trinh_giam_gia']
        Discount.nhacungcap_add_discount(ma, phan_tram_giam_gia, ngay_het_han, id_chuong_trinh_giam_gia)
        return redirect(url_for('supplier.nhacungcap_manage_discounts'))

    discounts = Discount.nhacungcap_get_discounts_by_supplier(id_nha_cung_cap)
    programs = Program.nhacungcap_get_programs_by_supplier(id_nha_cung_cap)
    
    return render_template('supplier/nhacungcap_manage_discounts.html', discounts=discounts, programs=programs)


@supplier_bp.route('/nhacungcap_manage_products', methods=['GET', 'POST'])
def nhacungcap_manage_products():
    if 'user_id' not in session or session['user_role'] != 'nhacungcap':
        return redirect(url_for('auth.login'))

    id_nha_cung_cap = session['user_id']

    if request.method == 'POST':
        ten_san_pham = request.form['ten_san_pham']
        gia = request.form['gia']
        Product.nhacungcap_add_product(ten_san_pham, gia, id_nha_cung_cap)
        return redirect(url_for('supplier.nhacungcap_manage_products'))

    products = Product.nhacungcap_get_products_by_supplier(id_nha_cung_cap)
    return render_template('supplier/nhacungcap_manage_products.html', products=products)
@supplier_bp.route('/update_supplier_info', methods=['POST'])
def update_supplier_info():
    if 'user_id' not in session or session.get('user_role') != 'nhacungcap':
        return redirect(url_for('auth.login'))
    
    user_id = session['user_id']
    ten_nha_cung_cap = request.form['ten_nha_cung_cap']
    dia_chi_ncc = request.form['dia_chi_ncc']
    so_dien_thoai_ncc = request.form['so_dien_thoai_ncc']
    email_ncc = request.form['email_ncc']
    
    Supplier.update_supplier_info(user_id, ten_nha_cung_cap, dia_chi_ncc, so_dien_thoai_ncc, email_ncc)
    return redirect(url_for('main.profile'))