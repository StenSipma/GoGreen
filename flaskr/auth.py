"""
File for login pages
"""
import functools
from flask import (
    Blueprint, render_template, request, redirect,
    url_for, flash, current_app, session, g
)

from flaskr.db import get_db
from flaskr.user import parse_user_request

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM Users WHERE id = ?', (user_id,)
        ).fetchone()


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        user = db.execute(
            'SELECT * FROM Users WHERE username = ?',
            (username,)
        ).fetchone()

        if user is None or not password == user['password']:
            error = "Incorrect Username and/or Password"

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('home.user_home'))
        # There is an error
        flash(error)
    # GET request
    return render_template("auth/login.html")


@bp.route('/logout')
@login_required
def logout():
    session.clear()
    return redirect(url_for('auth.login'))


@bp.route('/register', methods=('GET', 'POST'))
def register():
    current_app.logger.info(request.method)
    if request.method == 'POST':
        account, error = parse_user_request(request)
        db = get_db()
        if account is not None and db.execute(
                'SELECT id FROM Users WHERE username = ?', (account.username,)
        ).fetchone() is not None:
            error = 'Username: "{}" is already in use.'.format(
                account.username)

        if error is None:
            account.insert_in_db()
            return redirect(url_for('auth.login'))
        # There is an error
        current_app.logger.error(error)
        flash(error)
    # request == GET

    return render_template("auth/register.html")
