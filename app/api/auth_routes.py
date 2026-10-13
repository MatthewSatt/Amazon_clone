from flask import Blueprint
from flask_login import current_user, login_required, login_user, logout_user

from app.forms import LoginForm, SignUpForm
from app.models import User, db

from .utils import error, form_errors

auth_routes = Blueprint('auth', __name__)


@auth_routes.route('/')
def authenticate():
    """Current session's user, or null"""
    return {'user': current_user.to_dict() if current_user.is_authenticated else None}


@auth_routes.route('/login', methods=['POST'])
def login():
    form = LoginForm()
    if not form.validate_on_submit():
        return form_errors(form)

    user = User.query.filter(User.email == form.email.data).first()
    # One message for both cases so the form can't be used to discover accounts
    if not user or not user.check_password(form.password.data):
        return error('Incorrect email or password.', 401)

    login_user(user)
    return {'user': user.to_dict()}


@auth_routes.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return {'user': None}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    form = SignUpForm()
    if not form.validate_on_submit():
        return form_errors(form)

    user = User(
        username=form.username.data,
        email=form.email.data,
        password=form.password.data)
    db.session.add(user)
    db.session.commit()
    login_user(user)
    return {'user': user.to_dict()}, 201
