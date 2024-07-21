from flask import render_template, request, redirect, url_for, session
from . import supplier_bp
from models.supplier import Supplier

@supplier_bp.route('/suppliers', methods=['GET'])
def supplier_list():
    suppliers = Supplier.get_all_suppliers()
    return render_template('supplier_list.html', suppliers=suppliers)

@supplier_bp.route('/supplier/<int:supplier_id>', methods=['GET'])
def supplier_detail(supplier_id):
    supplier = Supplier.get_supplier_by_id(supplier_id)
    if not supplier:
        return 'Nhà cung cấp không tồn tại', 404
    discounts = Supplier.get_discounts_by_supplier_id(supplier_id)
    return render_template('supplier_detail.html', supplier=supplier, discounts=discounts)
