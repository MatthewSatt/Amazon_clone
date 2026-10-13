from flask import Blueprint
from flask_login import current_user, login_required

from app.models import db

from .utils import json_body

user_routes = Blueprint('users', __name__)


@user_routes.route('/prime', methods=['PUT'])
@login_required
def set_prime():
    """Join or leave Prime. Send {"isPrime": bool}; omit it to toggle."""
    wanted = json_body().get('isPrime')
    current_user.isPrime = wanted if isinstance(wanted, bool) else not current_user.isPrime
    db.session.commit()
    return {'user': current_user.to_dict()}
