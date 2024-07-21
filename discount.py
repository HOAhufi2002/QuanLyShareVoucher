# discount.py

from flask import Blueprint, render_template

discount = Blueprint('discount', __name__)

@discount.route('/discount_list')
def discount_list():
    return render_template('discount_list.html')
