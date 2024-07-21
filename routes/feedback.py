from flask import render_template, request, redirect, url_for, session
from . import feedback_bp
from models.feedback import Feedback
from models.rating import Rating
from models.discount import Discount

@feedback_bp.route('/feedback/<int:discount_id>', methods=['GET', 'POST'])
def feedback_list(discount_id):
    if request.method == 'POST':
        if 'user_id' not in session:
            return redirect(url_for('auth.login'))
        content = request.form['content']
        rating = request.form['rating']
        user_id = session['user_id']
        Feedback.add_feedback(user_id, discount_id, content)
        Rating.add_rating(user_id, discount_id, rating)
        return redirect(url_for('feedback.feedback_list', discount_id=discount_id))

    discount = Discount.get_discount_by_id(discount_id)
    feedbacks = Feedback.get_feedback_by_discount_id(discount_id)
    ratings = Rating.get_ratings_by_discount_id(discount_id)
    return render_template('feedback_list.html', discount=discount, feedbacks=feedbacks, ratings=ratings)
