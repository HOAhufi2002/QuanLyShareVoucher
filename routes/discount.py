from flask import render_template, request, redirect, url_for, session
from . import discount_bp
from models.discount import Discount
from models.feedback import Feedback
from models.rating import Rating

@discount_bp.route('/discount/<int:discount_id>', methods=['GET', 'POST'])
def discount_detail(discount_id):
    if request.method == 'POST':
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        content = request.form['content']
        rating = request.form['rating']
        user_id = session['user_id']
        Feedback.add_feedback(user_id, discount_id, content)
        Rating.add_rating(user_id, discount_id, rating)
        return redirect(url_for('discount.discount_detail', discount_id=discount_id))

    discount = Discount.get_discount_by_id(discount_id)
    feedbacks = Feedback.get_feedback_by_discount_id(discount_id)
    ratings = Rating.get_ratings_by_discount_id(discount_id)
    return render_template('chuongtrinh_detail.html', discount=discount, feedbacks=feedbacks, ratings=ratings)
@discount_bp.route('/discounts', methods=['GET'])
def discount_list():
    search = request.args.get('search')
    expiry_date = request.args.get('expiry_date')
    discount_percent = request.args.get('discount_percent')

    discounts = Discount.search_discounts(search, expiry_date, discount_percent)
    return render_template('discount_list.html', discounts=discounts)