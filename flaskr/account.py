from flask import Blueprint, render_template, request, flash
from flaskr.auth import login_required

bp = Blueprint('account', __name__, url_prefix='/account')


@bp.route('', methods=['GET', 'POST'])
@login_required
def account():
    if request.method == 'POST':
        flash('Successfully updated information', category='success')
    return render_template('account.html')
