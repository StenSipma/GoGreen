from flask import (
    Blueprint, render_template, redirect, url_for, g
)
from flaskr.auth import login_required

bp = Blueprint('home', __name__, url_prefix='/home')

OLD_COLORS = {
    "green": (0, 255, 14),
    "green-yellow": (186, 232, 9),
    "yellow": (255, 207, 0),
    "yellow-red": (232, 132, 9),
    "red": (255, 49, 0)
}

HEX_COLORS = {
    0: ['#FF1700', '#E8750C'],
    20: ['#E8750C', '#FFC700'],
    40: ['#FFC700', '#C4E80C'],
    60: ['#C4E80C', '#0DFF1F'],
    80: ['#0DFF1F', '#0DFF1F']
}


def pick_color(value):
    if value > 80:
        return HEX_COLORS[80]
    if value > 60:
        return HEX_COLORS[60]
    if value > 40:
        return HEX_COLORS[40]
    if value > 20:
        return HEX_COLORS[20]
    return HEX_COLORS[0]


@bp.route('')
def home():
    if g.user:  # if there is a user logged in
        return redirect(url_for('home.user_home'))
    return redirect(url_for('home.std_home'))


@bp.route('/general')
def std_home():
    return render_template('home.html', is_homepage=True)


@bp.route('/user')
@login_required
def user_home():
    score = g.user['score']
    color = pick_color(score)
    return render_template("uhome.html",
                           is_homepage=True,
                           name=g.user['name'],
                           score=score,
                           color=color)
