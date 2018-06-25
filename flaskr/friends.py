from flask import Blueprint, render_template, g, request, flash
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('friends', __name__, url_prefix='/friends')


@bp.route('/new')
@login_required
def add_friends():
    pass


@bp.route('', methods=['GET', 'POST'])
@login_required
def friends():
    db = get_db()
    if request.method == 'POST':
        error = None
        username = request.form['friend-username']

        friend = db.execute(
            "SELECT id FROM Users WHERE username = ?", (username,)
        ).fetchone()
        if friend is None:
            error = "Friend not found"
        elif friend['id'] == g.user['id']:
            error = "You cannot add yourself as a friend"
        elif db.execute(
                "SELECT * FROM Friends WHERE user_id = ? AND friend_id = ?",
                (g.user['id'], friend['id'])
        ).fetchone() is not None:
            error = "You are already friends with '"+username+"'"

        if error is None:
            db.execute(
                "INSERT INTO Friends (user_id, friend_id) VALUES (?, ?)",
                (g.user['id'], friend['id'])
            )
            db.commit()
        else:
            flash(error)

    # Proceed normally
    friends = db.execute(
        """
        SELECT id, name FROM Users
        WHERE id IN (SELECT friend_id FROM FRIENDS WHERE user_id = ?)""",
        (g.user['id'],))
    return render_template("friends/friends.html", friends=friends)
