# In routes/order.py

from flask import Blueprint, request, redirect, url_for, flash, session,render_template
from models.order import Order
from models.product import Product

order_bp = Blueprint('order', __name__)


@order_bp.route('/create_order/<int:product_id>', methods=['POST'])
def create_order(product_id):
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    
    dia_chi_giao_hang = request.form['dia_chi_giao_hang']
    so_dien_thoai = request.form['so_dien_thoai']
    tong_tien = request.form['tong_tien']
    
    product = Product.get_by_id(product_id)
    if not product:
        flash('Sản phẩm không tồn tại')
        return redirect(url_for('main.home'))
    
    Order.create_order(user_id, product_id, dia_chi_giao_hang, tong_tien)
    
    flash('Đặt hàng thành công')
    return redirect(url_for('main.home'))
@order_bp.route('/orders', methods=['GET'])
def view_orders():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('auth.login'))
    
    orders = Order.get_orders_by_user(user_id)
    return render_template('view_orders.html', orders=orders)