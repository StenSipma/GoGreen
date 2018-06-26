from flask import Blueprint, render_template

bp = Blueprint('tips', __name__, url_prefix='/tips')


@bp.route('')
def tips():
    return render_template("tips.html")
