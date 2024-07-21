# routes/search.py
from flask import render_template, session, redirect, url_for, request
from . import search_bp
from models.search import SearchHistory

@search_bp.route('/search')
def search_list():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    history = SearchHistory.get_by_user_id(session['user_id'])
    return render_template('search_history.html', history=history)

@search_bp.route('/search/add', methods=['POST'])
def add_search():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    keyword = request.form['keyword']
    SearchHistory.add_search(session['user_id'], keyword)
    return redirect(url_for('search.search_list'))

@search_bp.route('/search/delete/<string:keyword>')
def delete_search(keyword):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    SearchHistory.delete_search(session['user_id'], keyword)
    return redirect(url_for('search.search_list'))
