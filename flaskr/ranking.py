"""
File for ranking pages
"""

from flask import Blueprint, render_template, g, request, flash
from flaskr.db import get_db
from flaskr.badge import get_badge_by_rank, randomize_other_badges
from flaskr.auth import login_required
from flaskr.groups import query_groups

bp = Blueprint('ranking', __name__, url_prefix='/ranking')


@bp.route('', methods=['GET', 'POST'])
@login_required
def rank_groups():
    db = get_db()
    user_id = g.user['id']
    error=None
    if request.method == 'POST':
        group_name = request.form.get('group-name')
        friend_ids = request.form.getlist('friends-select')
        existing_group = db.execute("SELECT * FROM Groups WHERE group_name = ? AND user_id = ?", (group_name, user_id)).fetchone()
        if existing_group is None:
            group_id = db.execute(
                """INSERT INTO Groups(user_id, group_name) VALUES (?, ?)""",
            (user_id, group_name)).lastrowid
            print(group_id)
            for friend_id in friend_ids:
                db.execute("""INSERT INTO GroupMembers (group_id, user_id) VALUES (?, ?)""",(group_id, friend_id))
            db.commit()
        else:
            error = "You already have a group with that name"
        if error is not None:
            flash(error)
    groups = query_groups(user_id)
    badges = [randomize_other_badges(len(g.members)+1) for g in groups]

    friends = db.execute(
        """SELECT id, name FROM Users
        WHERE id IN (SELECT friend_id
                     FROM Friends
                     WHERE user_id = ?)""",
        (user_id,)
    ).fetchall()
    return render_template("ranking/ranking_groups.html",
                           friends=friends,
                           groups=list(zip(groups, badges)),
                           str=str,
                           get_badge_by_rank=get_badge_by_rank)
