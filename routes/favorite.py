# routes/favorite.py
from flask import render_template, session, redirect, url_for, request
from . import favorite_bp
from models.favorite import Favorite

@favorite_bp.route('/favorite')
def favorite_list():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    favorites = Favorite.get_by_user_id(session['user_id'])
    return render_template('favorite_list.html', favorites=favorites)

@favorite_bp.route('/favorite/add/<int:chuongtrinh_id>', methods=['POST'])
def add_favorite(chuongtrinh_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    Favorite.add_favorite(session['user_id'], chuongtrinh_id)
    return redirect(url_for('favorite.favorite_list'))

@favorite_bp.route('/favorite/remove/<int:chuongtrinh_id>', methods=['POST'])
def remove_favorite(chuongtrinh_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    Favorite.remove_favorite(session['user_id'], chuongtrinh_id)
    return redirect(url_for('favorite.favorite_list'))
